from packages.verificar import verificar_geral

def cancelaproduto():
    validacao_cpf = input("Valide seu cpf (somente números): ")
    validacao_senha = input("Valide sua senha: ") 
    if verificar_geral(validacao_cpf, validacao_senha) == False:
        pass
    elif verificar_geral(validacao_cpf, validacao_senha) == True:

            #CODIGO PRINCIPAL ->
            print(" ")
            print("Segue extrato de seu pedido, escolha o que cancelar: ") #Printa o extrato do cliente até o momento, para que possa
            arq = open('./users/ext%s.txt' %validacao_cpf, "r")                    #pegar o código e quantidade que deseja cancelar.
            texto = arq.readlines()
            arq.close()
            list = texto[11:]
            print(" ")
            for linha in list:
                print(linha.strip())

            print(" ")
            print("\033[m************************************************")
            #Informa novamente o código dos produtos, caso o cliente não lembre.
            print("""           \033[32mCódigos dos produtos:      
                X-Salada = 1 
                X-burger = 2
                Cachorro Quente = 3
                Misto quente = 4 
                Salada de Frutas = 5
                Refrigerante = 6
                Suco Natural = 7""")
            print("\033[m*************************************************")

            cardapio = [["Código", "Produto", "Preço"], 
                        [1, "X-Salada", "R$10,00"],
                        [2, "X-Burguer", "R$10,00"], 
                        [3, "Cachorro Quente", "R$7,50"],
                        [4, "Misto Quente", "R$8,00"], 
                        [5, "Salada de Frutas", "R$5,50"],
                        [6, "Refrigerante", "R$4,50"], 
                        [7, "Suco Natural", "R$6,25"]]

            code = input("Digite o código do produto que deseja cancelar: ")
            quant1 = input("Insira a quantidade: ")
            quant = float(quant1)



            def escrever(lanche, valor, linha):
                extrato = open("./users/ext%s.txt" %validacao_cpf, "a", encoding="utf-8") #Abre o arquivo e escreve o produto no extrato.
                extrato.write("{0} - {1}         - Preço unitário: R${2:.2f} - CANCELADO Valor: -{3:.2f}\n" .format(quant1, lanche,valor , quant*valor))
                extrato.close()
                
                extrato = open("./users/ext%s.txt" %validacao_cpf, "r")                            
                lines = extrato.readlines()
                extrato.close()

                novo = int(lines[linha]) - int(quant) #Refaz a quantidade do produto, reduzindo o produto desejado.
                del lines[linha] #Deleta a linha da quantidade do produto para sua inserção posterior.
                lines.insert(linha, "%s" %novo + "\n") #Insere a nova quantidade do produto.
                file = open("./users/ext%s.txt"%validacao_cpf, "w")
                file.writelines(lines)#Reescreve o arquivo.
                file.close() 

            #Somente o primeiro IF será comentado pois os outros só mudam o produto a ser cancelado.
            if code == "1": #TODOS os extrato.write devem colocar no arquivo ext(cpf).txt o pedido cancelado.
                extrato = open("./users/ext%s.txt" %(validacao_cpf), "r") 
                lines = extrato.readlines()
                extrato.close()
                #O if a seguir serve para prevenir que o cliente remova mais itens do que ele pediu.
                if int(lines[0]) - int(quant) >= 0: 
                    escrever("X-salada", 10.00, 0) #Executa a função principal de remoção.
                else:
                    print("\033[31mInsira uma quantidade válida!") #Caso o usuário não coloque uma quantidade válida, ele cai nesse else.

            elif code == "2":
                extrato = open("./users/ext%s.txt" %(validacao_cpf), "r") 
                lines = extrato.readlines()
                extrato.close()
                if int(lines[1]) - int(quant) >= 0: 
                    escrever("X-burger", 10.00, 1) 
                else:
                    print("\033[31mInsira uma quantidade válida!")

            elif code == "3":
                extrato = open("./users/ext%s.txt" %(validacao_cpf), "r") 
                lines = extrato.readlines()
                extrato.close()
                if int(lines[2]) - int(quant) >= 0: 
                    escrever("Cachorro quente", 7.50, 2) 
                else:
                    print("\033[31mInsira uma quantidade válida!")    

            elif code == "4":
                extrato = open("./users/ext%s.txt" %(validacao_cpf), "r") 
                lines = extrato.readlines()
                extrato.close()
                if int(lines[3]) - int(quant) >= 0: 
                    escrever("Misto quente", 8.00, 3) 
                else:
                    print("\033[31mInsira uma quantidade válida!")  

            elif code == "5": 
                extrato = open("./users/ext%s.txt" %(validacao_cpf), "r") 
                lines = extrato.readlines()
                extrato.close()
                if int(lines[4]) - int(quant) >= 0: 
                    escrever("Salada de frutas", 5.50, 4) 
                else:
                    print("\033[31mInsira uma quantidade válida!")

            elif code == "6":
                extrato = open("./users/ext%s.txt" %(validacao_cpf), "r") 
                lines = extrato.readlines()
                extrato.close()
                if int(lines[5]) - int(quant) >= 0: 
                    escrever("Refrigerante", 4.50, 5) 
                else:
                    print("\033[31mInsira uma quantidade válida!")

            elif code == "7":
                extrato = open("./users/ext%s.txt" %(validacao_cpf), "r") 
                lines = extrato.readlines()
                extrato.close()
                if int(lines[6]) - int(quant) >= 0: 
                    escrever("Suco natural", 6.25, 6)
                else:
                    print("\033[31mInsira uma quantidade válida!")

            else:
                print("\033[31mCódigo errado!")
            