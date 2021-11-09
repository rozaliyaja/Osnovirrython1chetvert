def thesaurus(user_value):
    user_value = a.split(' ')
    user_value.sort()
    letter_name = {}
    for element in user_value:
        name = element[0]
        first_let = name[0]
        if not first_let in letter_name:
            new_list = [element]
            letter_name[first_let] = new_list
        elif first_let in letter_name:
            letter_name.get(first_let).append(element)
    print(letter_name)

a = input('Введите имена сотрудников через пробел: ')
thesaurus(a)