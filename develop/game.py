# from random import choice
# name = "bobo"
# #key

# def room_1():
#     global name
#     print(f"Hi {name} You have entered the Confectionary Room and come across a giant gummy bear. With a booming voice he says, In order to pass me and get the first key you need to answer this question.\nGummy bears were first made in which country?\n a. The United States \n b. Germany \n c. Italy")
#     choice = input(">>>  ")
#     if choice == "b":
#         print("The giant gummy bear goes in his pocket and hands you a key")
#         #key +1
#         #main()
#     elif choice == "c":
#         print("The giant gummy bear eats you in one go then poops you back to the strart")
#         #main
#     elif choice == "a":
#         print("The giant gummy bear eats you in one go then poops you back to the strart")
#         #main
#     else:
#         print("type a, b or c")

# room_1()

# name = "bobo"

# def room_2():
#     global name
#     print(f"Hi {name}. You have now entered the Gum room to try and earn a key. But lucky for you, you get stuck in a chewing gum spider web. You try and wiggle free until you spot a giant spider. The spider says \"""I will release you if you can give me the correct answer to this question\"""\n How long does chewing gum take to digest in your body?\n a. Three years \n b. Seven years \n c. It doesn't")

#     choice = input(">>>  ")
#     if choice == "a":
#         print("Spider spins you in her web and eats you for dinner!")
#         #main()
#     elif choice == "b":
#         print("Spider spins you in her web and eats you for dinner!")
#         #main
#     elif choice == "c":
#         print("Correct! I will now release you from my web and hand over a shiny key")
#         #key +1
#         #main
#     else:
#         print("type a, b or c")

# room_2()


# Congratulations bobo! You have reached the final room. Your challenge will be: Eat 10 crisps. Eat 10 chocolate bars. Eat 5 chewing gum. Eat 20 haribos

def boss_room():
    print("Congratulations bobo! You have reached the final room. Your challenge will be: Eat 10 crisps. Eat 10 chocolate bars. Eat 5 chewing gum. Eat 20 haribos.")
    crisps_eat() 

def crisps_eat():
    crisps_count = 9
    boss_choice = input("Eat 10 crisps: Type nom nom nom >>>").lower()
    if boss_choice == "nom nom nom":
        print(f"{crisps_count} crisps left")
        while crisps_count > 0:
            crisps_count -=1
            print(f"{crisps_count} crisps left")
    else:
        print("Type nom nom nom")
        crisps_eat()
        



def choco_eat():
    choco_eat = 9
    boss_choice = input("Eat 10 choco's: Type nom nom nom >>>").lower()
    if boss_choice == "nom nom nom":
        print(f"{choco_eat} choco's left")
        while choco_eat > 0:
            choco_eat -=1
            print(f"{choco_eat} choco's left")
    else:
        print("Type nom nom nom")
        choco_eat()
        
choco_eat()



def gum_eat():
    gum_eat = 4
    boss_choice = input("Eat 5 chewing gums: Type nom nom nom >>>").lower()
    if boss_choice == "nom nom nom":
        print(f"{gum_eat} gum's left")
        while gum_eat > 0:
            gum_eat -=1
            print(f"{gum_eat} gum's left")
    else:
        print("Type nom nom nom")
        gum_eat()
        
gum_eat()


def haribo_eat():
    haribo_eat = 19
    boss_choice = input("Eat 20 haribo's: Type nom nom nom >>>").lower()
    if boss_choice == "nom nom nom":
        print(f"{haribo_eat} haribo's left")
        while haribo_eat > 0:
            haribo_eat -=1
            print(f"{haribo_eat} haribo's left")
    else:
        print("Type nom nom nom")
        haribo_eat()
        
haribo_eat()

def boss_room()





# def crisps_count():
#     crisps_count = 10
#     current = None
#     while crisps_count >0:
#             crisps_count -=1
#             print(f"{crisps_count} crisps left")
#     else:
#         print("Type nom nom nom")

# crisps_count()


# def crisps_count():
#     crisps_count = 10
#     current = None
#     while crisps_count >0:
#             crisps_count -=1
#             print(f"{crisps_count} crisps left")
#     else:
#         print("Type nom nom nom")

# crisps_count()





#     if boss_choice == "nom nom nom":
#         print(f"{crisps_count} crisps left")
#             while crisps_count > 0:
#             crisps_count -=1
#             print(f"{crisps_count} crisps left")
#     else:
#         print("nom nom nom")
#         boss_room()

# boss_room()


# crisps_count = 10

# while crisps_count > 0:
#     crisps_count -=1
#     print(crisps_count)

# chocolate_count = 10

# while chocolate_count > 0:
#     chocolate_count -=1
#     print(chocolate_count)

# gum_count = 5

# while gum_count > 0:
#     gum_count -=1
#     print(gum_count)


# haribo_count = 20

# while haribo_count > 0:
#     haribo_count -=1
#     print(haribo_count)


# import sys, time, os

# message - "hello world, nic eto eet you"

# for char in message:
#     sys.stdout.write(char)