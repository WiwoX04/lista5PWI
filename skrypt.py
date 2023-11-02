liczba = 5
silnia = 1
while liczba > 0:
    silnia *= liczba  # Zmieniam "n" na "liczba"
    liczba -= 1  # Poprawiam błąd, powinno być odejmowanie
print(silnia)
