# Here is the practise page where i learnt python.
# Uncommand and run for outputs

#latest conditional statements

# sum = 0
# marks = []
# for i in range(0,6):
#     mark= int(input(f"Enter the mark {i}: "))
#     marks.append(mark)
#     sum += mark
# avg = sum/5
# result = "PASS" if avg > 60 else "FAIL" 
# for i in range(0,6):
#     print(f"Mark of Subject {i}: {marks[i]}")
# print(f"You have {result}ED in the Exam...")

# a=6
# b=7
# print(a if a>b else b)

#card
# card_number='1234-5678-9012-6789'
# print("xxxx-xxxx-xxxx-"+card_number[-4:])
# Time
# import time
# n=int(input("Enter a Number:"))
# for i in range(n,0,-1):
#     seconds = i%60
#     minutes = int(i/60)%60
#     hours = int(i/3600)%24
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("All done...")

# nested loops
# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()
# rows=int(input("Enter no of rows:"))
# column=int(input("Enter no columns:"))
# symbol=input("Enter the item:")
# for i in range(rows):
#     for j in range(column):
#         print(symbol, end=' ')
#     print()

# Lists

# bike=["BMW","Kawazuki","Harley Davidson"]
# cars=["BMW","Mercedes benz","Range Rover","Pagani","Rolls Royce"]
# cars.append("Lamborghini")
# print(cars)
# print(cars.index("Pagani"))
# cars.remove("Lamborghini")
# print(cars)
# cars.insert(3,"Audi")
# print(cars)
# cars.extend(bike)
# print(cars)
# # cars.append(bike)
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# print(len(cars))

# set

# bike={'Honda','Suzuki','Hero Honda','Yamaga','KTM','Kawazuki'}
# bike.add("BMW")
# bike.remove("KTM")
# print(bike)

#Tuple

# cars=("BMW","Mercedes benz","Range Rover","Pagani","Rolls Royce,BMW")
# print(cars.index('Pagani'))
# print(cars.count("BMW"))

#Shopping Cart Program

# products=[]
# prices=[]
# total=0
# while True:
#     product= input("Enter the Product you want to buy (Enter q to quit):")
#     if product.lower() == "q":
#         break
#     else:
#         price=float(input(f"Enter the Price of the {product}: Rs."))
#         products.append(product)
#         prices.append(price)
# print("---------Shopping Cart---------")
# for i in range(0,len(products)):
#     print(f"{products[i]:>10} - {prices[i]:<10.2f}")
# for i in prices:
#     total+=i
# print(f"The Total price is Rs.{total:.2f}")

#2d lists

# phones = ['Vivo','Oppo','Iphone','Oneplus','Redmi','Poco']
# laptops = ['Lenevo','Dell','Apple','HP','Asus','Acer']
# earphones = ['Airpods','Boult','Jbl','Realme','Boat']
# products = [phones,laptops,earphones]

# for product in products:
#     for i in product:
#         print(f"{i:^10}")
#     print("---------------------------------------------------------------")

# Creating a numpad using 2d lists

# num_pad = ((7, 8, 9),
#            (4, 5, 6),
#            (1, 2, 3),
#            (0, '    .','  Enter'))
# for num in num_pad:
#     for i in num:
#         print(f'{i:5}',end=" ")
#     print()

# Dictionary

# student = {"Robert":"01",
#            "Joseph":"02",
#            "David":"03",
#            "William":"04",
#            "Daniel":"05"
# }
# print(student)
# print(student.get("Joseph"))
# student.update({"Hendry":"06"})
# student.update({"William":"003"})
# for key in student.keys():
#     print(key)
# for value in student.values():
#     print(value)
# for key,value in student.items():
#     print(f"The {key} => {value}")
# student.pop("David")
# student.popitem()
# student.clear()
# print(student)

#Random
# import random as rdm
# number = rdm.randint(1,10)
# guess=int(input("Guess the Number (1 - 10) : "))
# if guess == number:
#     print(f"You are Right {guess} is the correct 👍")
# else:
# #     print(f"You are Wrong! 😔 The number is {number}")
# cards=['A','K','Q','J','10','9','8','7','6','5','4','3','2']
# print(rdm.choice(cards))

# Functions

# def hbd(name , num, cake_flavor):
#     print(f"Happy Birthday {name} 🥳")
#     print(f"Today is your {num} birthday.")
#     print(f"And here yours fav {cake_flavor} Cake 🎂")
# name_of_person = input("Enter the birthday guy name : ")
# age = int(input("Enter the age : "))
# cake = input("Enter the cake flavor : ")
# hbd(name_of_person, age, cake)
# def add(a=0,b=0,c=0,d=0,e=0,f=0):
#     return a+b+c+d+e+f
# print(add(8,6,5,2,1))
# def greet(name,year,degree,clg):
#     print(f"Hello {name} \n    You have completed your {degree} degree in the year ({year-1}-{year-2000}) from {clg}.")
# greet("Spideyy",2025,clg="Coimbatore Institute of Engineering and Technology",degree="B.E CSE")

# *args

# def add(*sums):
#     sum=0
#     for i in sums:
#         sum +=i
#     return sum
# print(add(1,5,8,2,4))
# def display(*names):
#     for name in names:
#         print(name,end=",\n")
# display("Spidey","Undertaker","Tony Stark","Tom Holland")

# **kwargs

# def address(**adss):
#     for i,j in adss.items():
#         print(f"{i}-{j}")
# address(city="cbe",street="Thangavel st")
# def student_details(*args,**kwargs):
#     for i in args:
#         print(i)
#     print("Address:-")
#     for key,value in kwargs.items():
#         print(f"{key:5} : {value}")
# name = input("Enter Student Name: ")
# dob = input("Enter DOB (dd/mm/yyyy): ")
# father  = input("Enter your Father\'s Name: ")
# mother = input("Enter your Mother\'s Name: ")
# print("---------------Address Details-------------")
# doorno = input("Door no: ")
# st = input("Street: ")
# ar = input("Area: ")
# cty = input("City: ")
# pin = int(input("Pincode: "))
# print("-------------------------------------------")
# student_details(name,dob,father,mother,door_number=doorno,street=st,area=ar,city=cty,pincode=pin)

# membership operator

# email = input("Enter Your Mail id : ")
# while True:
#     if ('@' and '.') not in email or len(email)<8:
#         print("You\'ve entered a invalid email ! ")
#         email = input("Enter Your Mail id : ")
#     else:
#         break
# print(email)

# List Comprehension

# num = (i**2 for i in range(1,50))
# print(set(i for i in num))
# n=int(input("Enter the number of Students: "))
# students = [input(f"Enter Student{i} Name: ").capitalize() for i in range(1,n+1)]
# print(*(f"{i:<10}\n" for i in students))

# modules

# import module
# print(module.num)
# print(*(f"{i}" for i in module.num1))

# objects

# class phone:
#     def __init__(self,brand,model,price,ram,storage):
#         self.brand=brand
#         self.model=model
#         self.price=price
#         self.ram=ram
#         self.storage=storage
# ph=[]
# n = int(input("How many objects u want: "))
# for i in range(n):
#     b=input("Enter the brand: ")
#     m=input("Enter the model: ")
#     p=float(input(f"Enter the price: "))
#     r=input("Enter the RAM: ")
#     s=input("Enter the storage: ")
#     ph.append(phone(b,m,p,r,s))
#     print("\n")
# for i in ph:
#     print(f"""
# Brand : {i.brand}
# Model : {i.model}
# Price : {i.price}
# RAM : {i.ram}
# Storage : {i.storage}""")
# class student:
#     class_year=2025
#     num_of_students=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         student.num_of_students+=1
# student1=student("Ram",19)
# student2=student("Pran",19)
# student3=student("Vasa",20)
# student4=student("Mr.K",19)
# print(f"Name : {student1.name}\nAge : {student1.age}\nNum of Students : {student.num_of_students}")

# Inheritance

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         print(f"{self.name} eats food...")
#     def sleep(self):
#         print(f"{self.name} sleeps peacefully...")
# class dog(Animal):
#     def sound(self):
#         print(f"{self.name} barks...")
# class cat(dog):
#     def soun(self):
#         print(f"{self.name} meows...")
# a1=Animal("Liger")
# d1=dog("Karthi")
# c1=cat("Jimy")
# c1.eat()
# d1.sleep()
# a1.sleep()
# c1.soun()
# d1.sound()
# c1.sound()

# Super()

# class vehicle:
#     def __init__(self,brand,model,color):
#         self.brand=brand
#         self.model=model
#         self.color=color
#     def drive(self):
#         print(f"I have a {self.color} color {self.brand}-{self.model}.")
# class car(vehicle):
#     def __init__(self, brand, model, color,seater):
#         vehicle.__init__(self,brand, model, color)
#         self.seater=seater
#     def drive(self):
#         print(f"And its a {self.seater} seater car")
# class bike(vehicle):
#     def __init__(self, brand, model, color, mileage):
#         super().__init__(brand, model, color)
#         self.mileage=mileage
#     def drive(self):
#         super().drive()
#         print(f"And gives {self.mileage} mileage")
# v1 = vehicle("Volvo","Z60","Black")
# c1 = car("BMW","M5","White",4)
# b1 = bike("Royal Enfield","Classic 350","grey",32)
# c1.drive()

# polmorphism

# from abc import ABC,abstractmethod
# class shape:
#     @abstractmethod
#     def area(self):
#         pass
# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2
# class square:
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side**4
# shapes = [circle(6),square(4)]
# for i in shapes:
#     print(i.area())

# Duck Typing

# class animal:
#     isalive = True
# class dog(animal):
#     def speak(self):
#         print("Barks")
# class cat(animal):
#     def speak(self):
#         print("Meows")
# class car(animal):
#     isalive=False
#     def speak(self):
#         print("Honks")
# all = [dog(),cat(),car()]
# for i in all:
#     i.speak()
#     print(i.isalive)

#Static method

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f"My Name {self.name} and i\'m {self.age}") 
#     @staticmethod
#     def disp(std):
#         print(f"I\'m Studying {std}")
# s1=student("hari",18)
# s1.display()
# s1.disp(5)
# student.disp(6)

# class method

# class student:
#     count = 0
#     total_gpa=0
#     def __init__(self,name,gpa):
#         self.name=name
#         self.gpa=gpa
#         student.count+=1
#         student.total_gpa+=gpa
#     def get_info(self):
#         return f"My name is {self.name}, and my gpa is {self.gpa}."
#     @classmethod
#     def student_count(cls):
#         return f"Student count: {cls.count}\nTotal GPA: {cls.total_gpa}\nAVG GPA: {cls.total_gpa/cls.count}"
# s1=student("harry",5.23)
# s2=student("David",5.62)
# s3=student("joseva",8.02)
# ss=[s1,s2,s3]
# for i in ss:
#     print(i.get_info())
# print(student.student_count())

# Magic methods

# class laptop:
#     def __init__(self,brand,model,price,ram):
#         self.brand=brand
#         self.model=model
#         self.price=price
#         self.ram=ram
#     def __str__(self):
#         return f"""
# Brand: {self.brand}
# Model: {self.model}
# Price: {self.price}
# RAM: {self.ram}"""
#     def __eq__(self, value):
#         return self.brand==value.brand and self.model==value.model and self.ram==value.ram
#     def __lt__(self,other):
#         return self.price < other.price 
#     def __gt__(self,other):
#         return self.price > other.price
#     def __add__(self,other):
#         return self.price + other.price 
#     def __contains__(self,keyword):
#          return keyword in self.brand or keyword in self.model
#     def __getitem__(self,key):
#         if key.lower() == "brand":
#             return self.brand
#         elif key.lower() == "model":
#             return self.model
#         elif key.lower() == "price":
#             return self.price
#         elif key.lower() == "ram":
#             return self.ram
#         else:
#             return "Invalid"      
# l1=laptop("Lenovo","LOQ",78999,"24gb")
# l2=laptop("Dell","Inspiron15",54999,"16gb")
# l3=laptop("Lenovo","LOQ",69999,"24gb")
# print(l1,"\n",l2)
# print(l1==l3)
# print(l1<l2)
# print(l1>l2)
# print(l1+l2)
# print("Lenovo" in l3)
# print(l1["brand"])
# print(l2["price"])
# print(l3["ram"])
# print(l2["sdd"])

# Property

# class house:
#     def __init__(self,bhk,price):
#         self._bhk=bhk
#         self._price=price
#     @property
#     def bhk(self):
#         return f"{self._bhk} BHK House."
#     @property
#     def price(self):
#         return f"Rs.{self._price}/-"
#     @bhk.setter
#     def bhk(self,new_bhk):
#         if new_bhk>0:
#             self._bhk=new_bhk
#         else:
#             print("BHK must be greater than zero.")
#     @price.setter
#     def price(self,new_price):
#         if new_price>0:
#             self._price=new_price
#         else:
#             print("Price must be greater than zero.")
#     @bhk.deleter
#     def bhk(self):
#         del self._bhk
#         print("bhk deleted")
#     @price.deleter
#     def price(self):
#         del self._price
#         print("price deleted")
# h1 = house(3,100000)
# h1.bhk=0
# h1.price=-5
# print(h1.bhk)
# print(h1.price)
# del h1.bhk
# del h1.price

# Decorator

# def mayonnaise(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         print("With Mayonnaise")
#     return wrapper
# def mustard(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         print("With Mustard")
#     return wrapper
# def ketchup(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         print("With ketchup")
#     return wrapper
# @mayonnaise
# @ketchup
# def burger(meat):
#     print(f"Here is ur {meat} burger",end=" ")
# burger("chicken")

# Exception handling

# try:
#     a = int(input("Enter a Number: "))
#     print(1/a)
# except ZeroDivisionError:
#     print("1 can't be divided by zero.")
# except ValueError:
#     print("Invalid Value Entered.")
# except Exception as e:
#     print("Something went wrong. it might be",e)
# else:
#     print("Calculation Successful.")
# finally:
#     print("bye")

# File Detection

# import os
# file_path = "calculator.py"
# if os.path.exists(file_path):
#     print(f"{file_path} exists")
#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a Directory")
# else:
#     print(f"{file_path} does not exists")

# file operations

# file_path = "New.txt"
# with open(file_path, "a")as file:
#     file.write("\n"+"Hello, This is a new file")
# with open(file_path, "r") as file:
#     print(file.read())

#json

# import json
# file_path = "input.json"
# with open(file_path,'w')as file:
#     content=json.dump({"Name":"Sri","Age":25},file)
# with open(file_path,'r') as file:
#     content = json.load(file)
#     print(content)

# csv

# import csv
# employees = [["Name","Age","Location"],["Sri",19,"Coimbatore"]]
# file_path = "input.csv"
# with open(file_path,'w')as file:
#     content=csv.writer(file)
#     for i in employees:
#         content.writerow(i)
# with open(file_path,'r')as file:
#     content = csv.reader(file)
#     for i in content:
#         print(i)

# Datetime

# import datetime
# date = datetime.date(2006,6,19)
# print(date)
# today=datetime.date.today()
# print(today)
# time = datetime.time(5,23,58)
# current_time = datetime.datetime.now()
# current_time=current_time.strftime("%H : %M : %S")
# print(current_time)
# target = datetime.datetime(2028,12,5,10,56,23)
# now= datetime.datetime.now()
# if target < now:
#     print("The target date is passed.")
# else:
#     print("The target date is not passed.")
#     n_date=target-now
#     print(n_date)


# Threading

# import threading
# import time
# def drive(brand,model):
#     time.sleep(5)
#     print(f"I\'m Driving a {brand} {model}")
# def vibe(song):
#     time.sleep(2)
#     print(f"I\'m Vibing with the {song} songs")
# def eat():
#     time.sleep(3)
#     print("I had a tasty snacks")
# T1 = threading.Thread(target=drive,args=("BMW","M5"))
# T2 = threading.Thread(target=vibe,args=("Melody",))
# T3 = threading.Thread(target=eat)
# T1.start()
# T2.start()
# T3.start()

# API Requests

# import requests
# def display_pokemon(name):
#     url = f"https://pokeapi.co/api/v2/pokemon/{name}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
# pokemon_name = input("Enter Pokemon Name: ")
# poke_info=display_pokemon(pokemon_name)

# print(f"Name: {poke_info["name"]}\nHeight: {poke_info["height"]}\nWeight: {poke_info["weight"]}")
