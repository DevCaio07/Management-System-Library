import json
from model.usuario import Dados_dos_Usuarios
class DadosJson: 
    def __init__(self):
        self.data = Dados_dos_Usuarios()

    with open("Dados_dos_Usuarios.json", "w", encoding= "utf-8") as arquivo: 
        json.dump(Dados_dos_Usuarios, arquivo, ensure_ascii=False, indent=4)
    
