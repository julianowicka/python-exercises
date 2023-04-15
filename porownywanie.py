"""Opis
Mając dane dwie liczby całkowite, określ relację między nimi, tzn. czy pierwsza jest mniejsza, większa, czy też równa drugiej.
Źródło: https://onlinejudge.org/external/111/11172.pdf
Specyfikacja
Dane
 - liczby całkowite z przedziału
Wynik
Znak relacji pomiędzy liczbami  i  , tzn. jeden ze znaków: , ,
Przykład
Dane
a := 10
b := 15
Wynik
<"""
a = input().split()
a = int(a[-1])
print("to jest a",a)

b = input().split()
b = int(b[-1])
print("to jest b",b)
if a == b:
    print("=")
elif a<b:
    print("<")
else:
    print(">")
