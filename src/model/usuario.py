from repository.usuario_repository import Usuario_dados
class Usuario_dados: 
    def __init__(self, nome, data_nascimento, idade, cadastro_CPF):
        self.nome_do_usuario = nome
        self.data_nascimento = data_nascimento
        self.idade_do_usuario = idade 
        self._cadastro_CPFcadastro_CPF = cadastro_CPF

@property
def nome_do_usuario(self):
    return self.nome_do_usuario

def data_nascimento(self): 
    return self.data_nascimento
 
def cadastro_CPF(self): 
    return self.cadastro_CFP 

def idade_do_usuario(self): 
        return self.idade 



#Funcões da classe

def InserirDados(self): 
    print("-----Cadastro de Usuário-----")
    nome_do_usuario = input("Insira seu nome: ")
    self.enviar_para_lista(nome_do_usuario)

    data_nascimento = input("Insira sua data de nascimento:")
    self.enviar_para_lista(data_nascimento)

    cadastro_CPF = input("Insira seu CPF:")
    self.enviar_para_lista(cadastro_CPF)

    idade_do_usuario = input("Insira sua idade") 
    self.enviar_para_lista(idade_do_usuario)

    Dados_usuarios = {
         "Nome": nome_do_usuario,
         "Data de Nascimento": data_nascimento,
         "CPF": cadastro_CPF,
         "Idade": idade_do_usuario
    }


    return Dados_usuarios