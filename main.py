from pprint import pprint
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ

header = contacts_list[0]
contacts_list_clean = [header]

for item in contacts_list[1:]:
    if item[0] != '' and item[1] != '' and item[2] != '':
        contacts_list_clean.append(item)
    else:
        full_name = ' '.join(item[0:3]).strip()
        rest_of_item = item[3:]

        full_name_divided = re.split('\s+', full_name)

# добавляем пустую строку в поле surname, если отчества нет
        if len(full_name_divided) == 3:
            pass
        else:
            full_name_divided.append('')

        full_raw = full_name_divided + rest_of_item

        contacts_list_clean.append(full_raw)


for item in contacts_list_clean:
    
    phone_pattern = '(\+7|8)(\s*)(\(?)(\d{3})(\)?)(\s*)(\-*)(\d{3})(-*)(\d{2})(-*)(\d{2})(\s*)(\(?)(\s?(доб)?)(\.?)(\s*)(\d*)(\)?)'
    find_phone = re.findall(phone_pattern, item[5])
    clean_phone = re.sub(phone_pattern, r'+7(\4)\8-\10-\12\13\15\17\19', item[5])

    item[5] = clean_phone


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list_clean)
