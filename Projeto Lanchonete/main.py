from packages.novopedido import novopedido
from packages.cancelapedido import cancelapedido
from packages.insereproduto import insereproduto
from packages.cancelaproduto import cancelaproduto
from packages.valorpedido import valorpedido
from packages.extrato import extrato
import os

def main():
    while True:
        print("\n\033[34mObrigado por pedir na BurgerAZS, por favor siga para o menu: ")
        print("\033[34m1 - Novo Pedido")
        print("\033[34m2 - Cancela Pedido")
        print("\033[34m3 - Insere Produto")
        print("\033[34m4 - Cancela Produto")
        print("\033[34m5 - Valor do Pedido")
        print("\033[34m6 - Extrato do Pedido\n")
        print("\033[36m0 - Sair")
        print("\033[m")

        # Input principal do menu, transiciona entre os menus.
        menu = int(input())

        if menu == 0:
            print("Obrigado!")
            confirmacao = input("Caso deseje voltar para o menu, digite 0 novamente. ")
            if confirmacao == "0":
                os.system("cls" if os.name == "nt" else "clear")
                main()
            else:
                break
        elif menu == 1:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nNovo Pedido")
            novopedido()
        elif menu == 2:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nCancelar Pedido")
            cancelapedido()
        elif menu == 3:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nInserir Produto")
            insereproduto()
        elif menu == 4:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nCancelar Produto")
            cancelaproduto()
        elif menu == 5:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nValor do pedido")
            valorpedido()
        elif menu == 6:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nExtrato")
            extrato()
        else:
            print("\033[31mDigite um código válido, por favor.\n")

if __name__ == "__main__":
    main()