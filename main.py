shopping_list_items = []
unit_prices = []
item_list = []
final_print = []
num_of_items = []
items_to_buy = []
items_brought = []
item_names = []
store_data_list = []
shopping_list = open('shopping.txt', 'r')
store_data = open('input_data.txt', 'r+')
item_overflow = {}
store_dictionary = {}
items_dict = {}
total_price = 0
list_index = 0
flex_sentinel = 0
flex_sentinel_2 = 0
final_string = ''
city = ''
store = ''

for item in store_data:  # retrieves the data from input_data.txt and stores it in a dictionary
    store_data_list.append(item)

    if flex_sentinel_2 == 0:

        if item == 'Store detail:\n':
            continue

        if store == '':
            store = item[:-1]
            flex_sentinel = 1
            continue

        if flex_sentinel == 1:
            city = item[:-1]
            store_dictionary[store] = item[:-1]
            flex_sentinel = 0
            continue

        flex_sentinel_2 = 1

    if flex_sentinel_2 == 1:
        if item == '\n':
            for shopping_item in item_list:
                shopping_item = shopping_item[:-1]
                item_list[list_index] = shopping_item.split(',')
                list_index += 1
            store_dictionary[city] = item_list
            store = ''
            flex_sentinel = 0
            flex_sentinel_2 = 0
            list_index = 0
            item_list = []
            continue
        else:
            item_list.append(item)

for shopping_item in item_list:  # buffer so input_data.txt does not require 2 empty lines below it
    shopping_item = shopping_item[:-1]
    item_list[list_index] = shopping_item.split(',')
    list_index += 1
store_dictionary[city] = item_list
flex_sentinel = 0
flex_sentinel_2 = 0
list_index = 0

for item in shopping_list:  # retrieves data from shopping.txt and puts it into a list
    if 'LIST' in item.upper():
        continue

    else:
        item = item.replace('\n', '')
        shopping_list_items.append(item.split())
        item_names.append(shopping_list_items[list_index][1])
        list_index += 1

list_index = 0

for keys, values in store_dictionary.items():  # takes all instances of the items to purchase from store_dictionary and stores their prices within a list
    if isinstance(values, list):
        for grocery in values:
            for item in shopping_list_items:
                if grocery[0] in item:
                    items_to_buy.append(grocery)
                    items_to_buy.sort()

for item in items_to_buy:  # organizes stock and value into a dictionary

    if item[2][-2] == '.':
        item[2] += '0'

    if not item[0] == flex_sentinel:
        flex_sentinel = item[0]
        item_overflow[item[0]] = [[item[2], item[1]]]
    else:
        item_overflow[item[0]].append([item[2], item[1]])

for key, values in item_overflow.items():
    if isinstance(values, list):
        item_overflow[key].sort()

for item in items_to_buy:  # formats the prices into a dictionary where all the prices are in a list
    if flex_sentinel == item[0]:
        items_dict[item[0]].append(item[2])
        continue

    else:
        flex_sentinel = item[0]
        items_dict[item[0]] = [item[2]]
        continue

flex_sentinel = 0

for item in shopping_list_items:  # formats the amount of a product to buy and the product to buy
    final_print.append(item[0] + ' ' + item[1])

for item in shopping_list_items:  # adds the amount of items to a list
    num_of_items.append(item[0])

for item in final_print:  # adds the minimum price while taking the current stock into account
    for keys, values in item_overflow.items():
        if keys in item:
            for value in values:
                value[0] = value[0][1:]
                if int(num_of_items[list_index]) - flex_sentinel_2 > int(value[1]):
                    flex_sentinel += int(value[1]) * float(value[0])
                    flex_sentinel_2 += int(value[1])
                    value[1] = 0
                    items_brought.append(f'{item_names[list_index]},{value[1]},${value[0]}\n')

                elif int(num_of_items[list_index]) - flex_sentinel_2 == 0:
                    continue

                else:
                    flex_sentinel += (int(num_of_items[list_index]) - flex_sentinel_2) * float(value[0])
                    value[1] = int(value[1]) - (int(num_of_items[list_index]) - flex_sentinel_2)
                    flex_sentinel_2 += int(num_of_items[list_index]) - flex_sentinel_2
                    items_brought.append(f'{item_names[list_index]},{value[1]},${value[0]}\n')

    unit_prices.append(flex_sentinel)
    flex_sentinel = 0
    flex_sentinel_2 = 0
    list_index += 1

list_index = 0

for item in final_print:  # text formatting to position the price exactly 30 chars from the left
    final_print[list_index] += ' @'
    while len(final_print[list_index]) < 30:
        final_print[list_index] += ' '
    list_index += 1

list_index = 0

for item in unit_prices:  # removes the dollar sign from the unit prices
    item = str(item)
    unit_prices[list_index] = item.replace('$', '')
    list_index += 1

list_index = 0

for item in final_print:  # additional text formatting, as well as multiplying the unit prices by the num of items
    flex_sentinel = unit_prices[list_index]
    item = item + '$' + f'{str(round(float(flex_sentinel), 2))}'
    if item[-2] == '.':
        item += '0'
    final_print[list_index] = item
    final_string += item + '\n'
    list_index += 1

flex_sentinel = ''
list_index = 0

for item in unit_prices:  # calculating the total price
    total_price += float(unit_prices[list_index])
    list_index += 1

store_data_list[-1] += '\n'

for item in items_brought:
    item = item.split(',')
    for line in store_data_list:
        if item[0] in line:
            if item[2] in line:
                store_data_list[store_data_list.index(line)] = ','.join(item)

final_string = 'Order Details:\n' + final_string + f'Total                         ${round(total_price, 2)}\n'

print(final_string)
for item in store_data_list:
    item = item.replace('\n', '')
    print(item)