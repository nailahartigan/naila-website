# key1 = 0
# key2 = 0
# key3 = 0
# key4 = 0
# def start():
#     print("You notice a sign that reads \"Collect keys to exit this factory. Follow meeeeeeeeeeeee\". What do you do? a) Try and force the door open or b) Follow the sign.")
#     question_1 = input("Choose a or b?>>> ").lower()
#     if question_1 == "a":
#         print("It has been locked from the outside")
#         start()
#     if question_1 == "b":
#         print("I will just follow the signl...\nYou follow the sign down several corridors until you reach a big room with 5 doors. You notice another sign saying \"There are 4 rooms and 4 keys to collect, once you have collected all 4 keys you can progress the the main room, in which you then have to pass a final challenge to exit the factory... what room will you choose first?\"")
#         mainroom()
#     else:
#         print("Umm...What? Choose a or b.")
#         start()

# def boss_room():
#     print("Congratulations bobo! You have reached the final room. Your challenge will be: Eat 10 crisps. Eat 10 chocolate bars. Eat 5 chewing gum. Eat 20 haribos.")
#     crisps_eat()

# # def crisps_eat():
# #     crisps_count = 9
# #     boss_choice = input("Eat 10 crisps: Type nom nom nom >>>").lower().strip()
# #     if boss_choice == "nom nom nom":
# #         print(f"{crisps_count} crisps left")
# #         while crisps_count > 0:
# #             crisps_count -=1
# #             print(f"{crisps_count} crisps left")
# #         choco_eat()
# #     else:
# #         print("Type nom nom nom")
# #         crisps_eat()
# # def choco_eat():
# #     choco_eat = 9
# #     boss_choice = input("Eat 10 choco's: Type nom nom nom >>>").lower().strip()
# #     if boss_choice == "nom nom nom":
# #         print(f"{choco_eat} choco's left")
# #         while choco_eat > 0:
# #             choco_eat -=1
# #             print(f"{choco_eat} choco's left")
# #         gum_eat()
# #     else:
# #         print("Type nom nom nom")
# #         choco_eat()
# # def gum_eat():
# #     gum_eat = 4
# #     boss_choice = input("Eat 5 chewing gums: Type nom nom nom >>>").lower().strip()
# #     if boss_choice == "nom nom nom":
# #         print(f"{gum_eat} gum's left")
# #         while gum_eat > 0:
# #             gum_eat -=1
# #             print(f"{gum_eat} gum's left")
# #         haribo_eat()
# #     else:
# #         print("Type nom nom nom")
# #         gum_eat()
# # def haribo_eat():
# #     haribo_eat = 19
# #     boss_choice = input("Eat 20 haribo's: Type nom nom nom >>>").lower().strip()
# #     if boss_choice == "nom nom nom":
# #         print(f"{haribo_eat} haribo's left")
# #         while haribo_eat > 0:
# #             haribo_eat -=1
# #             print(f"{haribo_eat} haribo's left")
# #         print("You finally finish the last haribo, then all of a sudden the floor rumbles and a golden key emerges from the ground, you quickly grab the key and run to the exit, you unlock the door with the golden key and make your way out of the factory, all of a sudden you awake in your bedroom. You shake your head then get out of bed to get ready for work, you step on some gum that was on the floor. Was it a dream...or not?")
# #     else:
# #         print("Type nom nom nom")
# #         haribo_eat()

# def room_1 ():
#     global key1
#     if key1 == 1:
#         print("You've already done this room! Choose a different one.")
#         mainroom()
#     print("You enter the Confectionary Room and come across a giant gummy bear with a booming voice. He says \"In order to pass me and my key, you need to answer this question: Gummy bears were first made in which country?\" \n a) The United States, b) Germany, c) Italy")
#     answer = input("Choose an answer>>> ").lower().strip()
#     if answer == "b":
#         print("WELL DONE! Here is the Gummy Key")
#         key1 += 1
#         mainroom()
#     elif answer == "a" or answer == "c":
#         print("WRONG! Try Again!")
#         room_1()
#     else:
#         print("Type a, b or c")
#         room_1()

# def room_2():
#     global key2
#     if key2 == 1:
#         print("You've already done this room! Choose a different one.")
#         mainroom()
#     print("You have entered the Gum room to try and earn a key. You get stuck in a chewing gum spider web, you try and wiggle free until you spot a giant spider. The spider says \"I will release you if you can give me the correct answer to this question\"\n How long does chewing gum digest in your body?\n A). Three years \n B). Seven years \n C). It doesn't")
#     choice = input(">>>  ").lower().strip()
#     if choice == "c":
#         print("Correct! I will now release you from my web and hand over the Gum key")
#         key2 += 1
#         mainroom()
#     if choice == "a" or choice == "b":
#         print("spider spins you in her web and eats you for dinner!")
#         room_2()
#     else:
#         print("type a, b or c")
#         room_2()

# def room_3 ():
#     global key3
#     if key3 == 1:
#         print("You've already done this room! Choose a different one.")
#         mainroom()
#     print("You enter the Chocolate Room and run into a Chocolate bunny. He says \"In order to pass me and get my key, you need to answer this question: Chocolate melts at which temperature?\" \n a) Around 34 Celsius b) Around 44 Celsius or c) Around 54 Celsius")
#     answer = input("Choose an answer>>> ").lower().strip()
#     if answer == "a":
#         print("\"WooHoo you have given me the correct answer, here is the Chocolate key! Now hurry up before I change my mind\"")
#         key3 += 1
#         mainroom()
#     elif answer == "c" or answer == "b":
#         print("HA! Wrong answer nerd! Its now time for you to melt...")
#         room_3()
#     else:
#         print("Type a, b or c")
#         room_3()

# def room_4 ():
#     global key4
#     if key4 == 1:
#         print("You've already done this room! Choose a different one.")
#         mainroom()
#     print("You enter the crisp room and you notice a crisp zombie \"Hi my name is walker, and I am guessing you are here for this key, BUT you can't have it until you give me the right answer to my question\" \n What year walkers founded? A. 1967 B. 1935 C. 1948")
#     answer = input("Choose an answer>>> ").lower().strip()
#     if answer == "c":
#         print("Awesome, you have given me the correct answer to my question, here is the Crisp key")
#         key4 += 1
#         mainroom()
#     elif answer == "a" or answer == "b":
#         print("Oh No! you have given me the wrong answer (He then looks at you and you instantly burn to a crisp!)")
#         room_4()
#     else:
#         print("Type a, b or c")
#         room_4()

# def mainroom():
#     keycount = key1 + key2 + key3 + key4
#     if keycount < 4:
#         print("a) The Confectionary Room b) The Gum Room c) The Chocolate Room or d) The Crisp Room")
#         answer = input("Choose a room: >>> ").lower().strip()
#         if answer == "a":
#             room_1()
#         elif answer == "b":
#             room_2()
#         elif answer == "c":
#             room_3()
#         elif answer == "d":
#             room_4()
#         else:
#             print("choose a, b, c or d")
#             mainroom()
#     else:
#         boss_room()
##start game
# print("You are wondering around and found and abandoned factory, you decide to explore the abandoned factory. You approach the door and notice the door is open a little bit. You open the door and walk in, but suddenly the door slams shut behind you.")
# start()