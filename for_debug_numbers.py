import textwrap
from datetime import datetime
from decimal import Decimal

# goods 1 section
item_1_title = input('Введіть назву першого товару: ')[:20]
item_1_quantity = Decimal(input('Введіть бажаєму кількість першого товару: '))
item_1_price = Decimal(input('Введіть ціну першого товару: '))

# goods 2 section
item_2_title = input('Введіть назву другого товару: ')[:20]
item_2_quantity = Decimal(input('Введіть бажаєму кількість другого товару: '))
item_2_price = Decimal(input('Введіть ціну другого товару: '))

item_1_total_cost = item_1_quantity * item_1_price
item_1_total_cost_right_format = item_1_total_cost.quantize(Decimal('1.00'))

item_2_total_cost = item_2_quantity * item_2_price
item_2_total_cost_right_format = item_2_total_cost.quantize(Decimal('1.00'))

total_quantity = item_1_quantity + item_2_quantity
total_cost = item_1_total_cost + item_2_total_cost
total_cost_right_format = total_cost.quantize(Decimal('1.00'))


# printing receipt
print('\n\n\n')
print('фіскальний чек'.capitalize().center(80, '~'))
print('магазин "все для дому"'.upper().center(80))
print(f'{"Товар":<20} {"Кількість":<15} {"Ціна":<10} {"Вартість":<15}') # Використання f-string для вирівнювання

print(f'{item_1_title:<20} {item_1_quantity:<15} {item_1_price:<10} {item_1_total_cost_right_format:<15}')
print(f'{item_2_title:<20} {item_2_quantity:<15} {item_2_price:<10} {item_2_total_cost_right_format:<15}')
print('~' * 80)
print(f'{"ВСЬОГО":<20} {total_quantity:<15} {"x":<10} {total_cost_right_format:<15}')
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S').rjust(80))
print('\n\n')