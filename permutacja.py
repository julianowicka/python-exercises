"""
Tablice w programowaniu to podstawa. Posortowane tablice to także podstawa. A czymże jest posortowana tablica, jak nie
pewną permutacją tablicy początkowej?
Permutację tablicy można opisać podając docelową kolejność poszczególnych elementów tablicy, a także ich początkowy układ.
Twoje zadanie polega na wypisaniu permutowanej tablicy na podstawie takiego właśnie opisu.
Dane
 - n liczba elementów tablicy
 - opis permutacji: docelowa kolejność elementów, unikalne (bez powtórzeń) liczby całkowite z przedziału
 - wartości tablicy w jej początkowym ułożeniu, liczby całkowite
Dane
5
3 5 2 1 4
20 41 84 93 12

Wynik
93 84 20 12 41

"""
def readTable():
    line = input()
    string_numbers = line.split(' ')
    number_numbers = []
    for number in string_numbers:
        number_numbers.append(int(number))
    return number_numbers

n = int(input("podaj n"))
order = readTable()
values = readTable()

print(n)
print(order)
print(values)

result = []
for i in range(n):
    result.append(1)

print("result", result)

for i in range(n):
    print(i)
    result[order[i]-1] = values[i]

print(result)
