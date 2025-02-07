import random, datetime
now = datetime.datetime.now()
wincard = {'p': 's','s': 'r','r': 'p'}

pc_win = 0
h_win = 0
round_count = 0

# write the header of log
with open ('log.txt', 'a') as f:
    f.write(f'\nStart New Game ({now})')
    f.write('\nResult as user to pc')
    f.write('\n------------------------------------------')

while True:
    pc_choice = random. choice(list(wincard.keys()))
    h_choice = input( 'select one: ')

    if h_choice == 'end':
        print( 'game is finished !')
        break
    elif h_choice not in wincard. keys():
        print( 'Your choice is not valid')
        log = f'! invalid ({h_choice})'
    elif h_choice == pc_choice:
        print( 'equal choice, try again !')
        log = f'? equal ({h_choice})'
    elif wincard[pc_choice] == h_choice:
        print('you win')
        h_win += 1
        log = f'+ win ({h_choice} | {pc_choice})'
    else:
        pc_win += 1
        print( 'you loss')
        log = f'- loss ({h_choice} | {pc_choice})'

    with open( 'log.txt', 'a') as f:
        round_count += 1
        f.write(f'\nround {round_count if round_count > 9 else ('0'+str(round_count))}: {log}')
    

# write the final footer of log
with open ('log.txt', 'a') as f:
    f.write('\n------------------------------------------')
    f.write(f'\nFinal result in {round_count} rounds: user {h_win}, pc {pc_win}\n\n\n')