empty = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
a = []
def display():
    print(f"{empty[0]}|{empty[1]}|{empty[2]}")
    print(f"{empty[3]}|{empty[4]}|{empty[5]}")
    print(f"{empty[6]}|{empty[7]}|{empty[8]}")

display()
def displayforuser():
    empty=[1,2,3,4,5,6,7,8,9]
    print(f"{empty[0]}|{empty[1]}|{empty[2]}")
    print(f"{empty[3]}|{empty[4]}|{empty[5]}")
    print(f"{empty[6]}|{empty[7]}|{empty[8]}")
def start():
    while True:
        print("Below numbers are position.")
        displayforuser()
        playerx = (input("player x,Select position."))
        playery = (input("player o,Select position."))
        playerx=int(playerx)-1
        playery=int(playery)-1
        if playerx>=9 or playery>=9:
            print("invalid input")
        elif playerx<=9 or playery<=9:
            if empty[playerx]=="x":
                print("already taken")
                pass
            elif empty[playery]=="o":
                print("already taken")
                pass
            elif empty[playerx]=="o":
                print("already taken")
                pass
            elif empty[playery]=="x":
                print("already taken")
                pass
            else:
                empty[playerx] = "x"
                empty[playery]="o"
                playerx+=1
                playery+=1
                a.append(playerx)
                a.append(playery)
                display()
                if empty[0]=="x"and empty[1]=="x" and empty[2] == "x":
                    print("Player x won!")
                    break
                elif empty[0]=="o"and empty[1]=="o" and empty[2] == "o":
                    print("Player o won!")
                    break
                elif empty[0]=="x"and empty[3]=="x" and empty[6] == "x":
                    print("Player x won!")
                    break
                elif empty[0]=="o"and empty[3]=="o" and empty[6] == "o":
                    print("Player o won!")
                    break
                elif empty[1]=="x"and empty[4]=="x" and empty[7] == "x":
                    print("Player x won!")
                    break
                elif empty[1]=="o"and empty[4]=="o" and empty[7] == "o":
                    print("Player o won!")
                    break
                elif empty[2]=="x"and empty[5]=="x" and empty[8] == "x":
                    print("Player x won!")
                    break
                elif empty[2]=="o"and empty[5]=="o" and empty[8] == "o":
                    print("Player o won!")
                    break
                elif empty[3]=="x"and empty[4]=="x" and empty[5] == "x":
                    print("Player x won!")
                    break
                elif empty[3]=="o"and empty[4]=="o" and empty[5] == "o":
                    print("Player o won!")
                    break
                elif empty[6]=="o"and empty[7]=="o" and empty[8] == "o":
                    print("Player o won!")
                    break
                elif empty[6]=="x"and empty[7]=="x" and empty[8] == "x":
                    print("Player x won!")
                    break
                elif empty[0] == "o" and empty[4] == "o" and empty[8] == "o":
                    print("Player o won!")
                    break
                elif empty[0]=="x"and empty[4]=="x" and empty[8] == "x":
                    print("Player x won!")
                    break
                elif empty[2]=="o"and empty[4]=="o" and empty[6] == "o":
                    print("Player o won!")
                    break
                elif empty[2]=="x"and empty[4]=="x" and empty[6] == "x":
                    print("Player x won!")
                    break
                elif empty[0] == "x" and empty[1] == "x" and empty[2] == "x" and empty[6]=="o"and empty[7]=="o" and empty[8] == "o":
                    print("Game tie")
                    break
                elif empty[0] == "o" and empty[1] == "o" and empty[2] == "o" and empty[6]=="x"and empty[7]=="x" and empty[8] == "x":
                    print("Game tie")
                    break
                elif empty[0] == "x" and empty[3] == "x" and empty[6] == "x" and empty[2]=="o"and empty[5]=="o" and empty[8] == "o":
                    print("Game tie")
                    break
                elif empty[0] == "o" and empty[3] == "o" and empty[6] == "o" and empty[2]=="x"and empty[5]=="x" and empty[8] == "x":
                    print("Game tie")
                    break
            # print(a) ...... kindly don't uncomment this line because this line was created to test code whether it is properly working or not.
start()