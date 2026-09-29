# Camada model: onde fica as classes puras do négocio.
import json
from repository.livro_repository import DataLivross

class EmprestimoDeLivro: 

    def Consultar_Livro(self): 
        self.Nome_do_book = input("Qual o nome do livro desejado? ")


def fazer_busca(self): 
    with open('DataLivross.json', 'r', encoding="utf-08") as arquivo: 
        DataLivross = json.load(arquivo)

    nome_buscado = self.Nome_do_book 
    quantidade_minima = 1

    livros_filtrados = [ 
        DataLivross  for nome_do_livro in DataLivross
        if nome_buscado.lower() in DataLivross["nome_do_livro"] and nome_do_livro['Quantidade'] >= quantidade_minima
    ]
    for DataLivross in livros_filtrados: 
        print(f"Encontrado: {nome_buscado}")