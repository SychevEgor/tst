user_number = int(input('Введите число: '))
user_list = list()
result = 1
for i in range(1,user_number+1):
    result *= i
    user_list.append(result)

print(user_list)

