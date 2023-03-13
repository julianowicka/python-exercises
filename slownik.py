cost = dict()
cost["a"] = 5
cost["l"] = 25

print(cost["a"])

if "m" in cost:
    print(cost["m"])
#instrukcja jak wpisac 
letter, value = input().split()
cost[letter] = int(value)

print(cost)
