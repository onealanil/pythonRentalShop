from datetime import datetime
import someFunctions
import invoiceReturn
from colorama import Fore, Style, Back


def returnCostume():
    while True:
        try:
            date_string = input(
                "Enter the renting in the format YY-MM-DD: \n->")
            dt = datetime.strptime(date_string, '%Y-%m-%d')
            days = str(datetime.now() - dt)
            daysArr = days.split(" ")
            break
        except:
            print(
                f'{Back.RED}{Fore.YELLOW}Date must be in YY-MM-DD format{Style.RESET_ALL}')
            continue

    myArr = []
    newArr = []
    index = 0
    found = False
    secret_key = input("Enter the secret key : \n->")
    with open("allRentSecretDetails.txt", 'r') as file:
        data = file.read().splitlines()
        for i in range(len(data)):
            myArr = myArr + [data[i].split(", ")]
        data = file.readlines()
    file.close()

    # searching for secret key 
    for i in myArr:
        if secret_key in i:
            index = myArr.index(i)
            for j in myArr[index]:
                newArr.append(j)
                found = True
    if found == False:
        print(
            f'{Back.RED}{Fore.YELLOW} We did not found you in renting list {Style.RESET_ALL}')

    if newArr != []:
        name = input("Enter the exact name of the user: \n-> ")

        try:
            quantity = int(input("Enter the exact quantity you rented: \n-> "))

            if quantity == int(newArr[1]) and name+"s" == newArr[0]:
                message = someFunctions.returnDateTime(daysArr)
                if message == "noFine" or message == "today":
                    invoiceReturn.invoiceGeneratorReturn(
                        name, newArr[3], newArr[1], newArr[4], days, 0)
                elif message == "fine":
                    invoiceReturn.invoiceGeneratorReturn(
                        name, newArr[3], newArr[1], newArr[4], days, 1000)
                print()
                print(
                    f'{Back.GREEN}{Fore.YELLOW} Successfully returned, check invoice for more details{Style.RESET_ALL}')

                print()

                id = int(someFunctions.costumeNameReturn(newArr[3]))
                # adding the quantity in file
                dict = someFunctions.costumeCollection()

                with open("./data/data.txt", 'r') as file:
                    listOfLines = file.readlines()
                    listOfLines[id] = listOfLines[id].replace(
                        dict[id+1][3], " " + str(int(dict[id+1][3]) + quantity))
                file.close()
                with open("./data/data.txt", 'w') as file:
                    file.writelines(listOfLines)
                file.close()

            else:
                print(
                    f'{Back.RED}{Fore.YELLOW} You do not rent from our store. Your quantity or username does not match{Style.RESET_ALL}')
        except:
            print(f'{Back.RED}{Fore.YELLOW}quantity is invalid{Style.RESET_ALL}')
