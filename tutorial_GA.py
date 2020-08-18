# SOURCE: https://youtu.be/rfscVS0vtbw
# SOURCE: https://www.mikedane.com/programming-languages/python/
#
# Learn Python - Full Course for Beginners [Tutorial] - by Mike Dane (Giraffe Academy)
#
# character_name = "Tom"
# character_age = 50
#
# print("Character name is " + character_name + " .")
# print("Character age is " + str(character_age) + " years.")
#
# TOPIC: Basic operations with strings
# phrase = "Giraffe Academy"
# # print(phrase.lower())
# # print(phrase)
# print(phrase.replace("Giraffe", "Elephant"))
# END ------------------------------------------
#
# TOPIC: Math operations and importing "math"
# from math import *
#
# print(sqrt(3.19999))
# END --------------------------------
#
# TOPIC: Multiple input in one line
# color, plural_noun, celebrity = input("Enter color, plural noun and celebrity: ").split('-')
# print(f"Roses are {color}")
# print(f"{plural_noun} are blue")
# print(f"I love {celebrity}")
# END ----------------------------------------------
#
# TOPIC: Accessing list elements
# my_friends = ["Kevin", 2, False, "Mike", "Susie", 145, "John"]
# print(my_friends)
# print(f"Length of the array is {len(my_friends)}")
# print(f"Accessing [1:4] means index 1, 2, 3, not including 4: {my_friends[1:4]}")
# print(f"Elements [-4:-1] are {my_friends[-4:-1]}")
# print("Since range stops before the second index in [], i cannot include last list element using negative range")
# print("Because the program will stop before [-1] on index [-2]")
# print(f"All elements starting with index [3] are: {my_friends[3:]}")
# print(f"Or I can use [3:last_index+1], so [3:7] for a 7 array with actual last index 6: {my_friends[3:7]}")
# END -----------------------------------------------
#
# TOPIC: Basic operations on lists; extend, append, insert etc
# lucky_numbers = [15, 16, 4, 8, 23, 42]
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# friends.extend(lucky_numbers)
# print(friends)
# friends.append("Creed")
# friends.append(lucky_numbers[0])
# friends.insert(1,"Michael") # insert at specified index shifting everything else to the right
# friends.remove("Kevin") # remove either by exact name
# friends.remove(friends[2]) # remove my specifying element's index to be removed
# friends.clear()
# friends.pop() # if no argument: removes last element from list. OR, if given index, removes element with this index
# print(friends.index("Kevin")) # returns the index if element in the list or error
# print(friends.count("Kevin")) # return count of times the element is found in the list or 0 if not found
# lucky_numbers.sort() # by default sorts in ascending order
# friends.reverse() # reverse the order of elements in the list
# friends2 = friends.copy() # creates a copy of the list
# print(lucky_numbers)
# print(friends)
# END ------------------------
#
# TOPIC: Tuples
# coordinates = [(4, 6), (5, 8), (3, 21)]   # A list with tuples as list's elements
# print(coordinates[1][0])   # Print index[0] from the tuple which is at index[1] position in the list
# END ------------------------------------------------
#
# # TOPIC: Function definition and usage
# def say_hi(name, age):
#     print(f"Hello {name}, you are {age} years old")
#
#
# say_hi("Mike", "35")
# say_hi("Pete", 22)
# END -----------------------------------
#
# # TOPIC: IF Statement
# is_male = True
# is_tall = False
#
# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not is_tall:
#     print("You are a short male")
# elif not is_male and is_tall:
#     print("You are tall but not a male")
# else:
#     print("You are not tall and no male")
# END ------------------------------------
#
# # TOPIC: Using enumerate function in for loops to be able to handle both index and value at that index
# denominations_list = [1, '2', "masha", False, 20, "50 bitches", [100, 101, 102]]
#
# for pos, coin in enumerate(denominations_list):
#     print(f"Hello {coin}")
#
# END -------------------------------------
#
# TOPIC: Dictionaries
# months_dict = {
#     1: "January", 2: "February", 3: "March", 4: "April"
# }
# print(months_dict[2])
# print(months_dict.get(7, "Key not found"))
#
# TOPIC: Getting multiple (int) inputs in one line
# x, y, z = list(map(int, input().split()))
# print(x + y)
# END of Multiple Inputs --------------------------------------------
#
#
# # TOPIC: Guessing Game with while and IF
# # Variant 1
#
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not out_of_guesses:
#     if guess_count < guess_limit:
#         guess = input("Enter a guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("You Lose!")
# else:
#     print("You Win!")
# # END of Variant 1 --------------------------------------
#
# TOPIC: Guessing Game with while and IF
# Variant 2
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
#
# while True:
#     if guess == secret_word:
#         print("You win!")
#         exit()
#     elif guess_count >= guess_limit:
#         print("You lose!")
#         exit()
#     guess = input("Enter a guess: ")
#     guess_count += 1
# END of Variant 2 -----------------------------------------
#
# TOPIC: Guessing Game with while and IF
# Variant 3
# def guess_game(secret_word, guess_limit=5):
#     for i in range(guess_limit):
#         guess_try = input("Enter a guess: ")
#         if guess_try == secret_word:
#             return True
#     return False
#
#
# if guess_game("giraffe"):
#     print("You win")
# else:
#     print("You loose")
# END ----------------------------------------------------------
#
#
# TOPIC: Exponent function: my solution
# Get 2 inputs: base and exponent
# base_number = float(input("Enter base: "))
# exp_number = int(input("Enter exponent: "))
# # Set result equal to 1 for power of 0
# result = 1
# # Multiply required amount of times
# for i in range(exp_number):
#     result = result * base_number
# print(result)
# END of Exponent function
# ---------------------------------------------------------------
#
# TOPIC: Build a Translator
# every vowel -> to g
# dog -> dgg
# cat -> cgt
#
# def translate_giraffe(sentence):
#     translated_word = ""
#     for char in sentence:
#         if is_vowel(char) == 1:
#             translated_word = translated_word + "g"
#         elif is_vowel(char) == 2:
#             translated_word = translated_word + "G"
#         else:
#             translated_word = translated_word + char
#     return translated_word
#
#
# def is_vowel(char):
#     lower_vowels = ['a', 'e', 'i', 'o', 'u']
#     upper_vowels = ['A', 'E', 'I', 'O', 'U']
#     if char in lower_vowels:
#         return 1
#     elif char in upper_vowels:
#         return 2
#     return 3
#
#
# print(translate_giraffe("Anastacia"))

