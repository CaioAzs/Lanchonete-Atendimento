import os

#This function is responsible for verifying if an order already exists.

def verify_new_order(cpf):
    if os.path.exists("./users/%s.txt" %cpf):
        print("\n\033[31mA order with this CPF already exists.")
        return True
    elif os.path.exists("./users/%s.txt" %cpf) == False:
        return False

#This function is responsible for verifying if the CPF and Password written is right.

def verify_general(validacao_cpf, validacao_senha):
    if os.path.exists("./users/%s.txt" %validacao_cpf):
        arq = open("./users/%s.txt" %validacao_cpf, "r")
        senha = arq.readlines()
        arq.close()
        if validacao_senha + "\n" in senha:
            return True
        else:
            print("\033[31mWrong password.")
            return False
    else:
        print("\033[31mIncorrect CPF or non-existent order.")
        return False