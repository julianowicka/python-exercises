'''Napisz program zgodny z poniższą specyfikacją.
Specyfikacja
Dane
 - liczba naturalna
Wynik
Macierz kwadratowa o wymiarach , w której w każdym wierszu znajdują się wszystkie
liczby od do , a także w każdej kolumnie znajdują się wszystkie liczby od do . Wartości w
wierszu i kolumnie nie mogą się powtarzać.
Przykład
Dane
Wynik
3
1 2 3
2 3 1
3 1 2'''

n = int(input())

print("from 1", "to", n)
for j in range(n):
    for i in range(0, n ):
        print ((i+j)%(n)+1, end = ' ')
    print()

#another version
result = []

print("from 1", "to", n)
for j in range(n):
    result.append([])
    for i in range(0, n ):
        print ((i+j)%(n)+1, end = ' ')
        result[j].append((i+j)%(n)+1)
    print()
print(result)

for tab in result:
    for number in tab:
        print(number, end=" ")
    print()