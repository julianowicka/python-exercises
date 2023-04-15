'''Czy dodawanie, odejmowanie i mnożenie może sprawiać kłopoty? Oczywiście że nie! Dlatego
   mam dla ciebie proste zadanie: dla podanego w specjalnym zapisie wyrażenia arytmetycznego
   oblicz jego wartość! Specjalność tego zapisu polega na tym, że najpierw zawsze pojawiają się
   argumenty, a dopiero później działania M, O lub D (mnożenie, odejmowanie lub dodawanie).
   W wyrażeniu tym jednak nie musisz się martwić kolejnością działań arytmetycznych – po
   prostu wykonuj je zgodnie z wejściem!
   Wejście
   W pierwszym wierszu wejścia znajduje się jedna liczba N (1 ≤ N ≤ 10) – liczba wyrażeń do
   rozpatrzenia. W kolejnych N liniach znajdują się krótkie wyrażenia arytmetyczne. Długość
   żadnego z nich nie przekracza 1000 znaków. Wyrażenia składają się wyłącznie z wartości xi
   (0 ≤ xi ≤ 1015) oraz działań opisanych odpowiednimi literami.
   Wyjście
   W oddzielnych liniach należy wypisać N liczb całkowitych – wyniki obliczeń. Możesz założyć,
   że końcowy wynik nigdy nie przekroczy |10^15|. '''

def readTable():
    line = input().strip()
    string_numbers = line.split(' ')
    number_numbers = []
    for number in string_numbers:
        number_numbers.append(number)
    return number_numbers

n = int(input().strip())
for i in range(n):
    line = readTable()
    stack = []
    for j in line:
        if j != 'O' and j!="D" and j!="M":
            stack.append(j)
        else:
            if j == "O":
                element1 = int(stack.pop())
                element2 = int(stack.pop())
                result = element2 - element1
                stack.append(result)
            if j == "D":
                element1 = int(stack.pop())
                element2 = int(stack.pop())
                result = element1 + element2
                stack.append(result)
            if j == "M":
                element1 = int(stack.pop())
                element2 = int(stack.pop())
                result = element1 * element2
                stack.append(result)
    print(stack[0])
