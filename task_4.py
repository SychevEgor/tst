user_number = int(input('Введите число: '))
user_list = [i for i in range(-user_number, user_number+1)]
sum = 1
with open('data') as data:
    indexs = list(map(int, data.readlines()))
for i in range(len(indexs)):
        sum *= user_list[indexs[i]]
print(user_list)
print(sum)