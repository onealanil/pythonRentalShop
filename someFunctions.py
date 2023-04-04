from datetime import datetime
from colorama import Fore, Style, Back
import sys
import time

# loading function


def loading():
    string = 'Loading....>'
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.25)
    sys.stdout.write(f'{Fore.GREEN} 100% {Style.RESET_ALL}')


# welcome message
def welcome():
    print()
    print(f'{Fore.CYAN} ----------------------------> Welcome to the Python Rental Shop <------------------------------ {Style.RESET_ALL}')

# reading the file and inserting them in dictionary


def costumeCollection():
    dict = {}
    id = 1
    with open('./data/data.txt', 'r') as f:
        for line in f:
            dict[id] = line.replace("\n", "").split(",")
            id = id+1
    return dict

# what you want to do?


def options():
    print(f'{Fore.RED} What do you want to do? {Style.RESET_ALL}', end='')
    print(Fore.LIGHTGREEN_EX)
    print(""" 
        ::::::::::::< Options >::::::::::::::::

              Type d or D for display
              Type r or R for rent
              Type c or C for return
              Type e or E for Exit
    """)
    print(Style.RESET_ALL)


# header of display
def headerOfDisplay():
    print()
    print(f'{Fore.CYAN}------------------------> List of Available costume and details <--------------------------{Style.RESET_ALL}')
    print()

# check id and quantity


def checkIdAndQuantity():
    dict = costumeCollection()
    id = checkIdForRent()
    quantity = 0
    while True:
        try:
            qInput = int(input("Enter the quantity of the costume: \n-> "))
            if qInput <= int(dict[id][3]) and qInput > 0:
                quantity = qInput
                break
            else:
                print(
                    f'{Back.RED}{Fore.YELLOW} Quantity is out of range {Style.RESET_ALL}')
                continue
        except:
            print(f'{Back.RED}{Fore.YELLOW} Quantity is invalid {Style.RESET_ALL}')
            continue

    return id, quantity

# for secret details of rent


def detailsOfRent(name, quantity, secretKey, costume, tp):
    with open("allRentSecretDetails.txt", 'a') as details:
        details.write(name+"s, "+str(quantity)+", " +
                      secretKey+", "+costume+", "+str(tp)+"\n")
    details.close()


def returnDateTime(daysArr):
    message = ""
    if len(daysArr) == 1:
        message = "today"
    else:
        if int(daysArr[0]) > 0:
            if int(daysArr[0]) < 6:
                message = "noFine"
            else:
                message = "fine"
        else:
            print(f'{Back.RED}{Fore.YELLOW}You choose wrong date{Style.RESET_ALL}')

    return message


def costumeNameReturn(costume):
    index = ""
    newArr = []
    with open("./data/data.txt", 'r') as file:
        data = file.read().splitlines()
        for i in range(len(data)):
            newArr = newArr + [data[i].split(", ")]
        data = file.readlines()
    file.close()

    for i in newArr:
        if costume in i:
            index = newArr.index(i)
    return index

# checking the id is valid


def checkIdForRent():
    dict = costumeCollection()
    id = 0
    while True:
        try:
            idInput = int(input("Enter the id of the costume: \n-> "))
            if idInput <= int(len(dict)) and idInput > 0:
                id = idInput
                break
            else:
                print(
                    f'{Back.RED}{Fore.YELLOW} Id is out of range {Style.RESET_ALL}')
                continue
        except:
            print(f'{Back.RED}{Fore.YELLOW} Id is invalid{Style.RESET_ALL}')
            continue

    return id

# checking the name


def checkNameForRent():
    name = ""
    while True:
        nameInput = input("Enter your name: \n-> ")
        if nameInput.isalpha():
            name = nameInput
            break
        else:
            print(
                f'{Back.RED}{Fore.YELLOW}Name must be String{Style.RESET_ALL}')
            continue

    return name

# checking the address


def checkAddressForRent():
    address = ""
    while True:
        addressInput = input("Enter your address: \n-> ")
        if addressInput.isalpha():
            address = addressInput
            break
        else:
            print(
                f'{Back.RED}{Fore.YELLOW}Address must be String{Style.RESET_ALL}')
            continue

    return address
