'''
Gazeta Bitek w Bajtkowie cieszy się dużą popularnością, nawet w swojej oryginalnej, papierowej wersji. Co za tym idzie
wiele osób wysyła do redakcji swoje ogłoszenia do umieszczenia w kolejnym wydaniu. Do tej pory stawka była jasna: stała
kwota za każde ogłoszenie, w zależności od liczby znaków. Wydawca gazety Bitek zauważył jednak, że różne znaki zużywają
inne ilości tuszu, co oznacza, że koszt ich druku także się różni! Postanowił więc zaktualizować cennik i określić koszt
każdego znaku. Teraz opłata za wiadomość jest równa sumie kosztów każdego znaku z tej wiadomości.
Twoim zadaniem jest policzyć, ile będzie wynosić opłata za dany wyraz wedle nowego cennika.
'''

n = int(input())
mapa = {}
for i in range(n):
    [letter, cost] = input().split()
    mapa[letter] = int(cost)
result = 0
slowo = input().strip()
for i in range(len(slowo)):
    result += mapa[slowo[i]]
print(result / 100)
