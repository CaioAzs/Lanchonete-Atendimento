import os
from packages.verificar import verificar_geral

def cancelapedido():
    validacao_cpf = input("Valide seu cpf (somente números): ") #validação do cpf
    validacao_senha = input("Valide sua senha: ") #validação da senha
    if verificar_geral(validacao_cpf, validacao_senha) == False:
        pass
    elif verificar_geral(validacao_cpf, validacao_senha) == True:

            #CODIGO PRINCIPAL ->
            while True:
                confirmacao = input("Deseja realmente cancelar o pedido completo? (s/n)")
                if confirmacao == "s" or confirmacao == "S":
                    os.remove("./users/%s.txt" %validacao_cpf) #apaga o arquivo do cadastro
                    os.remove("./users/ext%s.txt" %validacao_cpf) #apaga o arquivo do extrato    
                    print("Ok, seu pedido foi cancelado.\n")
                    break
                elif confirmacao ==  "n" or confirmacao == "N":
                    break
                else:
                    "Digite somente 's' ou 'n', por favor.\n"