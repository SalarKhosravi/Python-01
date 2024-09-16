import random

li = ["paper", "rock", "scissors"]
Pc_win, H_win = 0, 0
winning_choices = {"paper": "scissors", "rock": "paper", "scissors": "rock"}

while True:
    Pc_choice = random.choice(li)
    text = input("choose one (p for paper, r for rock, s for scissors) or 'end' to quit: ")

    if text == "end":
        break
    
    h_choice = {"p": "paper", "r": "rock", "s": "scissors"}.get(text[0])
    if not h_choice:
        print("input is not valid.")
        continue

    if Pc_choice == h_choice:
        print("same, try again")
        continue

    if h_choice == winning_choices[Pc_choice]:
        H_win += 1
        print("you win")
    else:
        Pc_win += 1
        print("Oops, you lose")
    
    print(f"{Pc_choice} vs {h_choice}")
    print(f"you won {H_win} and computer won {Pc_win}")
