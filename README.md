# EC2 Security Group Editor In Python

## Conteúdo
 ![cover](.assets/cover.png)
 - [Introdução](#introdução)
 - [Visão Geral](#visaogeral)
 - [Iniciando](#iniciando)
 - [Modo de uso](#uso)
 - [Exemplos de uso](#exemplodeuso)
 - [Conclusão](#conclusões)
 - [Referências](#referências)
 - [Licença](#licença)

# Introdução
> Script que parsea instruções, sejam elas para adicionar, remover ou lista as regras de um grupo de segurança da AWS.<br>
> Todo o código leva como príncipio que cada classe deve ter um único propósito, a config obtem os dados de configuração, a AWS envia e retorna dados da AWS e a main parsea os comandos.<br>
> Esse projeto tem como objetivo ser implementado juntamente de uma esteira para que seja possível gerar uma auditoria das regras que são criadas.<br>

# Visão Geral
> O projeto usa dados recebidos do usuário para listar, adicionar ou remover regras de um grupo de segurança de um Amazon EC2<br>
> <br>
> De acordo com a instrução parseado ele:<br>

# Iniciando
> - Clone o repositorio:
>```bash
> > git clone 'https://github.com/aDwCarrazzone/EC2SecurityGroupEditorInPython'
>```
>
> - Instale as dependencias:
>```bash
> > pip install -r requirements.txt
>```
>
> - Configure o arquivo de configuração: [config.json](config.json) com os dados necessários: <br>
> <br>
>    - Grupos: <br>
>     Os grupos com seus nomes a ser passado na opção -g e seus ids.<br>
> <br>
>   - AWS:<br>
>     Os dados necessários para que seja feito a conexão através da AWS. <br>
> <br>
> - E então utilizando o "argparse" para inferencia
>```
> > python main.py -help ou outro comando desejado.
>```
> Pronto! Agora é só usar o [Modo de uso](#Mododeuso).<br>
><br>

# Modo de uso
> - Opções:
>```
> -ip: Define o ip para que a regra será criada, caso não passado será utilizado o ip da máquina por padrão;
> -g: Essa instrução é utilizada para passar o valor do argumento responsável por identificar o grupo de segurança que será utilizado durante o processo da script;
> -t: Essa instrução é utilizada para passar o valor do argumento responsável por identificar o tipo da regra a ser criada, RDP ou SSH;
>
> -> O argumento -ip não é obrigatório e só é utilizado em caso de necessidade especifica pois o script já utiliza o ip da máquina por padrão.
>
>```
> - Comandos:
> ```
>   -add: Adiciona uma regra a um grupo de segurança passando a descrição como argumento. Essa instrução só é parseada se as instruções -g (--group) e -t (--type) forem passadas juntamente;
>   -rem: Remove uma regra de um grupo de segurança passando a descrição como valor do argumento. Essa instrução só é parseada se a instrução -g (--group) for passada juntamente;
>   -list: Lista as regras existentes em um grupo de segurança, essa instrução só é parseada se a instrução -g (--group) for passada juntamente;
>   -v: Essa instrução é utilizada para trazer a versão da script.
>   -help: Essa instrução é utilizada para exibir a ajuda do script.
> ```

# Exemplos de uso:
> - Adicionar uma regra RDP com a descrição AcessoRDP ao grupo GrupoDeExemplo
> ```
> python main.py -add AcessoRDP -g GrupoDeExemplo -t RDP
> ```
>  Assim adicionando uma regra no GrupoDeExemplo.<br>
>
> - Remover uma regra com a descrição AcessoRDP no grupo GrupoDeExemplo
> ```
> python main.py -rem AcessoRDP -g GrupoDeExemplo
> ```
>   Assim removendo a regra AcessoRDP que está no GrupoDeExemplo
>
> - Lista as regras existentes no grupo GrupoDeExemplo
>
> ```
> python main.py -list -g GrupoDeExemplo
> ```
>   Assim listando as regras existentes em GrupoDeExemplo.

# Conclusão

# Referencias
> - [1]

# Licença
> temp