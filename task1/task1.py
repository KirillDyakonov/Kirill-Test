
n = int(input("Введите n: "))
m = int(input("Введите m: "))

arr = list(range(1, n + 1))

index = 0
path = []

while True:
    path.append(arr[index])
    index = (index + m-1) % n

    if index == 0:
        break

print(''.join(map(str, path)))
