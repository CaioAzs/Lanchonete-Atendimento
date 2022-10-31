import os
from src.new_order import new_order
from src.delete_order import delete_order
from src.add_product import add_product
from src.cancel_product import cancel_product
from src.print_receipt import print_receipt

def main():
    while True:
        print("\n\033[34mThanks for ordering at BurgerAZS, here is the menu: ")
        print("\033[34m1 - New Order")
        print("\033[34m2 - Delete Order")
        print("\033[34m3 - Add Product")
        print("\033[34m4 - Cancel Product")
        print("\033[34m5 - Order Receipt\n")
        print("\033[36m0 - Exit")
        print("\033[m")

        # Loops the main menu.
        menu = int(input())

        if menu == 0:
            print("Thank You!")
            confirmacao = input("In case you want to go back to the menu, type 0 again. ")
            if confirmacao == "0":
                os.system("cls" if os.name == "nt" else "clear")
                main()
            else:
                break
        elif menu == 1:
            os.system("cls" if os.name == "nt" else "clear")
            print("\n\033[34m<===New Order===>\033[m")
            new_order()
        elif menu == 2:
            os.system("cls" if os.name == "nt" else "clear")
            print("\n\033[34m<===Delete Order===>\033[m")
            delete_order()
        elif menu == 3:
            os.system("cls" if os.name == "nt" else "clear")
            print("\n\033[34m<===Add Product===>\033[m")
            add_product()
        elif menu == 4:
            os.system("cls" if os.name == "nt" else "clear")
            print("\n\033[34m<===Cancel Product===>\033[m")
            cancel_product()
        elif menu == 5:
            os.system("cls" if os.name == "nt" else "clear")
            print("\n\033[34m<===Receipt===>\033[m")
            print_receipt()
        else:
            print("\033[31mType a valid code, please.\n")

if __name__ == "__main__":
    main()