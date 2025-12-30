# matchcase 

day = int(input("Enter a Number : "))
while day not in [i for i in range(1,8)]:
    day = int(input("Enter a Number :"))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")