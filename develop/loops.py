# Displays 4 films stored in a list. Use a for loop to show each film in the list. Create a function called film_check() that checks if the 3rd film in the list is Ghostbusters. If it is, it should return “yey it’s ghostbusters”. If it isn’t, it should return “booo, we want ghostbusters

# fav_films = ["ghost", "sister act", "rush hour", "fast and furious"]

# for i in fav_films:
#     print(i)



# def film_check(film):
#     if film[3] == film:
#         print("yey its ghostbusters")
#     else:
#         print("booo, we want ghostbusters!")

# film_check("ghostbusters")
# print(fav_films[0])


# from random import choice, randint

# for i in range(3):
#     num = randint(1,50)
#     print(num)

# for i in range(6):
#     print(i)
    


# # Create a for loop that prints out “hello world” 13 times. Now convert this to a while loop

# for i in range(13):
#     print("hellow world")

# count = 0

# while count <13:
#     count += 1
#     print("hello world")

# for i in range(1,50):
#     print("cabbage")

# count = 0

# while count < 3:
#     count += 1
#     print("cabbbage")

# # num = 0

# while num < (50):
#       num += 10
#       print(num)

# import random
# rand_num = random.randint (0,20)

# my_num = 20

# while rand_num != my_num:
#     print(rand_num)
#     rand_num = random.randint(0,20)

# print(f"you've found {my_num}")
  

# # Create a variable, generate a random number between 1 and 30 six times, each random number generated, check if this number of divisible by 7 or not

# from random import choice, randint

# num = None

# for i in range(6):
#     num = randint(1,30)
#     print(num)
# if num % 7 == 0:
#     print(f"(num)is divisable by 7")
# else:
#     print(f"(num) is not divisable by 7")

# for i in range(20, 0, -1):
#     print(i)



# Create a while loop to randomly cycle through a list of card suits until a given suit is reached. cards = ["Diamond", "Spade", "Club", "Heart"] Create a variable called current_card and use a list method to randomly give it a value from the list every time the loop runs. Then compare this to the suit you want to find to stop the while loop.

# from random import choice
# cards = ("heart" , "spade", "diamond", "club")

# current_card = None

# while current_card != "club":
#     current_card = choice(cards)
#     print(current_card)
#     if current_card == "club":
#         print("smashed it")
#     else:
#         print("hot dog")

# coin = ("one", "two", "three", "four")

# current_coin = None

# while current_coin != "four":
#     current_coin = choice(coin)
#     print(current_coin)
#     if current_coin == "four":
#         print("great")
#     else:
#         print("try again boomer")

# from random import choice


# crisps = ["doritoz","skips","wotsits","walkers"]
# current_crisps = None

# while current_crisps != "doritoz":
#     current_crisps = choice(crisps)
#     print(current_crisps)
# if current_crisps == "doritoz":
#     print("yayy")
# else:
#     print("space")

# num1 = 14
# num2 = 2

# if (num1 + num2) % 3 == 0:
#     print("happy")

# num = 22200221

# if str(num) == str(num)[::-1]:
#     print("this is palindrome")
# else:
#     print("this is not palindrome")

# print("naila"[::2])

# num = 12455420

# if str(num) == str(num)[::-1]:
#     print("palindrome baby!")
# else:
#     print("bobo")

 # finding the index of a vowel

# string = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"

# a = string.rfind("a")
# e = string.rfind("e")
# i = string.rfind("i")
# o = string.rfind("o")
# u = string.rfind("u")

# print(a,e,i,o,u)

# last = -1

# if a > last:
#     last = a
# if e > last:
#     last = e
# if i > last:
#     last = i
# if o > last:
#     last = o
# if u > last:
#     last = u


# print(last)

# print(string.rfind([a for a in string if a in "aeiou"][-1]))


# age = 75

# if age < 18:
#     print(8.00)
# elif age >= 60:
#     print(7.50)
# else:
#     print(10.95)



# find the index of a vowel

# string = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"


# a = string.rfind("a")
# e = string.rfind("e")
# i = string.rfind("i")
# o = string.rfind("o")
# u = string.rfind("u")
 

# print("a,e,i,o,u")

# last = -1

# if a > last:
#     last = a
# if e > last:
#     last = e
# if i > last:
#     last = i
# if o > last:
#     last = o
# if u > last:
#     last = u

# print(last)





















































# Additional readingResearch do...while loops, find out about the difference between for loop, while loop and do...while loop. Give an example of each. What are the pros and cons?Extra challenge:Create a program that check all numbers between 1 and 20 if it is a prime number or not.








# num = 1234

# new_num = str(num)

# for i in range(len(new_num)):
#     print(i, new_num[i])

 