class Livros: 
    def __init__(self, nome_do_livro, autor_do_livro, ano_de_lancamento, quantidade_deExemplares):
        self.nome_do_livro = nome_do_livro
        self.autor_do_livro = autor_do_livro 
        self.ano_de_lancamento = ano_de_lancamento
        self.quantidade_deExemplares = quantidade_deExemplares

@property
def nome_do_livro(self): 
    return self.nome_do_livro

def autor_do_livro(self): 
    return self.autor_do_livro

def ano_de_lancamento(self): 
    return self.ano_de_lancamento 

def quantidade_deExemplares(self): 
    return self.quantidade_deExemplares 


#Funcoes da classe Livros

def InserirDadosLivro(self): 
    print("Cadastro de Livros")

    nome_do_livro = input("Insira o nome do livro:") 
    self.enviar_para_bd(nome_do_livro)

    autor_do_livro = input("Insira o autor:" )
    self.enviar_para_bd(autor_do_livro) 

    ano_de_lancamento = input("Insira o ano de lançamento")
    self.enviar_para_bd = 