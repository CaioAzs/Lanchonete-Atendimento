from packages.verificar import verificar_geral

def valorpedido():
    validacao_cpf = input("Valide seu cpf (somente números): ")
    validacao_senha = input("Valide sua senha: ")
    if verificar_geral(validacao_cpf, validacao_senha) == False:
        pass
    elif verificar_geral(validacao_cpf, validacao_senha) == True:
        
            #CODIGO PRINCIPAL ->
            count = 0 #Contador do total a pagar
            extrato = open("./users/ext%s.txt" %validacao_cpf, "r", encoding="utf-8") #Abre o arquivo de extrato em modo leitura para ler todos os pedidos.
            lines = extrato.readlines() #Lê todas as linhas do extrato.
            list = lines[12:] #Como é necessário somente a parte dos pedidos(por que tem o nome, cpf, total e data em cima) faz-se o slicing.
            for line in list:
                lista = line.split() #Divide-se no espaço para formar uma lista em que o índice -1 seja o valor do pedido.
                ultimo_item = lista[-1]
                total3 = float(ultimo_item)
                count = count + total3 #Soma todos os pedidos(até os cancelados).

            print("\n*****************************************")
            print("O total a pagar atual do pedido é: R$%.2f"%count)
            print("*****************************************\n")
            
            extrato.close()
