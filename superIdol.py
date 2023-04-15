'''
Super idol
Sława to ciekawa sprawa. Jeżeli jesteś sławny to dużo ludzi zna
Ciebie, ale Ty ich wcale nie musisz znać. Super idol to ktoś, u kogo ta
różnica między tymi, którzy go znają a tymi, których on zna jest największa.
Napisz program, który dla poniższych danych wskaże super idola.
Wejście
W pierwszym wierszu wejścia będą podane dwie liczby całkowite L, R
(5 <= L <= 10000, 10 <= R <= 1000000) oznaczające odpowiednio ilość ludzi
w danej grupie oraz ilość relacji „ktoś kogoś zna” między nimi. W kolejnych
R wierszach będziemy mieli dwie liczby A i B (1 <= A, B <= L) oddzielone
pojedynczą spacją oraz różne od siebie, które oznaczają: „A zna B” (z tego
nie wynika, że B zna A). Żadna para liczb A B się nie powtarza (chociaż
oczywiście może się zdarzyć para B A).
Wyjście
Na wyjściu mają być podane dwie liczby w jednej linii. Pierwsza oznacza
numer osoby, będącej super idolem (to znaczy takiej, której różnica między
tym, kto ją zna, a tymi, których ona zna jest największa). Druga liczba
stanowi tę różnicę. Jeżeli takich osób jest więcej powinna zostać wypisana
ta, która ma największy numer.
Przykład:
1)
Wejście:
5 10
1 2
1 4
1 3
2 3
2 4
2 5
3 5
4 1
4 2
4 5
Wyjście
5 3
Osoba nr 5 jest znana przez 3 osoby, a sama nikogo nie zna)
'''

line = input().strip()

array = line.split()

people_number = int(array[0])
number = int(array[1])

znani = []
znaja = []
# dwie zerami - dl people_number
for i in range(people_number):
    znani.append(0)
    znaja.append(0)
for i in range(number):

    line2 = input().strip()
    array2 = line2.split()
    ktozna = int(array2[0]) - 1
    kogozna = int(array2[1]) - 1

    znani[kogozna] = znani[kogozna] + 1
    znaja[ktozna] = znaja[ktozna] + 1

wynik = []
for i in range(people_number):
    wynik.append(znani[i] - znaja[i])
maxi = max(wynik)
gwiazda = 1
for i in range(len(wynik)):
    if maxi == wynik[i]:
        gwiazda = i +1
print(f"{gwiazda} {maxi}")

