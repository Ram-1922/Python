# banking program

def check_balance(avl_balance):
    return avl_balance
def withdraw(avl_balance,amount):
    if amount <= 0:
        print("Amount must be greater than 0 for withdrawal...")
        return 0
    elif amount > avl_balance:
        print("Insuffient Balance!!!\nCheck Balance and retry...")
        return 0
    elif amount > 50000:
        print("You entered a exceeding limit\nTry with small amounts...")
        return 0
    else:
        print(f"Your Amount rs.{amount:.2f} is Successfully Withdrawed...")
        return amount
def deposit(amount):
    if amount <= 0:
        print("Amount must be greater than 0 for deposit...")
        return 0
    elif amount > 50000:
        print("You entered a exceeding limit\nTry with small amounts...")
        return 0
    else:
        print(f"Your Amount rs.{amount:.2f} is Successfully Deposited...")
        return amount
def exit():
    return False
def main():
    balance = 100
    is_running=True
    while is_running:
        print("--------------------------------------------------------------------------------------")
        print("1.Check Balance \n2.Deposit \n3.Withdraw \n4.Exit")
        print("--------------------------------------------------------------------------------------")
        choice = int(input("Enter Choice: "))
        match choice:
            case 1:
                print(check_balance(f"Available Balance in your account = {balance:.2f}"))
            case 2:
                deposit_amount = float(input("Enter amount u want to Deposit: "))
                valid_deposit_amount = deposit(deposit_amount)
                balance += valid_deposit_amount
            case 3:
                withdraw_amount = float(input("Enter amount u want Withdraw: "))
                valid_withdraw_amount = withdraw(balance,withdraw_amount)
                balance -= valid_withdraw_amount
            case 4:
                print("Exits...")
                is_running=exit()
            case _:
                print("Invalid Choice...")
if __name__ == "__main__":
    main()
