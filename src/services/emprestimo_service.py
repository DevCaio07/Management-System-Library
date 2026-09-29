from model.livro import Livros

class Validacao_de_Livros: 
    def validar_emprestimo(Livros): 
        if(quantidade_deExemplares > 1): 
            print("Esse livro pode ser emprestado") 
        else: 
            print("este livro nao está disponivel")