
# Cписок ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Если целое число- добавить с обеих сторон ккавычки
# Если градусы тоже кавычки и до 2х знаков дополнить 0

message = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_message = []
for element in message:
    if element.isalpha(): # Если буквы- добавляем в новый список
        new_message.append(element)
    elif not element.isdigit() and not element.isalpha(): # Если не буква и не целое число
        index = message.index(element)
        new_message.insert(index,'"') # добавить кавычки до градусов
        new_message.append(element)
        index_2 =  message.index(element) + 2
        new_message.insert(index_2, '"') # добавить кавычки после градусов
        temperature = element.zfill(3) # дополнить это число нулём до двух целочисленных разрядов
    else:
        time_index = message.index(element)
        new_message.insert(time_index, '"')
        new_message.append(element)
    result = ' '.join(new_message)
print(result)