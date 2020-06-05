### Zadanie 4.4 | Zbiornik
# Stwórz klasę `Zbiornik`. Niech ta klasa ma tylko jeden atrybut: `ilosc_wody` (z początkową wartością 0).
# Niech ta klasa ma metody `dolej` i `odlej`. Obie metody niech przyjmują argument `ile` i niech
# odpowiednio dodają lub odejmują tę liczbę do atrybutu `ilosc_wody`. Niech nie da się odlać
# więcej wody, niż jest w zbiorniku.
# Niech obiekt klasy `Zbiornik` po skonwertowaniu na napis dawał napis `zbiornik z (ileś tam) litrami wody`.
# Przerób klasę `Zbiornik` tak, żeby miała też drugi atrybut - `temperatura`. Metoda dolej oprócz
# argumentu `ile` powinna też przyjmować argument `temperatura` oznaczający temperaturę dolewanej wody.
# Dolanie wody do zbiornika powinno powodować zmianę temperatury wody w zbiorniku (zgodnie ze zwykłymi
# prawami fizyki).
from pytest import approx


class Zbiornik:
    def __init__(self, ilosc_wody: int or float = 0, temperatura: int or float = 0, pojemnosc: int or float = 0):
        """
        Afin d'utiliser cette fonction, il faut preciser la qnt de l'eau, la temperature et la capacite de reservoir.
        :param ilosc_wody: la qnt de l'eau (l)
        :param temperatura: la temperature
        :param pojemnosc: la capacite de reservoir
        """
        self.ilosc_wody = ilosc_wody
        self.pojemnosc = pojemnosc
        self.temperatura = temperatura


    def opis(self):
            return f'Zbiornik z {self.ilosc_wody} litrami wody t = {self.temperatura} (pojemnosc: {self.pojemnosc} l).'


    def __str__(self):
        return self.opis()


    def dolej(self, ilosc, temperatura_1):
        self.ilosc_wody += ilosc
        self.temperatura = (self.temperatura + temperatura_1)/self.ilosc_wody * self.ilosc_wody

        if self.ilosc_wody > self.pojemnosc:
            return f"Pense bien qu'est ce que tu veux faire!"
        else:
            return self.ilosc_wody, self.temperatura


    def odlej(self, ilosc):
        if ilosc > self.ilosc_wody:
            return f"C'est pas possible. Il y a que {self.ilosc_wody} l de l'eau dans le reservoir."
        else:
            self.ilosc_wody -= ilosc
        return self.ilosc_wody, self.temperatura


def test_dolej():
    butla = Zbiornik(60, 30, 120)
    assert butla.dolej(50, 90) == (110, approx(120))
    assert butla.dolej(30, 20) == f"Pense bien qu'est ce que tu veux faire!"


def test_odlej():
    butla = Zbiornik(60, 30, 120)
    assert butla.odlej(30) == (30, 30)
    assert butla.odlej(70) == f"C'est pas possible. Il y a que 30 l de l'eau dans le reservoir."