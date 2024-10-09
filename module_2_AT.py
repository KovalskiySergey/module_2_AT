import random
def generete_number():
    number1 = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    number2 = random.choice(number1)
    return number2
def generate_password(n):
    result = ""
    for i in range(1, n):
        for j in range(i+1, n+1):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += f'{i}{j}'
    return result
m = generete_number()
print('Введите число во вторую вставку: ', m)
n = int(input ('Введите число из первой вставки: '))
if m == n:
    password = generate_password(n)
    print(f'Нужный пароль:  {password}')
else:
    print('Вы съедены туземцами!!! ')



