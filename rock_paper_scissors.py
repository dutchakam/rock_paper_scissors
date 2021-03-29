import random
import time

print('Welcome to Rock, Paper, Scissors!!\n')
time.sleep(1)
print('Make your choice!!\n')
time.sleep(1)

plays = ['Rock', 'Paper', 'Scissors']

player_score = 0
pc_score = 0
total_games = 0

while total_games < 9:
    pc_play = random.choice(plays)
    play = input('Rock, Paper, Scissors or Quit: ')
    time.sleep(1)
    
    if play == pc_play:
        print(f'Draw! {play}\n')
    elif play == 'Rock':
        if pc_play == 'Paper':
            print(f'PC Wins! Paper beats Rock\n')
            pc_score += 1
            total_games += 1
        else:
            print('Player Wins! Rock beats Scissors\n')
            player_score += 1
            total_games += 1
    elif play == 'Paper':
        if pc_play == 'Scissors':
            print('PC Wins! Scissors beats Paper\n')
            pc_score += 1
            total_games += 1
        else:
            print('Player Wins! Paper beats Rock\n')
            player_score += 1
            total_games += 1
    elif play == 'Scissors':
        if pc_play == 'Rock':
            print('PC Wins! Rock beats Scissors\n')
            pc_score += 1
            total_games += 1
        else:
            print('Player Wins! Scissors beats Paper\n')
            player_score += 1
            total_games += 1
    elif play == 'Quit':
        print('You Quit\n')
        break
    else:
        print('Invalid Play\n')
        pass

    print(f'Player Score: {player_score}, PC Score: {pc_score}\n')
    time.sleep(1)

print(f'Final Score --> Player: {player_score}, PC: {pc_score}\n')
time.sleep(1)

if player_score > pc_score:
    print('Player wins the game!!!')
else:
    print('PC wins the game!!!')
