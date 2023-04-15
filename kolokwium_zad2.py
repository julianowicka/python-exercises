"""
Napisz program zgodny z poniższą specyfikacją.
Specyfikacja
Dane
n - liczba naturalna
n linii tekstu - ciągu (małych i wielkich) liter alfabetu angielskiego i białych znaków
6 3 9 8 1 0 29 5 2 11
1 8 9 89 54 12 11 56 55 13
4
Wynik
Liczba wystąpień każdej litery z alfabetu angielskiego w podanym tekście z pominięciem
wielkości liter.
"""
n = int(input())
licznik = {}
for i in range(n):
    line = input()
    #print(i)
    for j in line:
        lower = j.lower()
        if lower in licznik:
            licznik[lower] = licznik[lower] +1
        else:
            licznik[lower] = 1

for letter in licznik:
    print(f"'{letter}': {licznik[letter]}")