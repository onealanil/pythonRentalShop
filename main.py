from colorama import Fore, Style, Back
import display
import rent
import someFunctions
import time
import returnC


def main():
    # for loading
    someFunctions.loading()
    # for welcome message
    someFunctions.welcome()
    while True:
        someFunctions.options()

        user = input("Enter your choice: \n-> ")
        if user.isalpha():
            if user == "d" or user == "D":
                print(f'{Fore.YELLOW}You choose to Display...{Style.RESET_ALL}')
                time.sleep(2)
                display.displayCostume()
            elif user == "r" or user == "R":
                print(f'{Fore.YELLOW}You choose to Rent...{Style.RESET_ALL}')
                time.sleep(2)
                rent.rentCostume()
            elif user == "c" or user == "C":
                print(f'{Fore.YELLOW}You choose to Return...{Style.RESET_ALL}')
                time.sleep(2)
                returnC.returnCostume()
            elif user == "e" or user == "E":
                print(f'{Fore.YELLOW}You choose to exit...{Style.RESET_ALL}')
                time.sleep(2)
                print(f'{Fore.YELLOW}Thank you! for choosing us, {Style.RESET_ALL}')
                break
            else:
                print(
                    f'{Back.RED}{Fore.YELLOW} Choose the correct options {Style.RESET_ALL}')
                continue

        else:
            print(f'{Back.RED}{Fore.YELLOW} Choice is invalid {Style.RESET_ALL}')


if __name__ == '__main__':
    main()
