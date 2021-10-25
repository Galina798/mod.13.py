# Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов.
# Программа должна работать следующим образом:
# 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
# 2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:
# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# 3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует
# больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.
# Для проверки загрузите полученное решение на GitHub и прикрепите ссылку.

tikets = int(input("Введите количество билетов: ")) # вводим количество билетов
old = list(map(int,[input("Введите возраст посетителя: ") for i in range(tikets)])) #cоздаем список для ввода возраста посетителя

price = [] # создаем список для редактирования цен в зависимости от возраста посетителя
for i in old:          # устанавливаем стоимость билетов в зависимости от возраста посетителя
    if i<18:
        price.append (0)
    elif 18<=i<25:
        price.append (990)
    else:
        price.append (1390)

sum_price = sum(price)   # считаем итоговую стоимость билетов без учета скидки
if tikets >3:
    sum_price = sum_price*0.9  #считаем итоговую сумму с учетом скидки
print ("Cумма к оплате: ", int(sum_price))         #вывод суммы

