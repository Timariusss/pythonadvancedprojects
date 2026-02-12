import random 

def play_game():
    money = 100 
    print('welcome to the casino!')
    print('now you have $100')
    print('your goal is to reach 1000 dollars')
    print('you can play 3 games: dice, coin flip, and card draw')
    print('if you will lose all your money, you will be kicked out of the casino')
    print('good luck!')
    
    while money > 0 and money < 1000:
        print(f'\nyou have ${money}')
        print('you can choose a game to play: 1-dice, 2-coin flip, 3-card draw')
        game = int(input('enter the number of the game you want to play: '))
        
        if game == 1:
            print('you chose dice')
            print('you will guess the number on the dice, if you guess right, you will win 100 dollars, if you guess wrong, you will lose 20 dollars')
            dice = random.randint(1, 6)
            guess = int(input('guess the number on the dice (1-6): '))
            if guess == dice:
                print('you guessed! you won 100 dollars')
                money += 100
            else:
                print('you guessed wrong! you lost 20 dollars')
                money -= 20
        
        elif game == 2:
            print('you chose coin flip')
            print('you will guess the coin side, if you guess right, you will win 50 dollars, if you guess wrong, you will lose also 50 dollars')
            coin = random.choice(['heads', 'tails'])
            guess = str(input('guess the coin side (heads/tails): '))
            if guess == coin:
                print('you guessed! you won 50 dollars')
                money += 50
            else:
                print('you guessed wrong! you lost 50 dollars')
                money -= 50
        
        elif game == 3:
            print('you chose card draw')
            print('you will guess the card suit, if you guess right, you will win 500 dollars, if you guess wrong, you will lose 200 dollars')
            card = random.choice(['hearts', 'diamonds', 'clubs', 'spades'])
            guess = str(input('guess the card suit (hearts/diamonds/clubs/spades): '))
            if guess == card:
                print('you guessed! you won 500 dollars')
                money += 500
            else:
                print('you guessed wrong! you lost 200 dollars')
                money -= 200
    
    print(f'\nGame Over! You have ${money}')
    if money <= 0:
        print('you lost all your money! you are kicked out of the casino')
    elif money >= 1000:
        print('congratulations! you reached 1000 dollars! you won the game!')

if __name__ == '__main__':
    play_game()


