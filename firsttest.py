import random


def choices():
    player_choice = input("rock, paper or scissors?")
    computer_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_options)
    answers = { 'player' : player_choice, 'computer' : computer_choice }
    return answers


def who_wins(player, computer):
    print(f'you chose {player}, computer chose {computer}')
    if player == computer:
        return 'imagine tying with a bot, could never be me tho'
    elif player == 'paper' and computer == 'rock':
        return 'kind of a bitch`s play but a win is a win'
    elif player == 'scissors' and computer == 'paper':
            return 'kinda clean keeping paper in check but lock in gang'
    elif player == 'rock' and computer == 'scissors':
            return 'The good old rock, never fais, manly AF'
    else :
         return 'lost to a bot, DAMN, may wanna go 0/1 IRL'

y = choices()

result = who_wins(y['player'], y['computer'])
print(result)