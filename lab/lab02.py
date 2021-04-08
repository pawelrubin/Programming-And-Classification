from typing import List, Set

from nltk.book import text1, text2, text3, text4, text5, text6, text7, text8, text9
from nltk.tokenize.punkt import PunktLanguageVars, PunktSentenceTokenizer

from lab03 import TEXTS

TEXTS = [text1, text2, text3, text4, text5, text6, text7, text8, text9]


def task16() -> None:
    USERS = {
        "Joe": "White House",
        "Młody G": "Gdynia",
        "G.R. Emlin": "localhost",
        "Bilbo Baggins": "Shire",
    }
    print(dict(sorted(USERS.items(), key=lambda item: item[1])))


def task17() -> int:
    return text6.count("knight")


def task18() -> Set[str]:
    return set(text6) - set(text7)


def task19() -> Set[str]:
    return set.intersection(*(set(t) for t in TEXTS))


def task20() -> str:
    lang_vars_class = PunktLanguageVars
    lang_vars_class.sent_end_chars = PunktLanguageVars.sent_end_chars + (".--", "?--")
    tokenizer = PunktSentenceTokenizer(lang_vars=lang_vars_class())
    sentences: List[str] = tokenizer.sentences_from_tokens(text2)
    return max(sentences, key=len)
