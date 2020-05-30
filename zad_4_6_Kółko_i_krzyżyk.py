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
    def __init__(self, height: int = 3, width: int = 3):
        self.height = height
        self.width = width
        field = self.height * self.width


    def add_element(self, x: int, y: int, sign: str):
        pass


    def games_status(self):
        pass


    def whose_move(self):
        pass


    def field_description(self):
        pass
