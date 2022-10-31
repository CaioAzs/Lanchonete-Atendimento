import os
from datetime import datetime
from src.verify import verify_new_order
from src.menu import print_menu

#These functions is responsible for creating 2 txts (Registration and Receipt) for a user.
#It asks for the code and the amount of products the client wants.
#The client cannot use this function twice if the client has already used it before, because its a "new_order" function,
#If the client want to add more products, it should go to "Add a product" function.

def write_receipt(cpf, code, quant, menu_lines):
    receipt = open("./users/ext%s.txt" %cpf, "a", encoding="utf-8")
    for i in menu_lines:
        product = i.split(",")[1]
        price_ = i.split(",")[2]
        price = price_.strip("\n")
        if code == int(i.split(",")[0]):
            receipt.write("{0} - {1}         - Unitary Price: R${2:.2f}  Price: + {3:.2f}\n" .format(quant, product, float(price) , quant*float(price)))
    receipt.close()

    receipt = open("./users/ext%s.txt" %cpf, "r", encoding="utf-8")
    lines = receipt.readlines()
    receipt.close()

    new = quant + int(lines[code-1])
    del lines[code-1]
    lines.insert(code-1, "%s" %new+"\n")
    file = open("./users/ext%s.txt"%cpf, "w")
    file.writelines(lines)
    file.close()

def new_order():
    name = input("Type your name: ")
    if name == "":
        print("Please type the registration correctly.")
        return None
    cpf = input("Type your CPF(only numbers): ")
    if cpf == "":
        print("Please type the registration correctly.")
        return None
    password = input("Type your password: ")
    if password == "":
        print("Please type the registration correctly.")
        return None
    if verify_new_order(cpf) == True:
        return None
    else:
        new_register = open("./users/%s.txt" %cpf, "w", encoding="utf-8")
        new_register.write("{0}\n" "{1}\n" "{2}\n" .format(name, cpf, password))
        new_register.close()

        menu = open ("./src/menu.txt",'r',encoding = 'utf-8')
        menu_lines = menu.readlines()
        menu.close()

        receipt = open("./users/ext%s.txt" %cpf, "a", encoding="utf-8")
        for i in range(len(menu_lines)): #Used to count all items a client ordered.
            receipt.write("0\n")

        receipt.write("-\n")
        receipt.write("Name: {}\n" .format(name.capitalize()))
        receipt.write("CPF: {}\n" .format(cpf)) 
        receipt.write("Total = \n")
        date = datetime.now()
        date_br = date.strftime("%d/%m/%Y %H:%M")
        receipt.write("{}\n".format(date_br))
        receipt.write("Order Items:\n")
        receipt.close()

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

            try:
                write_receipt(cpf, code, quant, menu_lines) 
            except:
                print("Error while writing the order. Please try again later.")

            confirmation = input("Do you want to add more products (y/n)? ")
            if confirmation == "y" or confirmation == "Y":
                print("Ok!")
                print(" ")
            else:
                os.system("cls" if os.name == "nt" else "clear")
                break