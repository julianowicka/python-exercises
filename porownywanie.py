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
