import re
import csv


# Вивiд данних з файлу в форматі словника (ключ:значення)
with open('test.csv', 'r', encoding='UTF-8') as file_csv:
    text = csv.DictReader(file_csv, restkey= None, restval=None)
    list_ = []
    for row in text:
        print(row)
        print()
        list_.append(row)



# Сортування за алфавітом по імені та часом по часу входу 
print(sorted(list_, key=lambda x: x['customers_firstname']))
print(sorted(list_, key=lambda x: x['login_time']))




#  Інформація про першого покупця , для перевірки регулярних виразів  
text = ' '.join([f'{key}: {value}' for key, value in list_[0].items()])


id = re.findall("('customers_id:')([0-9])(.*?;)",  text)
name = re.search("^customers_firstname.*;$", text)
