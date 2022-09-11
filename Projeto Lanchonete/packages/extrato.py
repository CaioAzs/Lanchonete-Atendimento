from packages.verificar import verificar_geral

def extrato():
    validacao_cpf = input("Valide seu cpf (somente números): ") 
    validacao_senha = input("Valide sua senha: ") 
    if verificar_geral(validacao_cpf, validacao_senha) == False:
        pass
    elif verificar_geral(validacao_cpf, validacao_senha) == True:
            #CODIGO PRINCIPAL ->
            count = 0 #Contador do total a pagar
            extrato = open("./users/ext%s.txt" %validacao_cpf, "r", encoding="utf-8") 
            lines = extrato.readlines() #Lê todas as linhas do extrato.
            extrato.close()
            list = lines[12:] #Pega somente o extrato em si, sem as quantidades dos produtos acima.
            for line in list:
                lista = line.split()
                ultimo_item = lista[-1]
                total3 = float(ultimo_item)
                count = count + total3 #O count é o valorpedido, mesmo código.

            file = open("./users/ext%s.txt"%validacao_cpf, "r") #Abre o arquivo em modo leitura novamente, para organização e ter o código dividido em partes.
            lines = file.readlines()
            file.close()

            del lines[9] #Deleta o total antigo
            lines.insert(9, "Total = %.2f "%count + "\n") 
            file = open("./users/ext%s.txt"%validacao_cpf, "w") 
            file.writelines(lines)
            file.close()
            
            print(" ")
            print("******************************************************************************")
            ext = open("./users/ext%s.txt" %validacao_cpf, "r")
            texto = ext.readlines()
            extrato_completo = texto[7:]
            for linha in extrato_completo:
                print(linha, end="") #Print do arquivo do EXTRATO.
            ext.close()
            print("******************************************************************************")