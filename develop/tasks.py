# Challenge 1: Create a variable called password.  Check how many letters are in the password, if there are less than 8 print that the password is too short. Otherwise print the password


password = ("michael")

if len(password) < 8:
    print("password is too short")
else:
    print(password)

# Challenge 2: Create a variable called num. Check if the variable is divisible by 3 or 5. If it is print “This number is divisible by 3 or 5” to the console. Otherwise log “This number is not divisible by 3 or 5”

num = 15
if num % 3 == 0 or num % 5 == 0:
         print("this number is divisable by 3 or 5")
else:
       print("is not divisable by 3 or 5")


# Challenge 3: Create a variable called num. If num is divisible by 3 print “fizz”, if it’s divisible by 7 print “buzz”, if it’s divisible by both 3 and 7 print “fizz buzz”. Otherwise print num

num = 15
if num % 3 ==0 and num % 7 ==0:
         print("fizz buzz")
if num % 7:
         print("buzz")
if num % 3:
        print("fizz")

else:
        print(num)

# Challenge 4: Create a variable called word that takes a string. Create an if statement that checks if the last letter is the same as the first. If it is return true, otherwise return false

word = input ("Any word")
if word [0] == word [-1]:
       print("True")
else:
    print("False")

#  Challenge 5: Create a variable called time, a variable called place_of_work and a variable called town_of_home. Create an if statement that prints where someone is at times of the day. E.g. if the time is 7 I’m at home, at 8 I’m commuting, at 9 I’m at work   

time = 1400
place_of_work = ("Develop Coding")
town_of_home = ("Gagaland")

if time >= 9.45 and =< 17.30:
    print("I am on a course racking my brains out")
elif time >= 18.00 and 18.30:
    print("having scrummy tea with family")
else:
    print(f"at home in (Gagaland)")


# Challenge 6: Create two variables called num1 and num2. Create an if statement that checks if the result of the sum is even. If it is, return a success message

num_one = 13
num_two = 7

if (num_one + num_two) is even or % 2 == 0:
    print("Success. This is an even number")
else:
    print("this is an odd number")


# Challenge 8: Take the string Challenge 8: Take the string “jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi”. Find the index of a last vowel in the string
    
string = ("jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi")
print(string[95]) or Print(string[-1])

string = ("jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi")

aeiou = input("vowel[-1]")
print(string([95]vowel [-1]))

# challenge 1

passeord - "naila"
if len(naila) > 8:
    print("password too short")
else:
    print("naila")

# challenge 2

num = 15

if num % 5 == 0 or num % 3 == 0:
    print("the number is divisible by 5 and 3")
    

