import os

def verificar_novo_pedido(cpf):
    if os.path.exists("./users/%s.txt" %cpf):
        print("\n\033[31mJá existe um pedido cadastrado neste CPF.")
        return True
    elif os.path.exists("./users/%s.txt" %cpf) == False:
        return False

def verificar_geral(validacao_cpf, validacao_senha):
    if os.path.exists("./users/%s.txt" %validacao_cpf):
        arq = open("./users/%s.txt" %validacao_cpf, "r")
        senha = arq.readlines()
        arq.close()
        if validacao_senha + "\n" in senha:
            return True
        else:
            print("\033[31mSenha errada :(")
            return False
    else:
        print("\033[31mCPF errado ou pedido inexistente :(")
        return False