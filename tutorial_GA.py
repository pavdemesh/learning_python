# character_name = "Tom"
# character_age = 50
#
# print("Character name is " + character_name + " .")
# print("Character age is " + str(character_age) + " years.")

# TOPIC: Basic operations with strings
# phrase = "Giraffe Academy"
# # print(phrase.lower())
# # print(phrase)
# print(phrase.replace("Giraffe", "Elephant"))

# TOPIC: Math operations and importing "math"
# from math import *
#
# print(sqrt(3.19999))

# TOPIC: Multiple input in one line
# color, plural_noun, celebrity = input("Enter color, plural noun and celebrity: ").split('-')
# print(f"Roses are {color}")
# print(f"{plural_noun} are blue")
# print(f"I love {celebrity}")
#
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
#
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
#
# # TOPIC: Tuples
# coordinates = [(4, 6), (5, 8), (3, 21)]   # A list with tuples as list's elements
# print(coordinates[1][0])   # Print index[0] from the tuple which is at index[1] position in the list
#
#
# # TOPIC: Function definition and usage
# def say_hi(name, age):
#     print(f"Hello {name}, you are {age} years old")
#
#
# say_hi("Mike", "35")
# say_hi("Pete", 22)
#
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
#


