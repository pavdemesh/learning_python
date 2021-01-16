"""
https://youtu.be/-Zdu4ntX_DU
Python Hub Studio
"""


# class Purse:
#
#     def __ini t__(self, currency, name="Unknown"):
#         self.valuta = currency
#         self.user_name = name
#
#
# x = Purse("USD")
# print(x.valuta)
# x.valuta = "EUR"
# print(x.valuta)

class A:
    def a(self):
        print("A")


class B:
    def a(self):
        print("B")


class C(B):
    def a(self):
        print("C")


class D(C, A):
    def a(self):
        super().a()
        print(self.__class__.__mro__)


x = D()
x.a()
