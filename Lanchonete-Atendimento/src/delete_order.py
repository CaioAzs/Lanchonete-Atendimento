import os
from src.verify import verify_general

#This function is responsible for deleting the registration and receipts files if the user wants to.
def delete_order():
    validation_cpf = input("Validate your CPF (only numbers): ")
    validation_password = input("Validate your password: ")
    if verify_general(validation_cpf, validation_password) == False:
        return
    elif verify_general(validation_cpf, validation_password) == True:
            #Main code ->
            while True:
                confirmation = input("Are you completely sure you want to delete the order? (y/n)")
                if confirmation == "y" or confirmation == "Y":
                    os.remove("./users/%s.txt" %validation_cpf) #Delete the registration file.
                    os.remove("./users/ext%s.txt" %validation_cpf) #Delete the receipt file.    
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Ok, your order has been canceled.\n")
                    break
                elif confirmation ==  "n" or confirmation == "N":
                    break
                else:
                    "Type only 'y' or 'n', please.\n"