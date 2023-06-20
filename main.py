count = int(input("Введите количество арбузов: "))
first_weight = int(input("Введите вес арбуза: "))
minn = first_weight
maxx = first_weight

for i in range(count - 1):
    weight = int(input("Введите вес арбуза: "))
    if weight < minn:
        minn = weight
    if weight > maxx:
        maxx = weight
print(minn, maxx)
