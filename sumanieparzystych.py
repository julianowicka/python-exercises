"""
Opis
Dla zadanego przedziału podaj sumę wszystkich nieparzystych liczb z tego przedziału.
Specyfikacja
Dane
a,b - liczby całkowite z przedziału [0,100]
Wynik
Suma wszystkich liczb nieparzystych z przedziału [a,b]
Przykład
Dane
a := 3
b := 9
Wynik
24"""

a = int(input("Podaj liczbę całkowitą: "))
b = int(input("Podaj liczbę całkowitą: "))
# result = 0
# for i in range(a,b+1):
#    if i%2==1:
#        result+=i

if a % 2 == 0:
    a += 1

odd_numbers = list(range(a, b + 1, 2))
result = sum(odd_numbers)
print(f"Suma nieparzystych liczb to {result}")
