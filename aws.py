# Classe para salvar os dados da chave de conexão com o grupo de segurança da EC2 (AWS)

import boto3
from requests.models import Response

class AmazomWebServices:
    #Construtor
    def __init__(self, access_key, secret_key, region):
        self.access_key = access_key
        self.secret_key = secret_key
        self.region     = region
        self.client     = boto3.client('ec2', aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key, region_name=self.region)
        self.ec2        = boto3.client('ec2', aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key, region_name=self.region)
    
    # Função para listar os grupos de segurança
    def list_security_groups(self):
        try:
            response = self.client.describe_security_groups()
            print(response)
            return response
        except Exception as e:
            print(e)
            return None

    # Função para listar as regras de um grupo de segurança de acordo com o id do grupo
    def list_security_group_rules(self, group_id):
        try:
            response = self.client.describe_security_groups(GroupIds=[group_id])
            regras = []
            # Escreve cada regra do grupo de segurança
            for rule in response['SecurityGroups'][0]['IpPermissions']:
                for ipType in rule['IpRanges']:
                    print("Regras Ipv4: ", ipType['Description'])
                    regras.append(ipType['Description'])
                for ipType in rule['Ipv6Ranges']:
                    print("Regras Ipv6: ", ipType['Description'])
                    regras.append(ipType['Description'])
            return regras
            # print(response)
        except Exception as e:
            print(e)

    # Retorna as regras existentes no grupo de segurança
    def return_security_group_rules(self, group_id):
        try:
            response = self.client.describe_security_groups(GroupIds=[group_id])
            regras = []
            # Adiciona as regras existenes no grupo de segurança ao array regras
            for rule in response['SecurityGroups'][0]['IpPermissions']:
                for ipType in rule['IpRanges']:
                    regras.append(ipType['Description'])
                for ipType in rule['Ipv6Ranges']:
                    regras.append(ipType['Description'])
            return regras
        except Exception as e:
            print(e)
            exit()
        
    # Retorna os ips das regras existentes no grupo de segurança
    def return_security_group_ips(self, group_id):
        try:
            response = self.client.describe_security_groups(GroupIds=[group_id])
            ips = []
            # Adiciona os ip's das regras existentes no grupo de segurança ao array ips
            for rule in response['SecurityGroups'][0]['IpPermissions']:
                for ipType in rule['IpRanges']:
                    ips.append(ipType['CidrIp'])
                for ipType in rule['Ipv6Ranges']:
                    ips.append(ipType['CidrIpv6'])
            return ips
        except Exception as e:
            print(e)
            exit()
    
    # Função para adicionar uma regra de segurança em um grupo de segurança existente, recebendo como parametro a descrição, o ip da regra, o nome do grupo, a porta e o protocolo da regra.
    # Escreve o id da regra adicionada para poder remove-la no futuro.
    def add_security_group_rule(self, description, ip, group_id, port, protocol):
        try:
            # Primeiro checa se já existe uma regra com essa descrição no grupo de segurança
            regras = self.return_security_group_rules(group_id)
            for regra in regras:
                if regra == description:
                    print("Já existe uma regra com essa descrição no grupo de segurança")
                    exit()
            # Depois checa se já existe uma regra com esse ip no grupo de segurança
            ips = self.return_security_group_ips(group_id)
            for ip_regra in ips:
                if ip_regra == ip:
                    print("Já existe uma regra com esse ip no grupo de segurança")
                    exit()
            response = self.client.authorize_security_group_ingress(
                GroupId=group_id,
                IpPermissions=[
                    {
                        'IpProtocol': protocol,
                        'FromPort': port,
                        'ToPort': port,
                        'IpRanges': [
                            {
                                'CidrIp': ip,
                                'Description': description
                            },
                        ],
                    },
                ],
            )
            # print(response)
            # Após adicionar a regra, escreve o SecurityGroupRuleId da regra para poder removê-la no futuro.
            # Escreve os a descrição da regra, o ip, o grupo de segurança, a porta, o protocolo da regra e o ID da regra.
            print("Regra adicionada. Descrição: " + description + ", IP: " + ip + ", Grupo de segurança: " + group_id + ", Porta: " + str(port) + ", Protocolo: " + protocol + ", ID da regra: " + response['SecurityGroupRules'][0]['SecurityGroupRuleId'] + ".")
            # print(response['SecurityGroupRules'][0]['SecurityGroupRuleId'])
        except Exception as e:
            print(e)

    # Função para remover uma regra de segurança em especifico de um grupo de segurança especifico, obtendo os dados da regra existente e utilizando os mesmos para a remoção da regra.
    def remove_security_group_rule(self, description, group_id):
        # Primeiro obtem os dados da regra com o id que foi passado e que possui a descrição passada como parametro
        try:
            response = self.client.describe_security_groups(GroupIds=[group_id])
            for rule in response['SecurityGroups'][0]['IpPermissions']:
                if rule['IpRanges'][0]['Description'] == description:
                    print("Regra encontrada. ID da regra: " + rule['IpRanges'][0]['Description'])
                    # Após encontrar a regra, utiliza o mesmo id para remover a regra. Se não encontrar a regra, avisa
                    response = self.client.revoke_security_group_ingress(
                        GroupId=group_id,
                        IpPermissions=[
                            {
                                'IpProtocol': rule['IpProtocol'],
                                'FromPort': rule['FromPort'],
                                'ToPort': rule['ToPort'],
                                'IpRanges': [
                                    {
                                        'CidrIp': rule['IpRanges'][0]['CidrIp'],
                                        'Description': rule['IpRanges'][0]['Description']
                                    }
                                ]
                            }
                        ]
                    )
                    print("Regra encontrada e removida com sucesso.")
                    print("A regra possuia os seguintes dados:")
                    print("GroupId: " + group_id)
                    print("IpProtocol: " + rule['IpProtocol'])
                    print("FromPort: " + str(rule['FromPort']))
                    print("ToPort: " + str(rule['ToPort']))
                    print("CidrIp: " + rule['IpRanges'][0]['CidrIp'])
                    print("Description: " + rule['IpRanges'][0]['Description'])
                    # print("RuleId: " + response['SecurityGroupRules'][0]['SecurityGroupRuleId'])
                else:
                    print("Regra não encontrada.")
        except Exception as e:
            print(e)