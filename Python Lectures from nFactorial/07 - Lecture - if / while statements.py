# Date 2025-08-16

n = int(input())

count = 0
while count < n:
    print("Счет: ", count)
    count += 1


n = int(input())

count = 0
print("Счет: ", end = "")
while count < n:
    print(count, end = " ")
    count += 1


n = int(input())

count = 0
print("Счет: ", end = "")
while count < n:
    print(count)
    count += 1



i = 0
while True:
    if i > 15:
        break
    print("Этот цикл бесконечен", i)
    i += 1


i = int(input())

i = 0
while i <= n:
    if i % 2 == 0:  # 'i' even
        print(i, end = " ")
    i += 1



n = int(input())

i = 0
while i <= n:
    print(i, end = " ")
    i += 2



n = int(input())
while i <= n:
    print(i, end = " ")
    i += 3


n = int(input())

i = n
while i >= 0:
    print(i, end = " ")
    i -= 1



a = int(input())
b = int(input())

result = 1
i = 0
while i < b:
    result *= a
    i += 1
print(result)


a = int(input())
b = int(input())

result = 1
i = 0
while i < abs(b):
    result *= a
    i += 1
print(result if b >= 0 else (1 / result))



