# Separating odd and even
a= int(input("Enter the End num: "))
num=[i for i in range(1,a+1)]
odd=[x for x in num if x%2!=0]
even=[x for x in num if x%2==0]
print(f"Odd ->",*(odd))
print(f"Even ->",*(even))