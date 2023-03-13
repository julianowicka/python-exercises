"""
tekst wielolinijkowy
"""
#def compute_sum(numbers: list)oczekiwany typ) - > int:

from typing import List, Tuple
#sposób na importowanie konkretych rzeczy z danego modułu bilioteki

def compute_sum(numbers: List[int]) -> int:
    sum = 0
    # for i in range(numbers)
    #    sum += numbers[i]
    for el in numbers:
        sum += el
    return sum

def min_max(numbers: list) -> Tuple [int, int]:
    min = numbers[0]
    max = numbers[0]
    for el in numbers:
        if el > max:
            max = el
        if el < min:
            min = el
    return min, max
#przekazanie przez referencje albo przez wartosc
# sortowanie bąbelkowe
def sort_ascending(numbers):
    for a in range(len(numbers)):
        for b in range(len(numbers)-1):
            if numbers[b]>numbers[b+1]:
                numbers[b],numbers[b+1] = numbers[b+1], numbers[b]

#krotka wartosci lst = [ 2, 5] lista dwóch wartości którą możemy modyfikować a krotka tup = (2.5) służy do przechowywania wartośći jest immutable
#lst[0] == 2 tup[0] == 2
# komentarz
n = 5
print(type(n))

n = 5.4
print(type(n))

n = "hello"
print(type(n))
# domyślnie input wczyta string
n = int(input("Podaj liczbę naturalną: "))
print(type(n))

numbers = [ 10 ] # pusta lista []
#długość listy len 
print(numbers)
#print(len(numbers))

for i in range(n): # dwukropkek zamiast nawiasow klamrowych, kolejną istrukcje zapisujemy bez wcięcia poza pętla
    #wciecia tab lub spacja - należy wybrać konsekwentnie
    num = int(input("Podaj kolejna lizcbe: "))
    # range 10 -> 0,10 to to samo co range 0, 10 
    numbers.append(num)

print("lista:", numbers) 

#sum
result_sum = compute_sum(numbers)

result_avg = result_sum / n
# print(f"") nie ma roznicy miedzy pojedynczym a podwojnym cudzyslowiem
print(f"Suma: {numbers}\nŚrednia: {result_avg}")

# min maks
result_min, result_max = min_max(numbers)
#wartosci po lewej nie wieksze niz w prawej stronie w krotce
print(f"Minimum: {numbers}\nMinimum: {result_max}")
print(f"Maksimum: {numbers}\nMaksimum: {result_max}")

sort_ascending(numbers)
print(numbers)