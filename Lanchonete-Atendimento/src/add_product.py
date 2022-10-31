import os
from src.verify import verify_general
from src.menu import print_menu
from src.new_order import write_receipt

def add_product():
    validation_cpf = input("Validate your CPF (only numbers): ")
    validation_password = input("Validate your password: ")
    if verify_general(validation_cpf, validation_password) == False:
        return None
    elif verify_general(validation_cpf, validation_password) == True:
        # Main code ->
        while True:
            print_menu()
            code_ = input("Type the product code: ")
            try:
                code = int(code_)
            except:
                print("Type only a number, please.")
                return None

            quant_ = input("Type the amount: ")
            try:
                quant = int(quant_)
            except:
                print("Type only a number, please.")
                return None

            menu = open ("./src/menu.txt",'r',encoding = 'utf-8')
            menu_lines = menu.readlines()
            menu.close()

            try:
                write_receipt(validation_cpf, code, quant, menu_lines) 
            except:
                print("Error while writing the order. Please try again later.")

            confirmacao = input("Do you want to add more products (y/n)? ")
            if confirmacao == "y" or confirmacao == "Y":
                print("Ok!")
                print(" ")
            else:
                os.system("cls" if os.name == "nt" else "clear")
                break