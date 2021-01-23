"""
Convert a decimal number to binary representation using Stack class
"""


class Stack(object):
    def __init__(self):
        """Initiate empty stack"""
        self.__stack = list()

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        return self.__stack.pop()

    def is_empty(self):
        return len(self.__stack) == 0

    def __str__(self):
        return str(list(self.__stack))


n = int(input("Enter a decimal number: "))

decimal_representation = n
binary_representation = Stack()

while decimal_representation > 0:
    digit = decimal_representation % 2
    binary_representation.push(digit)
    decimal_representation //= 2

binary_string = ""
while not binary_representation.is_empty():
    binary_string = binary_string + str(binary_representation.pop())

print(f"decimal {n} in binary is: {binary_string}")
