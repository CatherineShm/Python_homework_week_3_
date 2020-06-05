# ### Zadanie 4.6 | Kółko i krzyżyk
# Stwórz klasę `PlanszaXO` - jej obiekty mają reprezentować stan planszy do gry w kółko i krzyżyk.
# Ma ona mieć metody:
# `dodaj_element(x: int, y: int, rodzaj_elementu)`
# W argumencie `rodzaj_elementu` będzie napis `"x"` lub `"y"`. Jeśli ruch jest nieprawidłowy,
# metoda powinna zwracać fałsz.
# `stan_gry()`
# Ta metoda ma zwracać liczbę oznaczającą stan gry
# (gra trwa, gra zakończona sukcesem krzyżyków, gra zakończona sukcesem kółek).
# `czyj_ruch()`
# Ta metoda ma powiedzieć, czyj ruch ma być teraz (kółek czy krzyżyków).
# Wyświetlenie obiektu tej klasy ma wypisać planszę.
# Użyj tej klasy do zrobienia gry w kółko i krzyżyk.

class PlanszaXO:
    def __init__(self, field = [1, 2, 3, 4, 5, 6, 7, 8, 9]):
        self.field = field


    def add_element(self, position: int, sign: str):
        try:
            if sign == "O" or sign.upper() == "X":
                return self.field.insert(position, sign)
        except TypeError:
            return 'Please, provide the correct data ("0" or "X")'

    def games_status(self):
        pass


    def whose_move(self):
        if self.sign == "O":
            return f'Kolej "X"'
        if self.sign == "X":
            return f'Kolej "O"'


    def field_description(self):
        return self.field

graczL = PlanszaXO
graczL.add_element(5, "0")