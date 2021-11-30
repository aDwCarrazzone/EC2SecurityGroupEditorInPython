# Classe para leitura de arquivo configuração json

import json

# Classe para leitura de arquivo configuração json
class Config:
    # Construtor
    def __init__(self, file):
        self.file = file
        self.data = {}
        self.load()

    # Carrega arquivo json
    def load(self):
        try:
            with open(self.file, 'r') as f:
                self.data = json.load(f)
        except:
            print("Erro ao abrir arquivo de configuração")
    
    # Retorna valor 0(nome) da chave ccl do "Group" recebido.
    def get_ccl(self, group):
        return self.data["Groups"][group][0]
    
    # Retorna o valor 1(id) da chave ccl do "Group" recebido.
    def get_id(self, group):
        return self.data["Groups"][group][1]

    # Retorna o access_key da AWS
    def get_aws_access_key(self):
        return self.data["AWS"]["access_key"]
    
    # Retorna o secret_key da AWS
    def get_aws_secret_access_key(self):
        return self.data["AWS"]["secret_key"]
    
    # Retorna a região da AWS
    def get_region(self):
        return self.data["AWS"]["region"]