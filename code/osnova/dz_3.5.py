from random import choice, randrange

nouns = ['аэропорт', 'дерево', 'вода', 'дверь', 'телефон']
adverbs = ['вечером', 'когда-то', 'вчера', 'сверху', 'много', 'весело', 'вперед', 'вдалеке']
adjectives = ['грустный', 'синий', 'твердый', 'страшный', 'бессмысленный']


def jokes(p, repeat=False):
    """
    Функция возвращает случайные шутки, собранные из трех списков слов
    :param p: колличество шуток
    :param repeat: уникальные/неуникальные
    :return: список случайных шуток
    """
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    list_jokes = []
    list_min = min(no, adv, adj)

    while p and len(list_min):
        word = randrange(len(list_min))
        if repeat:
            list_jokes.append(f'{no.pop(word)} {adv.pop(word)} {adj.pop(word)}')
        else:
            list_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        p -= 1
    return list_jokes


print(jokes(8, True))
