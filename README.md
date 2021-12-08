# EC2 Security Group Editor In Python
 ![cover](assets/unicep-cover.png)
## Conteúdo
> - [Introdução](#Introdução)
> - [Visão Geral](#Visão-geral)
> - [Iniciando](#iniciando)
> - [Modo de uso](#modo-de-uso)
> - [Exemplos de uso](#exemplos-de-uso)
> - [Conclusão](#Conclusão)
> - [Referências](#Referências)
> - [Agradecimentos](#agradecimentos)
> - [Licença](#licença)

# Introdução

## Introdução aos termos
> Durante toda a leitura você será apresentado á alguns termos que possivelmente não conhecerá, darei uma breve explicação sobre esses termos e sempre que eu citar os mesmos você poderá seguir os hiperlinks apresentados para ler mais sobre eles.
> * AWS: Amazon Web Services é uma subsidiária da Amazon que fornece através de seu conjunto de serviços, plataformas de computação em nuvem.<br>
> * EC2: Amazon Elastic Compute Cloud faz parte da plataforma de computação em nuvem da AWS, essa parte em especifica é a que permite alugar computadores virtuais.<br>
> * Grupo de segurança: O grupo de segurança atua como o firewall virtual para as máquinas EC2, controlando as regras de entrada e saída de tráfego para a mesma.<br>
> * Parcear: Parcear é um termo informal vindo de Parsing em inglês, que nesse contexto significa obter comandos e opções recebidas a partir do usuário.<br>
> * Esteira: O conceito de esteira seria referente a uma esteira de entrega contínua, onde, a script pode ser implementada para a criação e remoção de regras.

## Introdução a script
> Script que parcea instruções, sejam elas para adicionar, remover ou lista as regras de um grupo de segurança de uma ou mais EC2.<br>
> Todo o código leva como principio que cada classe deve ter um único propósito, a config obtem os dados de configuração, a AWS envia e retorna dados da AWS e a main parsea os comandos e opções.<br>
> Esse projeto tem como objetivo ser implementado juntamente de uma esteira para que seja possível gerar uma auditoria das regras que são criadas. Mas nada impede a utilização do mesmo sem a esteira, ele possui inclusive um arquivo de configurações onde é possivel colocar os dados da chave de aceso e da região.<br>

# Visão Geral
> O projeto usa dados recebidos do usuário para listar, adicionar ou remover regras de um grupo de segurança de um Amazon EC2<br>
> <br>

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
> 
>     Caso seja implementado a esteira é necessario alterar a linha 158 do código [main.py](main.py) com as credenciais correspondentes.<br>
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
>   -add: Adiciona uma regra a um grupo de segurança passando a descrição como argumento. Essa instrução só é parceada se as instruções -g (--group) e -t (--type) forem passadas juntamente;
>   -rem: Remove uma regra de um grupo de segurança passando a descrição como valor do argumento. Essa instrução só é parceada se a instrução -g (--group) for passada juntamente;
>   -list: Lista as regras existentes em um grupo de segurança, essa instrução só é parceada se a instrução -g (--group) for passada juntamente;
>   -v: Essa instrução é utilizada para trazer a versão da script.
>   -help: Essa instrução é utilizada para exibir a ajuda do script.
> ```
> <br>

# Exemplos de uso
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
> Ao fazer o uso da script e da esteira de forma apropriada pode-se obter um ambiente de trabalho mais seguro e rápido para entregar resultados. Denota-se que a script não precisa de forma obrigatória da esteira para seu funcionamento, porém, a intenção da script é que ela seja utilizada juntamente com a esteira para que seja possível obter-se uma auditoria desse processo, de quem adicionou ou removeu uma regra, quando foi feito e quantas vezes.
> 
# Referências
> - [Boto3 Docs 1.20.21 - Working with security groups](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-security-group.html)
> - [Classification and Gradient-based Localization of Chest Radiographs](https://github.com/priyavrat-misra/xrays-and-gradcam#readme)
> - [Amazing GitHub Template](https://github.com/dec0dOS/amazing-github-template#readme)

# Agradecimentos
> - Primeiramente a Deus, meus familiares, minha namorada e sua família:<br>
    ```Que tiveram que me tolerar e aguentar durante esse tempo isolado escrevendo isso.```
>
> - Aos Professores da faculdade [UNICEP](https://unicep.edu.br/rioclaro) e todo suporte dado:<br>
  ```mesmo que eu tenha demorado muito para escolher um tema para apresentar```
>
>- Apesar de não encontrar exatamente o que eu queria, a documentação:<br>
  [Boto3 Docs 1.20.21 - Working with security groups](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-security-group.html)
>
>- Aos projetos:<br>
[Classification and Gradient-based Localization of Chest Radiographs](https://github.com/priyavrat-misra/xrays-and-gradcam#readme)<br>
[Amazing GitHub Template](https://github.com/dec0dOS/amazing-github-template#readme)<br>
```Que ajudaram muito a escrever esse leia-me de uma forma mais agradável e legível.```

# Metodologia
> A criação desse script partiu da necessidade de uma maior segurança ao ambiente da AWS e de maior velocidade para adicionar as regras aos grupos de segurança.<br>
> Durante todo o processo foi prestado muita atenção para que ficasse de facil entendimento o processa da script, tentando ser o mais simples sempre que possível e sempre criando comentários no código.<br>
> Como fonte inicial para que fosse possível o desenvolvimento da mesma foi utilizado a documentação do Boto3, todo o processo utiliza seus metodos apresentados na documentação. Toda a base do desenvolvimento foi utilizando essa documentação.

# Licença
