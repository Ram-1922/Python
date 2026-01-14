# ATM Daily Limit System

# Allow only 3 withdrawals per day
# Each withdrawal ≤ ₹20,000
# Track total withdrawn amount
# Block account if daily limit exceeds ₹50,000

Avl_balance = 100000.00
limit = 0
daily_limit = 0
while limit < 3:
    print("1.Check Balance\n2.Withdraw\n3.Exit")
    choice = int(input("Enter Your Choice: "))
    match choice:
        case 1:
            print(f"Available Balance is rs.{Avl_balance:.2f}/-")
        case 2:
            w_amount = float(input("Withdrawal Amount: "))
            if w_amount > Avl_balance:
                 print("Insufficient Balance...")
            elif w_amount > 20000:
                print("Withdrawal must be less than or equal to 20000")
            elif daily_limit+w_amount > 50000:
                    print("Your transaction is blocked today...")
            else:
                limit+=1
                Avl_balance -= w_amount
                print(f"Rs.{w_amount:.2f} is withdrawed successfully...")
                daily_limit+=w_amount
                print(f"Total Amount withdrawed rs.{daily_limit:.2f}/-")
        case 3:
            break
    if limit == 3:
         print("Today's transaction count is reached...\nTry again Tommorrow...")