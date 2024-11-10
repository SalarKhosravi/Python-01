import random, time, os

try:
    file = open("projects/scores.txt", "w")
    file.seek(0)      # Move cursor to the beginning
    file.truncate(0)  # Clear content from the beginning
    print('clear old data')
except FileExistsError as e:
    print(f"Error: {e}")
finally:
    file.close()

li = [ "paper", "rock", "scissors" ]

Pc_win = 0
H_win = 0
iterate = 0
while True:
    iterate += 1
    Pc_choice = random.choice(li)
    text = input("choose one : ")
    if(text == "end"):
        break
    else:
        if text[0] == "p" :
            h_choice = "paper"
        elif text[0] == "r":
            h_choice = "rock"
        elif text[0] == "s":
            h_choice = "scissors"
        else:
            print("input is not valid.")
            continue
    
    if Pc_choice == h_choice:
        print("same, try again")
        continue
    else:
        if(Pc_choice == "paper"):
            if(h_choice == "scissors"):
                H_win += 1
                print("you win")
            else:
                Pc_win += 1
                print("Oops, you lose")
        elif(Pc_choice == 'rock'):
            if(h_choice == "paper"):
                H_win += 1
                print("you win")
            else:
                Pc_win += 1
                print("Oops, you lose")
        else:
            if(h_choice == "rock"):
                H_win += 1
                print("you win")
            else:
                Pc_win += 1
                print("Oops, you lose")
    
    # store data in file
    # ----------------------------------------------------------
    try:
        file = open("projects/scores.txt", "a")
        file.write(f"{iterate}- {Pc_choice} vs {h_choice}: ")
        print('write 1 successfully')
        file.write(f"you won {H_win} and computer won {Pc_win} \n")
        print('write 2 successfully')
    except FileExistsError as e:
        print(f"Error: {e}")
    finally:
        file.close()
        
    # print(f"{Pc_choice} vs {h_choice}")
    # print(f"you won {H_win} and computer won {Pc_win}")

