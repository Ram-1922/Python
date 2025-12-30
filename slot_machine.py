# Slot Machine

import random

def bet_check(balance):
    bet = input("Enter the bet amount : ")
    if not bet.isdigit():
        print("It\'s not a valid bet...")
        return 0
    elif int(bet) > balance:
        print("Insufficient funds...")
        return 0
    else:
        return bet
def rowspin(symbols):
    spin = [random.choice(list(symbols)) for _ in range(3)]
    return spin
def printrow(spin):
    print("------------------")
    print(" |".join(spin))
    print("\n------------------")
def getpayout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0] == '🍒':
            return 1*bet
        elif row[0] == '🍉':
            return 2*bet
        elif row[0] == '🍋':
            return 3*bet
        elif row[0] == '🔔':
            return 4*bet
        elif row[0] == '⭐':
            return 5*bet
    elif (row[0] == row[1]) or (row[0] == row[2]) :
        if row[0] == '🍒':
            return 5+bet
        elif row[0] == '🍉':
            return 6+bet
        elif row[0] == '🍋':
            return 7+bet
        elif row[0] == '🔔':
            return 8+bet
        elif row[0] == '⭐':
            return 10+bet
    elif row[1] == row[2]:
        if row[1] == '🍒':
            return 5+bet
        elif row[1] == '🍉':
            return 6+bet
        elif row[1] == '🍋':
            return 7+bet
        elif row[1] == '🔔':
            return 8+bet
        elif row[1] == '⭐':
            return 10+bet
    return 0
    
def main():
    balance = int(input("Enter the Amount : "))
    print("Slot Machine 🎰")
    symbols = ['🍒','🍋','⭐','🔔','🍉']
    print(*(f"{i} " for i in symbols))
    while balance > 0:
        print(f"Current Balance : {balance}")
        bet = int(bet_check(balance))
        if bet <= 0:
            continue
        balance -= bet
        spin = rowspin(symbols)
        printrow(spin)
        payout = getpayout(spin,bet)
        balance += payout
        if payout>0:
            print(f"You Won rs.{payout} ")
        else:
            print("You lost the round...")
        play_again = input("Do you want to Play Again...(Yes/No) :").upper()
        if play_again == "NO":
            break
    if balance == 0:
        print("Game Over!")

if __name__ == '__main__':
    main()