from itertools import combinations
from typing import Dict, List, Set, Tuple, TypeVar

from nltk.book import text1, text2, text3, text4, text5, text6, text7, text8, text9
from nltk.metrics import edit_distance
from nltk.tokenize import word_tokenize

T = TypeVar("T")
TEXTS = [text1, text2, text3, text4, text5, text6, text7, text8, text9]


def task21(b: str) -> List[str]:
    return [f"{int(b, 2) ^ (1 << i):b}".zfill(len(b)) for i in range(len(b))]


# task 22
def jaccard(a: Set[T], b: Set[T]) -> float:
    return 0 if a.isdisjoint(b) else len(a & b) / len(a | b)


def task23(a: str, b: str) -> float:
    return jaccard(set(word_tokenize(a)), set(word_tokenize(b)))


def task24() -> List[str]:
    return [word for word in text1 if len(word) < 7 and edit_distance(word, "dog") < 4]


def task25() -> List[Tuple[str, float]]:
    return [
        (f"{t1.name} and {t2.name}", jaccard(set(t1), set(t2)))
        for t1, t2 in combinations(TEXTS, 2)
    ]


def task26() -> float:
    pass


def task27() -> Dict[Tuple[str, str], float]:
    return {(w1, w2): jaccard(set(w1), set(w2)) for w1, w2 in zip(text1, text1[1:])}


def task28() -> Tuple[str, str]:
    # TODO: optimize
    def relative_levenstein(v: str, w: str) -> float:
        return edit_distance(v, w) / (len(v) + len(w))

    return min(
        ((v, w) for v, w in combinations(text2, 2) if len(v) == len(w)),
        key=lambda vw: relative_levenstein(vw[0], vw[1]),
    )


def task29(b: str, n: int) -> List[str]:
    pass


def task30(s: str, k: int) -> Set[Tuple[str, ...]]:
    words = word_tokenize(s)
    return set(zip(*(words[i:] for i in range(k))))
