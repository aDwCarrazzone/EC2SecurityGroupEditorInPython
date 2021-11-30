# Script para parsear argumentos da linha de comando e dependendo do argumento trazer informações de regras existentes, adicionar regras ou remover regras em um grupo de segurança de um EC2 (AWS).
# Autor: Andrew Vianna Carrazzone
# Data: 27/11/2021
VERSION = "1.0"


# Importação de bibliotecas
import argparse


# Importação de classes
from aws import AmazomWebServices as AWS
from config import Config
from requests import get
import re as regex


# Função de parseamento de argumentos
# -add:         Adiciona uma regra a um grupo de segurança passando a descrição como valor do argumento. Esse argumento só pode ser usado se os argumentos -group e -type forem passados.
# -remove:      Remove uma regra de um grupo de segurança passando a descrição como valor do argumento. Esse argumento só deve ser utilizado ao remover uma regra de um grupo de segurança. E não precisa de outros argumentos.
# -list:        Lista as regras existentes em um grupo de segurança passando o nome do grupo como valor do argumento.
# -ip:          Não é obrigatório passar o valor do argumento, caso não seja passado, o valor padrão é o IP da máquina. Esse argumento é responsavel por identificar o IP da máquina.
# -g, --group:  É obrigatorio passar o valor do argumento, caso não seja passado, a mensagem de erro será mostrada. Esse argumento é responsável por identificar o grupo de segurança.
# -t --type:    É obrigatorio passar o valor do argumento, caso não seja passado, a mensagem de erro será mostrada. Esse argumento é responsável por definir o tipo de regra que será adicionada.
# -version:     Exibe a versão do script.
# -help:        Exibe a ajuda do script.

def parse_args():
    parser = argparse.ArgumentParser(
        description="Script para parsear argumentos da linha de comando e dependendo do argumento trazer informações de regras existentes, adicionar regras ou remover regras em um grupo de segurança de um EC2 (AWS)."
    )
    parser.add_argument("-add",
                        help="Adiciona uma regra a um grupo de segurança passando a descrição como valor do argumento. Esse argumento só pode ser usado se os argumentos -group e -type forem passados.",
                        default="")
    parser.add_argument("-rem",
                        "--remove",
                        help="Remove uma regra de um grupo de segurança passando a descrição como valor do argumento. Esse argumento só deve ser utilizado ao remover uma regra de um grupo de segurança. E não precisa de outros argumentos.",
                        default="")
    parser.add_argument("-list",
                        help="Lista as regras existentes em um grupo de segurança passando o nome do grupo como valor do argumento.",
                        action="store_true")
    parser.add_argument("-ip",
                        help="Não é obrigatório passar o valor do argumento, caso não seja passado, o valor padrão é o IP da máquina. Esse argumento é responsavel por identificar o IP da máquina.",
                        default="")
    parser.add_argument("-g",
                        "--group",
                        help="É obrigatorio passar o valor do argumento, caso não seja passado, a mensagem de erro será mostrada. Esse argumento é responsável por identificar o grupo de segurança.",
                        default="")
    parser.add_argument("-t",
                        "--type",
                        help="É obrigatorio passar o valor do argumento, caso não seja passado, a mensagem de erro será mostrada. Esse argumento é responsável por definir o tipo de regra que será adicionada.",
                        default="")
    parser.add_argument("-version",
                        help="Exibe a versão do script.",
                        action="store_true")
    parser.add_argument("-help",
                        help="Exibe a ajuda do script.",
                        action="store_true")
    args = parser.parse_args()
    return args

# Define a porta da regra de acordo com o tipo recebido, RDP ou SSH. Caso não seja passado o tipo, ou seja passado um valor diferente de RDP ou SSH, a mensagem de erro será mostrada.
def define_port(type):
    if type.upper() == "RDP":
        port = 3389
    elif type.upper() == "SSH":
        port = 22
    else:
        print(type)
        print("Erro: O tipo de regra deve ser RDP ou SSH.")
        exit()
    return port

# Define o protocolo da regra de acordo com o tipo escolhio. SSH ou RDP.
def define_protocol(type):
    if type.upper() == "RDP":
        protocol = "TCP"
    elif type.upper() == "SSH":
        protocol = "TCP"
    else:
        print("Erro: O tipo de regra deve ser RDP ou SSH.")
        exit()
    return protocol

# Verifica se foi passado um ip, se não foi passado um ip, o ip padrão será o IP da máquina. Se for passado um ip mas o mesmo for invalido, a mensagem de erro será mostrada.
# Lembrando que o ip deve possuir /32 no final para que a regra seja válida.
def check_ip(ip):
    if ip == "":
        ip = get("https://api.ipify.org").text + "/32"
        return ip
    # Verifica se o ip é valido, se ele estiver no formato de ip mas sem o /32, ele será adicionado.
    elif regex.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip) and not regex.search(r"/32", ip):
        ip = ip + "/32"
        return ip
    # Verifica se o ip é valido, se ele estiver no formato de ip com o /32, ele será adicionado.
    elif regex.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/32$", ip):
        ip = ip
        return ip
    # Se o ip não for valido, a mensagem de erro será mostrada.
    else:
        print("Erro: O ip informado é inválido.")
        exit()

# Verifica se foi passado um grupo de segurança, se o grupo de segurança existe no arquivo de configuração json, se não foi passado um grupo de segurança ou o mesmo não existir, a mensagem de erro será mostrada.
# no arquivo de configuração json, o nome do grupo é obtido através da função config.get_ccl().
def check_group(group, config):
    if group == "":
        print("Erro: O grupo de segurança deve ser informado.")
        exit()
    elif group not in config.get_ccl(group):
        print("Erro: O grupo de segurança informado não existe.")
        exit()
    else:
        return config.get_id(group)

# Checa se a regra pode ser adicionada utilizando os checks anteriormente definidos.
# Se os argumentos -group e -type não forem passados, a mensagem de erro será mostrada.
# Se os argumentos -group e -type forem passados, o ip é verificado, o grupo de segurança é verificado e o tipo da regra é verificado.
def check_add(args, config):
    if args.group == "" or args.type == "":
        print("Erro: Os argumentos -g e -t devem ser passados. E não podem ser vazios.")
        exit()
    else:
        args.ip =       check_ip(args.ip)
        args.group =    check_group(args.group, config)
        args.protocol =     define_protocol(args.type)
        args.port =     define_port(args.type)
        return args

# Checa se a regra pode ser removida utilizando os checks anteriormente definidos.
# Se oo argumento -group não for passado, a mensagem de erro será mostrada.
# Os argumentos subsequentes serão adicionados ao objeto args durante o processo de remoção.
def check_remove(args, config):
    if args.group == "":
        print("Erro: O argumento -g deve ser passado.")
        exit()
    else:
        args.group =    check_group(args.group, config)
        return args

# Checa se a regra pode ser listada utilizando os checks anteriormente definidos.
# Se o argumento -group não for passado, a mensagem de erro será mostrada.
# Se o argumento -group for passado, o grupo de segurança é verificado.
def check_list(args, config):
    if args.group == "":
        print("Erro: O argumento -g deve ser passado.")
        exit()
    else:
        args.group =    check_group(args.group, config)
        return args

# Função principal do script.
def main():
    args    = parse_args()
    config  = Config("config.json")
    aws     = AWS(config.get_aws_access_key(), config.get_aws_secret_access_key(), config.get_region())
    if args.version:
        print("Version: " + VERSION)
    elif args.help:
        print("Help: " + HELP)
    elif args.add:
        args = check_add(args, config)
        aws.add_security_group_rule(args.add, args.ip, args.group, args.port, args.protocol)
    elif args.remove:
        args = check_remove(args, config)
        aws.remove_security_group_rule(args.remove, args.group)
    elif args.list:
        args = check_list(args, config)
        aws.list_security_group_rules(args.group)
    else:
        print("Erro: Argumento inválido.")
        exit()

HELP = """
    -add: Adiciona uma regra de segurança.
    -remove: Remove uma regra de segurança.
    -list: Lista as regras de segurança.
    -version: Mostra a versão do script.
    -help: Mostra a ajuda do script.
    -g: O nome do grupo de segurança.
    -t: O tipo da regra.
    -ip: O ip da regra.
"""

if __name__ == "__main__":
    main()