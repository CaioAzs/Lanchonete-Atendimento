#This function prints the menu on the terminal.
#It uses the txt with the products informations.
def print_menu():
    menu = [["\nCode", "Product", "Price"]]
    with open ("./src/menu.txt",'r',encoding = 'utf-8') as file:
        file = file.readlines()
        count = 0
        for i in file:
            count+=1
            product = i.split(",")[1]
            price = i.split(",")[2]
            menu.append([count, product, price.strip("\n")])
    for line in range(len(menu)): #Este for e o próximo leem a matriz e printam ela.
        for column in range(len(menu[line])):
            print("{:<20}" .format(menu[line][column]), end=" ")
        print()

#If someone wants to add more products, just follow the pattern of the file menu.txt