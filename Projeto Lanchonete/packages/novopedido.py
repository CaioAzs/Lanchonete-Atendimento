from datetime import datetime
from packages.verificar import verificar_novo_pedido

def novopedido():
    nome = input("Insira seu nome: ") #As variáveis armazenam o cadastro do cliente.
    cpf = input("Digite seu CPF(somente números): ")
    senha = input("Insira sua senha: ")
    if verificar_novo_pedido(cpf) == True:
        pass  
    elif verificar_novo_pedido(cpf) == False:
        #Caso ainda não houver pedido com o cpf, cria-se um txt específico (com seu cpf como nome) para a pessoa, que conterá seus dados.
        registro_solo = open("./users/%s.txt" %cpf, "w", encoding="utf-8")
        registro_solo.write("{0}\n" "{1}\n" "{2}\n" .format(nome, cpf, senha))#O \n nessa situação ajuda a pular as linhas no txt, somente por organização.
        registro_solo.close()

        #Abrir um arquivo separado do extrato já no novo pedido(também com o cpf como nome , porém com o modelo "ext123.123.123-8.txt"), para facilitar posterior manipulação.
        extrato = open("./users/ext%s.txt" %cpf, "a", encoding="utf-8")

        for i in range(7): #Escreve no começo do extrato todas as quantidades iniciais dos produtos.
            extrato.write("0\n")

        #Abre o arquivo em modo append para adicionar o pedido gradualmente ao extrato.
        extrato.write("Nome: {}\n" .format(nome.capitalize())) #Write do nome do indivíduo.
        extrato.write("CPF: {}\n" .format(cpf)) #Write do cpf.
        extrato.write("Total = \n")
        data = datetime.now()
        data_br = data.strftime("%d/%m/%Y %H:%M")
        extrato.write("{}\n".format(data_br))
        extrato.write("Itens do pedido:\n")
        extrato.close()

        while True: #Serve para loopar o cardápio até que o cliente deseje sair.
            print(" ")
            print("Segue cardápio:")
            cardapio = [["Código", "Produto", "Preço"], 
                        [1, "X-Salada", "R$10,00"],
                        [2, "X-Burguer", "R$10,00"], 
                        [3, "Cachorro Quente", "R$7,50"],
                        [4, "Misto Quente", "R$8,00"], 
                        [5, "Salada de Frutas", "R$5,50"],
                        [6, "Refrigerante", "R$4,50"], 
                        [7, "Suco Natural", "R$6,25"]]

            for line in range(len(cardapio)): #Este for e o próximo leem a matriz e printam ela.
                for column in range(len(cardapio[line])):
                    print("{:<20}" .format(cardapio[line][column]), end=" ")
                print()
            
            code = input("Digite o código do produto: ")
            quant1 = input("Insira a quantidade: ")
            quant = float(quant1)

            def escrever(lanche, valor, linha):
                extrato = open("./users/ext%s.txt" %cpf, "a", encoding="utf-8") #Abre o arquivo e escreve o produto no extrato.
                extrato.write("{0} - {1}         - Preço unitário: R${2:.2f}  Valor: + {3:.2f}\n" .format(quant1, lanche,valor , quant*valor))
                extrato.close()

                extrato = open("./users/ext%s.txt" %cpf, "r")                            
                lines = extrato.readlines() #Lê as linhas do extrato para inserir as quantidades posteriormente.
                extrato.close()

                novo = int(quant1) + int(lines[linha]) #Refaz a quantidade do produto.
                del lines[linha] #Deleta a linha para ser inserida a nova.
                lines.insert(linha, "%s"%novo+"\n") #Insere a nova quantidade do produto.
                file = open("./users/ext%s.txt"%cpf, "w")
                file.writelines(lines) #Reescreve o arquivo.
                file.close()


            if code == "1":
                escrever(cardapio[1][1], 10.00, 0)
            elif code == "2":
                escrever(cardapio[2][1], 10.00, 1)
            elif code == "3":
                escrever(cardapio[3][1], 7.50, 2)
            elif code == "4":
                escrever(cardapio[4][1], 8.00, 3)
            elif code == "5":
                escrever(cardapio[5][1], 5.50, 4)
            elif code == "6":               
                escrever(cardapio[6][1], 4.50, 5)
            elif code == "7":              
                escrever(cardapio[7][1], 6.25, 6)
            else:
                print("\033[31mCódigo errado!")
                print("\033[m")

            confirmacao = input("Deseja adicionar mais algum produto (s/n)? ")
            if confirmacao == "s" or confirmacao == "S":
                print("Ok!")
                print(" ")
            else:
                break