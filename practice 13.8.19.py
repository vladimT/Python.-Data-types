tickets = int(input('Введите количечство билетов: \n'))
list_tickets = [i for i in range(1, tickets+1)]

age = [int(input('Введите через Enter возраст для каждого владельца билета: \n')) for j in range(len(list_tickets))]

sum_ = 0 # введем переменную для подсчета стоимости с учетом возраста менее 18 лет

for j in age:
    if j < 18:
        sum_ = sum_
    if 18 <= j <= 25:
        sum_ = sum_ + 990
    if j > 25:
        sum_ = sum_ + 1390

discount = int(0.1 * sum_)

if len(list_tickets) > 3:
    total = sum_ - discount
    print('Итоговая сумам к оплате с учетом скидки (при регистрации более 3-х человек): \n', total, 'руб.')
else:
    print('Итоговая сумам к оплате: \n',sum_, 'руб.')










