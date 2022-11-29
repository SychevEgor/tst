user_number = int(input('Введите число: '))
user_list = {i:round((1+1/i)**i, 3) for i in range(1, user_number+1)}
print(user_list)
print(sum(user_list.values()))