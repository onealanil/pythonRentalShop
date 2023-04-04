import display
import someFunctions
import invoiceRent
from colorama import Fore, Style, Back


def rentCostume():
    # displaying the costume 
    display.displayCostume()

    # valid name 
    name = someFunctions.checkNameForRent()

    # valid address 
    address = someFunctions.checkAddressForRent()
    phone = input("Enter your phone number: \n-> ")
    secret_key = input(
        "Enter your secret key, which you need while returning costume: \n-> ")
    # displaying costume 
    dict = someFunctions.costumeCollection()

    # valid id and quantity 
    check = someFunctions.checkIdAndQuantity()

    if check[0] == 0 or check[1] == 0:
        check
    else:
        id = check[0]
        quantity = check[1]

        with open("./data/data.txt", 'r') as file:
            listOfLines = file.readlines()
            listOfLines[id-1] = listOfLines[id -
                                            1].replace(dict[id][3], " " + str(int(dict[id][3])-quantity))
        file.close()
        with open("./data/data.txt", 'w') as file:
            file.writelines(listOfLines)
        file.close()

        price = dict[id][2]
        tp = float(price[2:len(price)]) * quantity
        
        # generating the invoice for rent 
        invoiceRent.invoiceGenerator(
            name, address, phone, tp, dict[id][0], dict[id][1])

        print(f'{Back.GREEN}{Fore.YELLOW} Successfully rented, check invoice for more details{Style.RESET_ALL}')
        print()
        
        # adding the data into secret file 
        someFunctions.detailsOfRent(name, quantity, secret_key, dict[id][0], tp)

        while True:
            rentAgain = input("Do you want to rent again? (Y/N) \n-> ")

            if rentAgain == "Y" or rentAgain == "y":
                return rentCostume()
            elif rentAgain == "N" or rentAgain == "n":
                break
            else:
                print(
                    f'{Back.RED}{Fore.YELLOW} Incorrect option, Choose (Y/N) or (y/n){Style.RESET_ALL}')
                continue
