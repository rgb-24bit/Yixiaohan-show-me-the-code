# -*- coding: utf-8 -*-


def get_filtered_words(file_name='filtered_words.txt'):
    with open(file_name, 'r', encoding='utf-8') as fp:
        filtered_words = [word.strip() for word in fp]
    return filtered_words


def get_user_input():
    return input('Input: ')


def prog_output(user_input, filtered_words):
    for word in filtered_words:
        user_input = user_input.replace(word, '*' * len(word))
    print(user_input)


if __name__ == '__main__':
    filtered_words = get_filtered_words()
    prog_output(get_user_input(), filtered_words)
