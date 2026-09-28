from .model.usuario import InserirDados


class Main: 
    def executar(self): 
        print("Iniciando Sistema de Gerenciamento de Biblioteca")

        data_user = InserirDados()

        print(data_user)