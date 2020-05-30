### Zadanie 4.5 | Żółw
# Napisz klasę `Zolw` z metodami `idz` i `obroc_sie`. Żółw ma jakieś położenie
# (wyrażone dwiema współrzędnymi) i jakieś ustawienie, czyli kurs (wyznaczony pojedyncza liczba).
# Początkowe położenie podajemy konstruktorowi klasy, początkowy kurs to zawsze 0.
# Metoda `obroc_sie ` powoduje obrót żółwia, czyli zmianę jego kursu.
# Metoda `idz` powoduje przejście żółwia o określoną odległość.
# Z klasy będzie się korzystać tak:
#
# ```python
# z = Zolw(100, 100)
# z.idz(50)
# print(z) # ma sie wypisac: x=100, y=50
# z.obroc_sie(90)
# z.idz(50)
# print(z) # ma sie wypisac: x=150, y=50
# ```
import pytest



class Turtle:
    def __init__(self, x: int = 0, y: int = 0):
        """
        Turtle can go straight, turn left ot right and go back.
        :param x: one of the position's description
        :param y: one of the position's description
        """
        self.x = x
        self.y = y


    def description(self):
        """
        The Turtle's coordinate
        :return: coordinate
        """
        return f"x = {self.x}, y = {self.y}"


    def __str__(self):
        return self.description()


    def go(self, how_much, direction = "straight"):
        """
        With this function user can set parameters for distance and direction.
        By defolt, the Turtle goes straight, the change of the direction always related
        with the first Turtle's position.
        :param how_much: distance that Turtle should go
        :param direction: direction for Turtle
        :return: the new Turtle's coordinate
        """
        if direction == "straight":
            self.y += how_much
        elif direction == "right":
            self.x += how_much
        elif direction == "back":
            self.y -= how_much
        elif direction == "left":
            self.x -= how_much
        return self.x, self.y


def test_go_straight():
    zaba = Turtle()
    assert zaba.go(20) == (0, 20)
    assert zaba.go(65) == (0, 85)


def test_go_left():
    zaba = Turtle()
    assert zaba.go(30, direction="left") == (-30, 0)
    assert zaba.go(20, direction="left") == (-50, 0)


def test_go_right():
    zaba = Turtle()
    assert zaba.go(20, direction="right") == (20, 0)
    assert zaba.go(-5, direction="right") == (15, 0)


def test_go_back():
    zaba = Turtle()
    assert zaba.go(15, direction="back") == (0, -15)
    assert zaba.go(10, direction="back") == (0, -25)


def test_go():
    zaba = Turtle(10, 10)
    assert zaba.go(10, "left") == (0, 10)
    assert zaba.go(5, "back") == (0, 5)
    assert zaba.go(20, "left") == (-20, 5)
    assert zaba.go(10, "straight") == (-20, 15)
