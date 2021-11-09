

def num_translate(user_value):
    for k in translator:
        if k == user_value:
            print(translator.get(user_value))
        else:
            print(translator.get(user_value))



translator = {'one':'один', 'two':'два', 'tree':'три', 'four':'четыре', 'five':'пять', 'six':'шесть', 'seven':'семь', 'eight':'восемь', 'nine':'девять', 'ten':'десять'}
a = input("Please enter a number in English: ")
num_translate(a)

# Не могу понять почему в консоли возвращает значение не 1 раз, а много?