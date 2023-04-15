'''Napisz program zgodny z poniższą specyfikacją.
Specyfikacja
Dane
 - ciąg unikalnych wartości liczbowych, podanych w jednej linii i
oddzielonych znakiem spacji
 - ciąg unikalnych wartości liczbowych, podanych w jednej linii i
oddzielonych znakiem spacji
Wynik
Liczba wspólnych elementów dla ciągów i .
Przykład
Dane
6 3 9 8 1 0 29 5 2 11
1 8 9 89 54 12 11 56 55 13
Wynik
4
Wyjaśnienie
Wspólne elementy'''
line1 = input().split()
print(line1)
line2= input().split()
set1 = set(line1)
set2 = set(line2)
licznik = 0
for a in set2:
    if a in set1:
        licznik += 1
print(licznik)
print(set1)