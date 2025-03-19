class PositiveNumber:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("raqam bolsin")
        if value <= 0:
            raise ValueError("musbat bolsin")

    def __delete__(self, instance):
        raise AttributeError("raqam topilmadi")


class Number:
    price = PositiveNumber("raqam")

    def __init__(self, price):
        self.price = price

p = Number(10)
p.price = 20
