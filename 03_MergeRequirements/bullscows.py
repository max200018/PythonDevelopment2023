import sys
from random import choice
from urllib.request import urlopen


def bullscows(guess, secret):
    cows = len(set(secret).intersection(guess))
    bulls = len([i for i in range(len(guess)) if guess[i] == secret[i]])

    return bulls, cows


def ask(string, words=None):
    while print(string) is None:
        if (guess := input()) and (not words or guess in words):
            return guess


def inform(string, b, c):
    print(string.format(b, c))


def gameplay(ask=ask, inform=inform, words=[]):
    secret = choice(words)
    tryes = 0
    while True:
        tryes += 1
        b, c = bullscows(ask('Введите слово: ', words), secret)
        inform('Быки: {},  Коровы: {}', b, c)
        if b == len(secret):
            return tryes


def download_dic(url):
    try:
        req = urlopen(url)
        data = req.readlines()
        return [d.decode().rstrip().lstrip() for d in data]
    except Exception as msg:
        print(f'While downloading words from {url} error occured:{msg}')
        return None


def get_words(path):
    try:
        with open(path) as f:
            words = f.readlines()
            return [word.rstrip().lstrip() for word in words]
    except FileNotFoundError:
        if (words := download_dic(path)):
            return words
        else:
            print('Could not find words for you:no file or correct url', file=sys.stderr)
            return None


if __name__ == '__main__':
    path = sys.argv[1]
    length = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    words = [word for word in get_words(path) if len(word) == length]
    gameplay(words=words)
