import random

li = [ "paper", "rock", "scissors" ]

Pc_win = 0
H_win = 0

while True:
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
    
    print(f"{Pc_choice} vs {h_choice}")
    print(f"you won {H_win} and computer won {Pc_win}")



# end
# you can make it better by removing extra if conditions