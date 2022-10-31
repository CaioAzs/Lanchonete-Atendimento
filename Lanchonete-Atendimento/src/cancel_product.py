from src.verify import verify_general
from src.menu import print_menu
import os

#This function is responsible for deleting a specific product chosen by the user.
#The program does not allow the user to delete more than it ordered.
def write_receipt_canceling(cpf, code, quant, menu_lines):
    receipt = open("./users/ext%s.txt" %cpf, "a", encoding="utf-8")
    for i in menu_lines:
        product = i.split(",")[1]
        price_ = i.split(",")[2]
        price = price_.strip("\n")
        if code == int(i.split(",")[0]):
            receipt.write("{0} - {1}         - Unitary Price: R${2:.2f} - *CANCELED* - Price: -{3:.2f}\n" .format(quant, product, float(price) , quant*float(price)))
    receipt.close()

    receipt = open("./users/ext%s.txt" %cpf, "r", encoding="utf-8")
    lines = receipt.readlines()
    receipt.close()

    new = quant - int(lines[code-1])
    del lines[code-1]
    lines.insert(code-1, "%s" %new+"\n")
    file = open("./users/ext%s.txt"%cpf, "w")
    file.writelines(lines)
    file.close()

def cancel_product():
    validation_cpf = input("Validate your CPF (only numbers): ")
    validation_password = input("Validate your password: ")

    if verify_general(validation_cpf, validation_password) == False:
        return None
    elif verify_general(validation_cpf, validation_password) == True:
        # Main code ->
        print("***********************************************")
        print_menu()
        print("***********************************************")
        print("This is your receipt, please select the the product you want to cancel: ")
        receipt = open('./users/ext%s.txt' % validation_cpf, "r")
        receipt_lines = receipt.readlines()
        receipt.close()
        spacer = "-\n"
        index = receipt_lines.index(spacer) + 5
        for i in receipt_lines[index:]:
            print(i.strip("\n"))

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

        #Verifying if the amount typed is bigger than the amount the client ordered
        receipt = open("./users/ext%s.txt" %validation_cpf, "r", encoding="utf-8")
        receipt_lines  = receipt.readlines()
        receipt.close()

        for i in receipt_lines[:receipt_lines.index(spacer) + 1]:
            
            if int(receipt_lines[code-1]) - quant < 0:
                print("Type a valid amount of products, please.")
                return None

        menu = open ("./src/menu.txt",'r',encoding = 'utf-8')
        menu_lines = menu.readlines()
        menu.close()

        try:
            write_receipt_canceling(validation_cpf, code, quant, menu_lines) 
        except:
            print("Error while writing the order. Please try again later.")

        os.system("cls" if os.name == "nt" else "clear")
