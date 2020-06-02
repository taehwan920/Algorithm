l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
lan = a // c if a % c == 0 else a // c + 1
math = b // d if b % d == 0 else b // d + 1
hw = max(lan, math)
result = l - hw
print(result)
