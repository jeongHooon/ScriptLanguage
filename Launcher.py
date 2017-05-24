loopFlag = 1
from LoadAPI import *
def printMenu():
    print("========Menu==========")
    print("Load xml:  l")
    print("Print xml: p")
    print("========Menu==========")

def launcherFunction(menu):
    if menu ==  'l':
        LoadXMLFile()
    elif menu == 'p':
        PrintXML()
    else:
        print ("error : unknow menu key")


def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()


##### run #####
while (loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")