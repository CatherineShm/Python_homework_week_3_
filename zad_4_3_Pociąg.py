### Zadanie 4.3 | Pociąg
# Stwórz klasę `Pociag`. Klasa niech ma dwa atrybuty: predkość (początkowa wartość to 10)
# i ilosc_paliwa (początkowa wartość to 1000).
# Dodaj do klasy `Pociag` metode `opis`. Ta metoda niech zwraca napis o treści "Moja predkość to (ileś tam).
# Mam jeszcze (ileś tam) litrów paliwa." Dodatkowo zaimplementuj metodę `__str__`.
# Dodaj metode `przyspiesz`. Ta metoda niech przyjmuje jeden argument mówiący, o ile ma zwiekszyć się prędkość.
# Ta metoda niech zwiększa predkość pociągu o tyle, ile jest powiedziane w argumencie.
# I niech zmniejsza ilość paliwa o: `(nowa predkosc - stara_predkosc) * (stara predkosc / 100)`.
# Niech nie da się jednorazowo zwiększyć prędkości o więcej niż 75% (jeśli ktoś spróbuje tak
# zwiększyć prędkość, prędkość niech pozostaje po prostu bez zmian). Niech nie da sie
# zwiększyć prędkości, jeśli pociąg nie ma juz paliwa (jeśli ktoś spróbuje zwiększyć prędkość, kiedy
# nie ma paliwa, prędkość niech pozostaje po prostu bez zmian).
# Przetestuj swoje rozwiązanie i napisz testy, w których:
# - zwiększysz prędkość pociągu o 5 km/h i wypisze jego opis
# - zwiększysz prędkość pociągu o 20 km/h i wypisze jego opis
# - zwiększysz prędkość pociągu o 8 km/h i wypisze jego opis
# - zwiększysz prędkość pociągu o 10 km/h i wypisze jego opis
import pytest


class Train:
    def __init__(self, speed: int = 10, fuel_level: int = 1000):
        """
        The first definition of the train.
        :param speed: describe the initial speed
        :param fuel_level: describe how much fuel train has
        """
        self.speed = speed
        self.fuel_level = fuel_level

    def description(self):
        return f'Moja prędkość: {self.speed} km/h\n' \
               f'Mam jeszcze {self.fuel_level} l paliwa.'

    def __str__(self):
        return self.description()

    def speed_up(self, how_much: int):
        if how_much > self.speed * 0.75:
            self.speed = self.speed

        else:
            new_speed = self.speed + how_much
            self.fuel_level_1 = (new_speed - self.speed) * (self.speed / 100)
            self.fuel_level -= self.fuel_level_1
            if self.fuel_level <= 0:
                self.speed = self.speed
            else:
                self.speed = new_speed

        return self.speed, self.fuel_level


def test_speed_up_1():
    train = Train(10, 1000)
    assert train.speed_up(5) == (15, 999.5)
    assert train.speed_up(10) == (25, 998)
    assert train.speed_up(30) == (25, 998)


def test_speed_up_2():
    train = Train(10, 1000)
    assert train.speed_up(20) == (10, 1000)


def test_speed_up_3():
    train = Train(10, 1000)
    assert train.speed_up(6) == (16, 999.4)


def test_speed_up_4():
    train = Train(10, 1000)
    assert train.speed_up(10) == (10, 1000)
    assert train.speed_up(5) == (15, 999.5)
    assert train.speed_up(20) == (15, 999.5)
    assert train.speed_up(8) == (23, 998.3)
    assert train.speed_up(10) == (33, 996.0)
