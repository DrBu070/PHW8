
b = [0]
count = int(input('Введите кол-во оценок: '))
b = b*count
for j in range(len(b)):
    num = int(input('Введите оценку: '))
    b[j] = num
print('Все оценки:',b)
for i in range(len(b)):
    if b[i] > 3:
        b[i] = 1
print('Изменённые оценки: ',b)
