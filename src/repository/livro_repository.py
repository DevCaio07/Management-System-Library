#Responsavel por armazenar, buscar, atualizar e deletar os dados. Pasta responsavel 
# pelo gerenciamento de dados
import json
from model.livro import DicionarioLivros 

class DataLivross: 
    def __init__(self): 
        self.dataBook = DicionarioLivros()

        with open("DicionarioLivros.json", "w", encoding="utf-8") as arquivo: 
            json.dump(DicionarioLivros, arquivo, ensure_ascii=False, indent=4)
