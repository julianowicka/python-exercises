n = int(input("Podaj liczbę naturalną: "))
# listy tworzymy spłaczając działanie pętli
#szybsze i wydajniejsze:
numbers = [int(input("Podaj liczbę naturalną: ")) for i in range(n)]
#[i for i in range(n)]

result_sum = sum(numbers)
result_avg = result_sum / n
result_min = min(numbers)
result_max = max(numbers)

print(f"Suma: {numbers}\nŚrednia: {result_avg}")
print(f"Minimum: {numbers}\nMaksimum: {result_max}")

numbers_ascending = sorted(numbers)
# numbers.sort()
numbers_descending = sorted(numbers, reverse=True)

print(f"Posortowana rosnąco: { numbers_ascending}")
print(f"Posortowana malejąco: { numbers_descending}")