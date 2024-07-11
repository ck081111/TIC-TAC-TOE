
gameboard=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
endTheGame =False

def fullPrint():
    for row in gameboard:
        print(row)

#PLAYING THE GAME
print("WELCOME TO TIC-TAC-TOE")

while(endTheGame == False):
    fullPrint() #Printing Board
    userChoice = str(input("Where u wanna go (ex. 02): "))
    gameboard[int(userChoice[0])][int(userChoice[1])]="X"
    r

    #STUFF