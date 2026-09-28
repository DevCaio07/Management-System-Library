# Camada model: onde fica as classes puras do négocio.
from repository.livro_repository import DataLivross

class EmprestimoDeLivro: 

    def Consultar_Livro(self): 
        self.Nome_do_book = input("Qual o nome do livro desejado? ")
        
        