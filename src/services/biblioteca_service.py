# Concentra todas as REGRAS de négocio mais complexas(Ex: validar se o usuario pode pegar um livro)
#(emprestado, calcular multas)
#Regra 1: Usuario só deve poder ser criado se for maior de 18  
#Regra 2: 
from model.usuario import Usuario_dados

class Validar_idade(Usuario_dados): 
    def Validacao_usuario(self): 
        if(self.idade_do_usuario >= 18):
            print("Prossiga com o cadastro!") 
        else: 
            print("Não é permitido usuários menores de idade")
            return 0 

        