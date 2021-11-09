

def get_jokes(user_value):
    nouns = [ "автомобиль", "лес", "огонь","город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    from random import choices
    joke = []
    while len(joke) != user_value:
        """returns the number of jokes entered by the user as a list of str"""
        for element in nouns:
            first_words = choices(nouns)
            joke_start = first_words
        for element in adverbs:
            sec_words = choices(adverbs)
            joke_start = first_words + sec_words
        for element in adjectives:
            third_words = choices(adjectives)
            joke_start = first_words + sec_words + third_words
            my_joke = ' '.join(joke_start)
        joke.append(my_joke)
    return (joke)

    # print(joke)



a = int(input('Введите '))
get_jokes(a)



