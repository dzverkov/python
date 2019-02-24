
n=int(input("Введите число:"))

d=10
even=0
odd=0

while n > 0:
    num = n % d
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    n = n // d

print (f"Чётных чисел:{even}")
print (f"Нечётных чисел:{odd}")