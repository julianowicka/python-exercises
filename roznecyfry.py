"""The inhabitants of Nlogonia are very superstitious. One of their beliefs is that street house numbers
that have a repeated digit bring bad luck for the residents. Therefore, they would never live in a house
which has a street number like 838 or 1004.
The Queen of Nlogonia ordered a new seaside avenue to be built, and wants to assign to the new
houses only numbers without repeated digits, to avoid discomfort among her subjects. You have been
appointed by Her Majesty to write a program that, given two integers N and M, determines the
maximum number of houses that can be assigned street numbers between N and M, inclusive, that do
not have repeated digits.

Input
Each test case is described using one line. The line contains two integers N and M, as described above
(1 ≤ N ≤ M ≤ 5000).

Output
For each test case output a line with an integer representing the number of street house numbers
between N and M, inclusive, with no repeated digits.

Sample Input
87 104
989 1022
22 25
1234 1234

Sample Output
14
0
3
1"""


def unique_digits(num: int) -> bool:
    num_string = str(num)
    num_list = list(num_string)  # [el for in num_string]
    num_set = set(num_list)
    return len(num_list) == len(num_set)


a = int(input("Podaj liczbę całkowitą: "))
b = int(input("Podaj liczbę całkowitą: "))

result = 0

for i in range(a, b + 1):
    if unique_digits(i):
        result += 1
print(result)
