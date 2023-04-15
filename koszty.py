'''Opis
Pewna firma postanowiła przeprowadzić redukcję zatrudnienia. Celem jest cięcie kosztów. Pracownicy pracują w zespołach trzyosobowych. W ramach jednego zespołu zarobki pracowników mogą się różnić. Zarząd postanowił, że z każdego takiego zespołu zostaną zwolnione dwie osoby o skrajnych zarobkach, tzn.: osoba zarabiająca najwięcej i osoba zarabiająca najmniej. Kto przetrwa redukcję i pozostanie zatrudniony?
Źródło: https://onlinejudge.org/external/117/11727.pdf
Specyfikacja
Dane
 a,b,c- trzy liczby naturalne określające zarobki pracowników, wszystkie w zakresie
Wynik
Zarobki pracownika, który pozostanie zatrudniony
Przykład
Dane
a := 1500
b := 1200
c := 1800
Wynik: 1500
'''

a = int(input())
b = int(input())
c = int(input())
array = [a,b,c]
print(array)
array.sort()
print(array[1])
print(array.pop(1))