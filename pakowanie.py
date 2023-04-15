"""Nareszcie wakacje! Czas gdzieś wyjechać. Najpierw jednak czas się spakować. Masz do dyspozycji jedną walizkę w kształcie prostopadłościanu o wymiarach . Udało Ci się zebrać wszystkie potrzebne rzeczy w jeden mały pakunek, także o kształcie prostopadłościanu. Pytanie brzmi, czy zmieści się on do walizki? Nie chcesz nic uszkodzić, więc pakunek nie może wystawać i musi być ułożony bokami równolegle do boków walizki.
Źródło: https://onlinejudge.org/external/123/12372.pdf
Specyfikacja
Dane
 - liczby naturalne, wymiary pakunku, wszystkie z zakresu
Wynik
Komunikat "TAK", jeżeli pakunek zmieści się walizce, lub komunikat "NIE" w przeciwnym przypadku
Przykład 1
Dane
a := 20
b := 20
c := 20
Wynik: "TAK"
Przykład 2
Dane
a := 1
b := 2
c := 21
Wynik: "NIE" """
a = int(input())
b = int(input())
c = int(input())
array = [a,b,c]
print(array)
array.sort()
print(array[1])
print(array.pop(1))