from colorama import Fore,Style
import someFunctions
import time


def displayCostume():
    dict = someFunctions.costumeCollection()
    someFunctions.headerOfDisplay()

    # Print the names of the columns.
    print(Fore.YELLOW)
    print("{:<10} {:<36} {:<20} {:<15} {:<10}".format(
        'ID', 'ITEM', 'BRAND', 'PRICE', 'QUANTITY'))
    print(f'{Style.RESET_ALL}' , end= "")

    # print each data item.
    print(f'{Fore.GREEN}' , end="")
    for key, value in dict.items():
        item, brand, price, quantity = value
        print("{:<10} {:<35} {:<20} {:<15} {:<10}".format(
            key, item, brand, price, quantity))
    time.sleep(3)
    print(Style.RESET_ALL)
    print()
