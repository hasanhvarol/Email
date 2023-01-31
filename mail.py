import email
import random
import string
import time
import os
import colorama
from colorama import Fore, Back, Style
output = []
randomLeghnt = 5

def randomgen(leght):
    harfeler = string.ascii_lowercase
    yazi = ''.join(random.choice(harfeler) for i in range(leght)) 
    return yazi

def uret(exportAmount, Email):
    for i in range(exportAmount):
        randomlar = randomgen(5)
        Email = Email.replace("@gmail.com", "")
        final = "{}+{}@gmail.com".format(Email, randomlar)
        output.append(final)
    print(Fore.RED, "    ")
    time.sleep(2)
    print(output)
    print("  ")
    os.system('exit')



def menu():
    os.system('clear||cls')
    time.sleep(1)
    print(Fore.RED, "         _                           _                         _ ")
    print(Fore.BLUE, "        | |__   __ _ ___  __ _ _ __ | |____   ____ _ _ __ ___ | |")
    print(Fore.RED, "        | '_ \ / _` / __|/ _` | '_ \| '_ \ \ / / _` | '__/ _ \| |")
    print(Fore.BLUE, "        | | | | (_| \__ \ (_| | | | | | | \ V / (_| | | | (_) | |")
    print(Fore.RED, "        |_| |_|\__,_|___/\__,_|_| |_|_| |_|\_/ \__,_|_|  \___/|_|")
    print("     ")
    time.sleep(0.5)
    print(Fore.BLUE + Style.DIM + "                                                     @hasanhvarol")
    # print("[1] Gmail Üretici")
    time.sleep(1)
    soru = input("'1' Gmail Üretici \n'2' Çıkış\nGirin: ")
    if soru == "1":
        os.system('clear||cls')
        email
        sayi = int(input("Kaç tane mail oluşturmak istersiniz: "))
        print("    ")
        emailg = input("Email Adresini Yaz: ")
        uret(sayi, emailg)
    elif soru == "2":
        os.system('exit')
    

menu()