from collections import defaultdict
from itertools import combinations, product
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


def task26() -> Tuple[Tuple[str, str], int]:
    words = set(text1)

    def hamming_distance(pair: Tuple[str, str]) -> int:
        return sum(x != y for (x, y) in zip(*pair))

    # group words by length
    words_by_length: Dict[int, Set[str]] = defaultdict(set)
    for w in words:
        words_by_length[len(w)].add(w)

    max_diameter = 0
    max_pair = ("", "")
    for length, words_set in sorted(
        words_by_length.items(), key=lambda pair: pair[0], reverse=True
    ):
        if length < max_diameter:
            break
        if len(words_set) < 2:
            continue
        max_pair_for_set = max(combinations(words_set, 2), key=hamming_distance)
        max_diameter_for_set = hamming_distance(max_pair_for_set)
        if max_diameter_for_set > max_diameter:
            max_diameter = max_diameter_for_set
            max_pair = max_pair_for_set

    return max_pair, max_diameter


def task27() -> Dict[Tuple[str, str], float]:
    return {(w1, w2): jaccard(set(w1), set(w2)) for w1, w2 in zip(text1, text1[1:])}


def task28() -> Tuple[Tuple[str, str], float]:
    def relative_levenstein(v: str, w: str) -> float:
        return edit_distance(v, w) / (len(v) + len(w))  # type: ignore

    words = set(text2)

    # group words by length
    words_by_length: Dict[int, Set[str]] = defaultdict(set)
    for w in words:
        words_by_length[len(w)].add(w)

    min_distance = 1.0
    min_pair = ("", "")

    for i in sorted(words_by_length.keys(), reverse=True):
        for j in range(i, 1, -1):
            if 1 / (i + j) > min_distance or (i - j) / (i + j) > min_distance:
                continue

            s1 = words_by_length[i]
            s2 = words_by_length[j]
            try:
                new_pair, new_min = min(
                    [
                        ((v, w), relative_levenstein(v, w))
                        for (v, w) in product(s1, s2)
                        if v != w
                    ],
                    key=lambda x: x[1],
                )
                if new_min < min_distance:
                    min_distance = new_min
                    min_pair = new_pair
            except ValueError:  # in case of empty sequence in min
                continue

    return min_pair, min_distance


def task29(b: str, n: int) -> List[str]:
    return [
        "".join(
            [
                f"{int(bit, 2) ^ 1:b}" if index in indices else bit
                for index, bit in enumerate(b)
            ]
        )
        for indices in combinations(range(len(b)), n)
    ]


def task30(s: str, k: int) -> Set[Tuple[str, ...]]:
    words = word_tokenize(s)
    return set(zip(*(words[i:] for i in range(k))))
