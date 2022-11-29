uNum = input('Введите число: ')

def sum_num(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum
print(sum_num(uNum))