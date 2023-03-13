"""
A sequence of n > 0 integers is called a jolly jumper if the absolute values of the difference between
successive elements take on all the values 1 through n − 1. For instance,
1 4 2 3
is a jolly jumper, because the absolutes differences are 3, 2, and 1 respectively. The definition implies
that any sequence of a single integer is a jolly jumper. You are to write a program to determine whether
or not each of a number of sequences is a jolly jumper.
Input
Each line of input contains an integer n ≤ 3000 followed by n integers representing the sequence.
Output
For each line of input, generate a line of output saying ‘Jolly’ or ‘Not jolly’.
Sample Input
4 1 4 2 3
5 1 4 2 -1 6
Sample Output
Jolly
Not jolly
"""
def unique_digits(num: int) -> bool:
    num_string= str(num)
    num_list = list(num_string) #[el for in num_string]
    num_set = set(num_list)
    return len(num_list) == len(num_set)

    
n = int(input("Podaj liczbę całkowitą: "))
numbers = [int(input("Podaj liczbę całkowitą: ")) for i in range(n)]

diff = []
for el in range(len(numbers) -1):

    diff.append(abs(numbers[el] - numbers[el+1]))

min_value = min(diff) 
max_value = max(diff)
num_set = set(diff)
is_unique = len(diff) == len(num_set)

if min_value ==1 and max_value == n-1 and is_unique ==True:
    print("Tak")
else:
    print("Nie")
