
n=int(input("Введите число:"))

d = 10
s = ""

while n > 0:
    num = n % d
    s = s + str(num)
    n = n // d

print (s)
