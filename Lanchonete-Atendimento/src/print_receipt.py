from src.verify import verify_general

#This function is responsible for printing the txt of the receipt on the terminal.
def print_receipt():
    validation_cpf = input("Validate your CPF (only numbers): ")
    validation_password = input("Validate your password: ")

    if verify_general(validation_cpf, validation_password) == False:
        return None
    elif verify_general(validation_cpf, validation_password) == True:
        receipt = open("./users/ext%s.txt" %validation_cpf, "r", encoding="utf-8")
        receipt_lines = receipt.readlines()
        receipt.close()
        total = 0 #Total of money at the end of the order
        spacer = "-\n"
        index = receipt_lines.index(spacer) + 6
        for i in receipt_lines[index:]:
            list = i.split()
            last_item = float(list[-1])
            total += last_item

        index_total = receipt_lines.index(spacer) + 3

        del receipt_lines[index_total]
        receipt_lines.insert(index_total, "Total = %.2f "%total + "\n")
        receipt = open("./users/ext%s.txt"%validation_cpf, "w") 
        receipt.writelines(receipt_lines)
        receipt.close()

        print("\n******************************************************************************")
        receipt = open("./users/ext%s.txt" %validation_cpf, "r")
        text = receipt.readlines()
        complete = text[index-6:]
        for i in complete:
            print(i, end="")
        receipt.close()
        print("******************************************************************************\n")