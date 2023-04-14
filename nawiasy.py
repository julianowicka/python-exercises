'''
Dany jest ciąg złożony z nawiasów okrągłych () oraz kwadratowych []. Twoim celem jest sprawdzenie, czy ciąg zawiera poprawne nawiasowanie, czy też nie. Ciąg uznajemy za poprawny, gdy:
jest pustym ciągiem,
jeżeli a i b są poprawne, to ab także jest poprawne,
jeżeli a jest poprawne, to (a) oraz [a] także są poprawne.
'''

def is_ok(bracket1, bracket2):
    return (bracket1 == '[' and bracket2 == ']') or (bracket1 == '(' and bracket2 == ')')
brackets = (input("podaj nawiasy"))
print(brackets)
def is_bracket_correct():
    stack = []
    for i in range(len(brackets)):
        value = brackets[i]
        if value == '(' or value == '[':
            stack.append(value)
        else:
            if len(stack) == 0:
                return False
            last_element = stack.pop()
            if not is_ok(last_element, value):
                return False

    return True


is_correct = is_bracket_correct()

if is_correct:
    print("correct")
else:
    print("not correct")
