# objects

class phone:
    def __init__(self,brand,model,price,ram,storage):
        self.brand=brand
        self.model=model
        self.price=price
        self.ram=ram
        self.storage=storage
ph=[]
n = int(input("How many objects u want: "))
for i in range(n):
    b=input("Enter the brand: ")
    m=input("Enter the model: ")
    p=float(input(f"Enter the price: "))
    r=input("Enter the RAM: ")
    s=input("Enter the storage: ")
    ph.append(phone(b,m,p,r,s))
    print("\n")
for i in ph:
    print(f"""
Brand : {i.brand}
Model : {i.model}
Price : {i.price}
RAM : {i.ram}
Storage : {i.storage}""")