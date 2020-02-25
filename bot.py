#Imports
from pyautogui import typewrite, FAILSAFE, press
from random import randint
from time import sleep
#Declare for what we need
randbet = randint(200, 999)
FAILSAFE = False
##########################


class bots:
    def bot(delay):
        global randbet
        typewrite("&#1082;&#1072;&#1079;&#1080;&#1085;&#1086; " + str(randbet)+ "&#1082;&#1082;&#1082;", interval=delay)
        randbet = randint(135,700)
        press('enter')
    def GivenBetBot(delay):
        typewrite("&#1082;&#1072;&#1079;&#1080;&#1085;&#1086; " + str(playerbet)+ "&#1082;&#1082;&#1082;", interval=delay)
        press("enter")
    def getdev():
        print("wait...")
        sleep(10)
        print("wait...")
        sleep(5)
        print("vk.com/lalof2")
        input()


delay = input("Delay for every symbol written ")
if delay == "dev":
    getdev()


boton = input("Turn on bot? yes/no/count/givenbet/givencount ")

if boton == "yes":
    sleep(5)
    while True:
        bots.bot(delay)

elif boton == "dev":
    bots.getdev()

elif boton == "count":
    betscount = input("How many bets you want to place? ")
    sleep(5)
    for i in range(int(betscount)):
        bots.bot(delay)

elif boton == "givenbet":
    print("In this mode your bet will spam and not change or randomise")
    playerbet = input("Your bet: ")
    sleep(5)
    while True:
        bots.GivenBetBot(delay)

elif boton == "givencount":
    givenbetscount = input("How many bets you want to place? ")
    playerbet = input("Your bet: ")
    sleep(5)
    for i in range(int(givenbetscount)):
        bots.GivenBetBot(delay)

else:
    print("script completed")