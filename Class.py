import random
import os
import shutil
import csv
from abc import ABC, abstractmethod
import json
import pickle
import gzip

# test_csv=[
#     ['Имя',"Возраст","Город"],
#     ['Анна',"30","Москва"],
#     ['Петр',"34","Москва"]
# ]

# with open("test_data_csv",'w',encoding='utf-8',newline='') as file:
#     writer=csv.writer(file)
#     writer.writerows(test_csv)

# with open("test_data_csv",'r',encoding='utf-8') as file:
#     reader=csv.reader(file)
#     for row_num,row in enumerate(reader,1):
#         print(f'Строка {row_num}: {row}')
#         print(f'Строка {type(row)}')

# # with open("test_data_csv",'r',encoding='utf-8') as file:
# #     reader=csv.DictReader(file)
# #     for i in reader:

# import json

# test_json={
#     'Имя':"Анна",
#     'Возраст':"30",
#     'Город':"Москва"
# }

# with open('test_data_json','w',encoding='utf-8') as file:
#     json.dump(test_json,file,ensure_ascii=False,indent=2)

# class Book:
#     raiting=5

#     def __init__(self,name,author,raiting):
#         self.name=name
#         self.author=author
#         self.is_reading=False
#         self.raiting=raiting
# book=Book('Иван',"Иванов Иван",6)
# print(book.is_reading)

# book.is_reading=True
# book.name='Николай'
# print(book.name,book.is_reading)

# class Book:
#     def __init__(self,name,author,year):
#         self.name=name
#         self.author=author
#         self.year=year
    
#     def book_info(self):
#         print(f'Автор {self.name} Автор {self.author} Год {self.year}')


# book1=Book('Преступление и наказание','Достоевский',2007)
# book2=Book('Стихи','Пушкин',2000)
# book3=Book('Басни','Крылов',1873)

# book1.book_info
# book2.book_info
# book3.book_info

# class Student:
#     def __init__(self,name,surname,age):
#         self.name=name
#         self.surname=surname
#         self.age=age
    
#     def student_info(self):
#         print(f'Привет, я {self.name} {self.surname} мне {self.age} лет')

# student1=Student('Айназик','Байматова',18)
# student2=Student('Саммира','Рахимова',17)

# student1.student_info()
# student2.student_info()

# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * (self.radius ** 2)
#     def dlina(self):
#         return 2*math.pi*(self.radius)
# area = Circle(1).area()
# dlina = Circle(2).area()
# print(area)
# print(dlina)

# class Movie:
#     raiting=[1,2,3,4,5,6,7,8,9,10]
#     def __init__(self,name,author,year,raiting):
#         self.name=name
#         self.author=author
#         self.year=year
#         self.raiting=raiting
#     def add_raiting(self,raiting):
#         self.raiting.append(raiting)

# class Vector:
#     def __init__(self, x, y):
#         self.x = x 
#         self.y = y
#     def __str__(self):
#         return f"Вектор {self.x} и {self.y}"
    
#     def __add__(self,other):
#         return Vector(self.x + other.x, self.y + other.y)
    
#     def __eq__(self, other):
#         return self.x==other.x and self.y==other.y

# vector1=Vector(*map(float,input('ghjk').split()))
# vector2=Vector(*map(float,input('gjk').split()))

# print(vector1)
# print(vector2)
# print(vector1+vector2)
# print(vector1==vector2)

# # абстрактные методы:
# from abc import abstractmethod,ABC

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width*self.height
    
# rect=Rectangle(5,6)
# print(rect.area())

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name}, {self.age} лет"

# class Cat(Animal):
#     def __init__(self, name, age, poroda):
#         super().__init__(name, age)
#         self.poroda = poroda
    
#     def __str__(self):
#         return f"Кот: {self.name}, {self.age} лет, порода: {self.poroda}"

# class Dog(Animal):
#     def __init__(self, name, age, poroda):
#         super().__init__(name, age)
#         self.poroda = poroda
    
#     def __str__(self):
#         return f"Собака: {self.name}, {self.age} лет, порода: {self.poroda}"

# cat = Cat("Муся", 4, "Сиамская")
# dog = Dog("Даша", 7, "Такса")

# print(cat)
# print(dog)

# class BankAccount:
#     def __init__(self,account_number,account_owner,balance):
#         self.__account_number=account_number
#         self.__account_owner=account_owner
#         self.__balance=balance

#     def get__account_number(self):
#         return self.__account_number
#     def get_account_owner(self):
#         return self.__account_owner
#     def get_balance(self):
#         return self.__balance
    
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             return True
#         return False
    
#     def withdraw(self,amount):
#         if 0<amount<=self.__balance:
#             self.__balance-=amount
#             return True
#         return False
    
#     def info(self):
#         print(self.__account_number)
#         print(self.__account_owner)
#         print(self.__balance)

# bank1=BankAccount(1455677, "Иван Петров",1000)

# bank1.get__account_number()
# bank1.get_account_owner()
# bank1.get_balance()

# bank1.deposit(500)
# bank1.withdraw(300)
# bank1.info()

# class Student:
#     def __init__(self, name):
#         self.__name=name
#         self.__grades=[]
#     def get__name(self):
#         return self.__name
#     def get__grades(self):
#         return self.__grades
#     def add_grade(self,grade):                                              
#         if isinstance(grade,(int,float)) and  1<=grade<=5:
#             self.__grades.append(grade)
#             return True
#         return False
#     def get_average(self):
#         if not self.__grades:
#             return 0
#         return sum(self.__grades)/len(self.__grades)
#     def info(self):
#         print(self.__grades)
#         print(self.__name)
#         print(self.get_average())
# student1=Student("Чередниченко Юрий")
# student2=Student("Власова Милана")
# student1.add_grade(5)
# student1.add_grade(4)
# student2.add_grade(4)
# student2.add_grade(2)

# student1.info()
# student2.info()

# class Car:
#     def __init__(self, model, year, mileage, fuel_level):
#         self.__model=model
#         self.__year=year
#         self.__mileage=mileage
#         self.__fuel_level=fuel_level

#     def get__model(self):
#         return self.__model
    
#     def get__year(self):
#         return self.year
    
#     def get__mileage(self):
#         return self.__mileage
    
#     def get__fuel_level(self):
#         return self.__fuel_level
    
#     def drive(self,km):
#         if km>0 and self.__fuel_level >=km*0.1:
#             self.__mileage+=km
#             self.__fuel_level-=km-0.1
#             return km
        
#     def refuel(self,litr):
#         if litr>0:
#             self.__fuel_level+=litr
#             return litr
        
#     def info(self):
#         return self.__model,self.__year,self.__fuel_level,self.__mileage
    
# car=Car("Модель123",2005)

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
    
#     def discount_price(self):
#         pass

# class Promo(Product):
#     def discount_price(self):
#         return self.price * 0.8

# class PromoX2(Product):
#     def discount_price(self):
#         return self.price * 0.4

# phone = [Promo('Айфон', 1000000), PromoX2('Самсунг', 500000)]
# for ph in phone:
#     print(ph.discount_price())

# # утиная типизация
# class Duck:
#     def __init__(self, name):
#         self.name = name
    
#     def make_sound(self):
#         return "кря-кря"
    
#     def swim(self):
#         return 'утка плавает'

# class Dog:
#     def __init__(self, name):
#         self.name = name
    
#     def make_sound(self):
#         return "гав-гав"
    
#     def run(self):
#         return 'собака бегает'

# class Fish:
#     def __init__(self, name):
#         self.name = name
    
#     def swim(self):
#         return 'рыба плавает'

# class Robot:
#     def __init__(self, name):
#         self.name = name
    
#     def walk(self):
#         return 'робот гуляет'
    
#     def make_sound(self):
#         return "бип-бип"

# def make_sound_animal(animal):
#     if hasattr(animal, "make_sound"):
#         return animal.make_sound()
#     else:
#         return "Животное не издаёт звуков"

# def can_swim_animal(animal):
#     if hasattr(animal, "swim"):
#         return animal.swim()
#     else:
#         return "Животное не плавает"

# animals = [Duck("дональд дак"), Dog("николай"), Fish("максим"), Robot("марина")]
# for animal in animals:
#     print(make_sound_animal(animal))

# for animal in animals:
#     print(can_swim_animal(animal))
# from abc import abstractmethod
# class Pay:
#     def __init__(self,summa,sp_pay):
#         self.summa=summa
#         self.sp_pay=sp_pay
#     @abstractmethod
#     def price_pay(self):
#         pass

# class Nal_pas(Pay):
#     def price_pay(self):
#         return self.summa -(self.summa*0.01)
    
# class Pr_pas(Pay):
#     def price_pay(self):
#         return self.summa-(self.summa*0.03)
    
# sp=[Nal_pas(4000,"Наличные"),Pr_pas(4000,"Перевод")]
# for i in  sp:
#     print(i.price_pay())
    
# Сериализация и десериализация

# import pickle
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

# point=Point(4,5)

# with open("main.pkl","wb") as file: #wb - write bites -запись байтов в бинарник
#     pickle.dump(point,file) #сереализация

# with open("main.pkl","rb") as file: #wb - read bites - чтение в бинарном формате
#     loaded_x_y=pickle.load(file)

# with open("main.pkl","rb") as file:
#     raw=file.read(50) #чтение первых 50 байтов
#     print(raw)
# print(point.x,point.y)
# print(loaded_x_y.x,loaded_x_y.y)

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

# points=[Point(4,5),Point(6,7),Point(9,0)]

# with open("main.pkl","wb") as file:
#     pickle.dump(points,file)

# with open("main.pkl","rb") as file:
#     loaded_x_y=pickle.load(file)

# for i in loaded_x_y:
#     print(i.x,i.y) # вывод для списка

# student={
#     "Anna":34,
#     "Anna1":34
# }

# with open("js.json","w",encoding="utf-8") as file:
#     json.dump(student,file,ensure_ascii=False,indent=4)

# with open("js.json","r",encoding="utf-8") as file:
#     p=json.load(file)

# print(p)

# class User:
#     def __init__(self,name,age):
#         self.name =name
#         self.age=age
    
#     def to_dict(self):
#         return{
#             "name":self.name,
#             "age":self.age,
#         }
#     @classmethod
#     def from_dict(cls,st):
#         return cls(
#             name=st["name"],
#             age=st["age"],
#         )

# user=User("tanya",17) #экзепмляр

# with open("js.json","w",encoding="utf-8") as file:
#     json.dump(user.to_dict(),file,ensure_ascii=False,indent=4)

# with open("js.json","r",encoding="utf-8") as file:
#     p=json.load(file)
# #класс не может быть сериализован

# user=User.from_dict(p)
# print(user.name,user.age)

# print(user.age,user.name)
# print(p) #последний тип


#кастомизация двух модулей + безопасность

# уменьешние размера файла (сжатие - zip)
# import gzip
# import pickle

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

# p=Point(5,6)

# with gzip.open("main.pkl.gs","wb") as file:
#     pickle.dump(p,file)

# with gzip.open("main.pkl.gs","rb") as file:
#     pickle.load(file)

# import os

# orig_size=os.path.getsize("main.pkl")
# gz_size=os.path.getsize("main.pkl.gs")
# print(orig_size)
# print(gz_size)

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

# p=Point(5,6)
# print(type(p))

# massiv=pickle.dumps(p)
# print(type(massiv))
# from_massiv=pickle.loads(massiv)
# print(type(from_massiv))
# print(from_massiv.x)
# print(from_massiv.y)

# class User:
#     def __init__(self,login,passw):
#         self.login=login
#         self.passw=passw
#     def __getstate__(self):
#         state=self.__dict__.copy()
#         del state["passw"]
#         state ["version"]=1
#         return state
#     def __setstate__(self,state):
#         version=state.pop("version",None)
#         self.__dict__.update(state)
#         self.passw=""
#     def upgrade(self):
#         self.version+="обновление"
#         if self.version<2:
#             self.upgrade()

# obj=User("Старые данные",123)
# user=User("123@mail.ru",123)

# with open("main.pkl.gs","wb") as file:
#     pickle.dump(user,file)

# with open("main.pkl.gs","rb") as file:
#     user1_0= pickle.load(file)

# print(user.login,user.passw)
# print(user1_0.login,user1_0.passw)

# вложенные объекты и насследование, протоколы - если данные передаются от одного приложения к другому (1. протокол 0 - не является безопасным и востребованным,
#1. протокол первый - болле компактный чем текст, первый бинарный, 3. протокол два - ввоядт новые типы классов, 
#4. протокол три - поддержка объектов bytes, 5. протокол четыре - поддержка данных для сериализации размером 4 гб, 
#6. протокол пять - передаёт данные без лишнего копирования)

# class Group:
#     def __init__(self,name):
#         self.name=name

# class Student:
#     def __init__(self,name,group):
#         self.name=name
#         self.group=group

# group=Group("П-1-24") #атрибут класса Group

# st=Student("ДАня",group) #атрибут класса Ctudent

# obj=pickle.dumps(st,protocol=pickle.HIGHEST_PROTOCOL)
# new_obj=pickle.loads(obj)
# print(new_obj.name,new_obj.group.name)

# JSON - не поддерживает автоматических преобразований

# class User:
#     def __init__(self,name,age):
#         self.name =name
#         self.age=age
    
#     def to_dict(self):
#         return{
#             "name":self.name,
#             "age":self.age,
#         }
#     @staticmethod
#     def from_dict(cls,st):
#         return cls(
#             name=st["name"],
#             age=st["age"],
#         )

# def to_default(obj):
#     if isinstance(obj,User): #isinstance - проверяет все объекты
#         return obj.to_dict()

# user=User("tanya",17)

# with open("js.json","w",encoding="utf-8") as file:
#     json.dump(user,file,default=to_default,ensure_ascii=False,indent=4)

# with open("js.json","r",encoding="utf-8") as file:
#     p=json.load(file)

# user=User.from_dict(p)
# print(user.name,user.age)
# print(user.age,user.name)

# from dataclasses import dataclass,asdict

# @dataclass #автоматическое преобразование данных
# class User:
#     name:str
#     age:int
#     grades:list

# user=User("g",5,[4,5,3])

# obj = asdict(user)
# print(type(obj))

# ser=json.dumps(obj) #записывает и сериализует данные в виде последовательности строк
# # * - оператор распаковки 
# des=json.loads(ser)
# obje=User(**des)
# print(obje)
# print(user)

# #Синхронное (ждет завершения операции и продолжает работу) и асинхронное () программирование

# import time
# print("Начало процесса")
# time.sleep(2)
# print("Процесс завершен")
# # ^^^ Синхронное программирование ^^^
# # |||                             |||
# import requests #модуль для работы с синхронными http запросами

# print("начинаю скачивать первое изображение")
# response=requests.get("https://ya.ru/images/search?pos=26&from=tabbar&img_url=https%3Alastfm.freetls.fastly.netiFuar0a1ce7ac0c97d5c4a5830187139097059.jpg&text=addison+rae+2026&rpt=simage&lr=213")
# print("скачалось первое изображение")
# print("начинаю скачивать второе изображение")
# response1=requests.get("https://ya.ru/images/search?pos=26&from=tabbar&img_url=https%3Alastfm.freetls.fastly.netiFuar0a1ce7ac0c97d5c4a5830187139097059.jpg&text=addison+rae+2026&rpt=simage&lr=213")
# print("скачалось второе изображение")
# print(response.status_code) #если 200 - то успешно, если 400, то нет
# print(response.text) #текст ответа 2
# print(response.content) #скачанные байты
# 
# import asyncio
# async def hello():
#     print("hello")
#     await asyncio.sleep(2)
#     print("p-1-24")

# async def main():
#     task1=asyncio.create_task(hello()) #крутина
#     task2=asyncio.create_task(hello())
#     await task1
#     await task2

# asyncio.run(main())
# # ^^^ Асинхронное программирование ^^^
# # |||                              |||

# работа с ассинхронными http-запросами

# import aiohttp

# async def download(session,url,name): #
#     print(f"начинаю скачивать изображение {name}")
#     async with session.get(url) as response: #контекстный менеджер, открывающий соединение
#         image_data= await response.read()
#         print(f"Изображение скачалось {name}")
#         return image_data

# async def main():
#     async with aiohttp.ClientSession() as session:
#         task1=download(session,"https://ya.ru/images/search?pos=26&from=tabbar&img_url=https%3Alastfm.freetls.fastly.netiFuar0a1ce7ac0c97d5c4a5830187139097059.jpg&text=addison+rae+2026&rpt=simage&lr=213","картинка 1")
#         task2=download(session,"https://ya.ru/images/search?pos=26&from=tabbar&img_url=https%3Alastfm.freetls.fastly.netiFuar0a1ce7ac0c97d5c4a5830187139097059.jpg&text=addison+rae+2026&rpt=simage&lr=213","картинка 2")
#         task3=download(session,"https://ya.ru/images/search?pos=26&from=tabbar&img_url=https%3Alastfm.freetls.fastly.netiFuar0a1ce7ac0c97d5c4a5830187139097059.jpg&text=addison+rae+2026&rpt=simage&lr=213","картинка 3")

#         await asyncio.gather(task1,task2,task3)
        
# asyncio.run(main())

# #многопоточность 
# import time
# import threading
# def work():
#     print("Начало работы потока")
#     time.sleep(2)
#     print("gпоток закончил работу")
# print("главная программа, создаём поток")
# t=threading.Thread(target=work) #в target находится действие определенное в этом потоке
# print("Запускаем поток")
# t.start()
# t.join()

# def make_coffee():
#     print("начали варить кофе")
#     time.sleep(2)
#     print("закончили варить кофе")

# def eggs():
#     print("начали варить яйцо")
#     time.sleep(2)
#     print("закончили варить яйцо")

# t1=threading.Thread(target=make_coffee)
# t2=threading.Thread(target=eggs)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# import time
# def d():
#     total =0
#     for i in range(20_000_000):
#         total+=1
# start=time.time()
# d()
# end=time.time()
# print(round(end-start,2),"сек")
# rlock=threading.RLock() #  используется в рекурсиях
# lock=threading.Lock() # когда несколько потоков
# import threading
# start=time.time()
# total=0
# def d1():
#     global total
#     for i in range(20_000_000):
#         with lock:
#             total+=1
#     start=time.time()

# t=threading.Thread(target=d1)
# t1=threading.Thread(target=d1)
# end=time.time()
# t.start()
# t1.start()
# t.join()
# t1.join()
# end=time.time()

# print(round(end-start,2),"сек")
# print(end-start,2)

#Сетевое программирование (для сетевого приложения, в котором клиент и сервер общается по сети)
# TSP - следит за каждым битом информации, который передаётся (используется сейчас) , UTP - для быстрой отправки, когда надо скачать видео или музыку, например, где небольшая потеря данных не так важна как скорость передачи
# ipf-4 вроде протокол

#сокет - конечная точка связи, которая позволяет общаться между клиентом и серверов в виде байтов

# import socket

# socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# socket_server.bind(("127.0.0.1", 5000))
# socket_server.listen()
# print("Сервер запущен и ждет клиента")
# client_socket, client_address = socket_server.accept()
# print("Подключился клиент", client_address)
# data = client_socket.recv(1024)
# print("Получено сообщение:", data.decode("utf-8"))
# client_socket.close()
# socket_server.close()

# демоны в потоке (потоки-демоны) -  поток, который выполняет задачу в фоновом режиме: автоматическое сохранение, просмотр, добавление записей
# многопоточный сервер - сервер который обслуживает сразу несколько клиентов. создаём конкретный поток, в который передаём функцию, отвечающую за итоговый результат

# import threading
# import time

# def count():
#     count=0
#     while True:
#         count+=1
#         time.sleep(2)
#         print(f"Прошло {count} секунд")


# t1=threading.Thread(target=count,daemon=True).start() # действие в фоновом режиме

# a=input("вы хотите выйти?")
# когда создаётся поток-демон, поток не заканчивается, пока не закроешь самостоятельно клавишой "Enter"
# логирование - действие пользователей, которые записываются в логи. можно использовать потоки-демоны

# import threading
# import socket
# lock=threading.Lock()

# clients=[]
# def server_thr(client_socket,client_address):
#     print(f"Клиент {client_address} подключён")
#     # состояние гонки raceCondition 
#     while True:
#         data=client_socket.recv(1024) #размер буфера обмена
#         if not data:
#             break
#         message=data.decode("utf-8")
#         print(f"{client_address} пришло сообщение {message}")
#         with lock:
#             if client_socket in clients:
#                 clients.remove(client_socket)
#         client_socket.close()

# socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF -семейство протоколов. SOCK_STREAM - использование TSP
# socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #setsockopt - уровень опций
# socket_server.bind(("127.0.0.1", 5000)) #привязка через указание IP-адреса
# socket_server.listen() # прослушиваем входящее соединение
# print("Сервер запущен и ждет клиента")

# while True:
#     client_socket,client_address=socket_server.accept() #принимает новые подклуючения и блокирует выполнение до появление нового клиента. метод возвращает новый сокет с клиентом и его адрес, с которым происходит общение
#     with lock:
#         clients.append(client_socket)
#     th=threading.Thread(target=server_thr,args=(client_socket,client_address),daemon=True).start() #аргументы - клиент



# несколько клиентов, один заходит на сервер и отправляет сообщение клиентам которые ждут вход на сервер. на сервере создаём переменную которая будет принимать сообщение от клиента

# однадресный, широковещательный - используем второй

# пул потоков автоматичеки блокирует, все клиенты не затрагивают друг друга из-за оболчки где мы находимся как клиент
# IO bound - поток ввода и выода данных, запрос во внешнюю среду - быстрее чем CPU bound - задачи, которые свзяны с процессором, потоки оптимизирован

from threading import Event
from queue import Queue
# #  у каждого класса существует ограниченное число параметров

# queue = Queue(maxsize=10) #до 10 клиентов, при прослушивании в listen указвыается конченое число прослушиваемых клиентов, ЗДЕСЬ максимальное кол-во элементов может быть 10

# try:
#     queue.put(item="",block=False) #безопасное блокирование последующего клиента, которое передаёт элемент, block=False - при переполнении очереди блокируем
# except queue.Full as e: #исключение которое говорит что очередь переполнена, необходимо заблокирвать по Timeout
#     item=queue.get() #получение элемента из очереди, будет блокироваться до тех пор пока не получит элемент из очереди

# try:
#     queue.get(block=False,timeout=10) #элемент из очереди обрабатывается без блокировки, timeout - 10 секунд
# except queue.empty:
#     size=queue.size() # size - возвращает кол-во элементов которые сидят в очереди

# queue.task_done() #получение результата после обработки элемента и помечать его как выполненный
# queue.join() # в потокобезопасной очереди всегда ожидается завершение всех прцоессов, а только потом уже выходить, чтобы обработка была поочереди

# import time
# from queue import Empty,Queue #классы на работу с проверкой пустоты и потокобезопсаной очереди
# import threading

# def pr(queue):
#     for i in range(1, 6):
#         print(f"Вставляем элемент {i} в очередь")
#         time.sleep(1)
#         queue.put(i)
        

# def cus(queue):
#     while True:
#         try:
#             item = queue.get()
#         except Empty:
#             continue
#         else:
#             print(f"Обрабатываем элемент {item}")
#             time.sleep(1)
#             queue.task_done()

# def main():
#     queue = Queue()
    
#     p = threading.Thread(target=pr, args=(queue,))
#     c = threading.Thread(target=cus, args=(queue,), daemon=True)
    
#     p.start()
#     c.start()
    
#     p.join()
#     queue.join() 

# if __name__ == "__main__":
#     main()

# пул потоков: защищает от неожиданных сбоев, создаёт возможности определения потоков
# на хранение, удаление потоков выделяется много памяти, поэтому используется пул потоков, когда используется много задач, шаблон

# екзекьютор - расширяющий класс, возвращает объект future, который имет три метода: результат, exception - исключение ассинхронных операций
from threading import Thread
from time import sleep,perf_counter
from concurrent.futures import ThreadPoolExecutor 

# def task(id):
#     print(f"Начинаю загрузку {id}")
#     sleep(1)
#     return f"закончили задачу"

# start=perf_counter # измерение времени начала и окончания работы

# print(task(1))
# print(task(2))

# fin=perf_counter() # переменная для окончания
# print(f"Выполнение заняло {fin} секунд")

# def task(id):
#     print(f"Начинаю загрузку {id}")
#     sleep(1)
#     return f"закончили задачу"

# start=perf_counter()

# # сохдаём пул потоком, в котором есть возможность вызвать экзекьютор (executor)
# with ThreadPoolExecutor() as executor:
#     f1=executor.submit(task,1) # отправляет функцию на выполнение и возвращает объект futures, еще есть map - выполняет функццию для каждого элемента ассинхронно и shutdown -завершает работу исполнителя
#     f2=executor.submit(task,2)
    

# print(f1.result())
# print(f2.result())

# fin=perf_counter()
# print(f"Выполнение заняло {fin-start} секунд")
# # за счёт определения пула потока происходит одновременное выполнение задач
























