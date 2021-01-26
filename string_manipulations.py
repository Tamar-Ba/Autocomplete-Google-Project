import string
import re


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def clean_data(sentence):
    re.sub('[^A-Za-z0-9]+', '', sentence)
    return sentence.lower().lstrip()


def clear_text(txt):
    exclude = set(string.punctuation + '•' + '◆' + '“')
    txt = ''.join(ch for ch in txt if ch not in exclude)
    return txt.lower()
