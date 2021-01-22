"""
Implement queue as a list.
Protect from mutation via encapsulation
"""


class Queue:

    def __init__(self, starting_queue=[]):
        self.__queue_list = list()
        for item in starting_queue:
            self.__queue_list.append(item)

    def enqueue(self, value):
        self.__queue_list.append(value)

    def dequeue(self):
        if self.__queue_list:
            self.__queue_list.pop(0)
        else:
            return False

    def display(self):
        print(f"The content of this queue is: ")
        for item in self.__queue_list:
            print(item)


obj = Queue([5, 7, 'Mariska'])
print(obj)
obj.display()
obj.enqueue(14)
obj.enqueue("Pasha")
obj.display()
