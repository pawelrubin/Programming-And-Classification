from hashlib import sha1
from itertools import combinations
from lab.lab03 import jaccard
from random import getrandbits
from struct import calcsize
from typing import Dict, List, Set, Tuple

from nltk.book import text1, text2, text3

INT_SIZE = 8 * calcsize("P")


def task31(n: int) -> Tuple[str, str]:
    return min(
        combinations((f"{getrandbits(100):b}".zfill(100) for _ in range(n)), 2),
        key=lambda vw: sha1("".join(vw).encode()).hexdigest(),
    )


def task32(k: int = 1000) -> Dict[Tuple[str, str], float]:
    texts = (text1, text2, text3)
    sets = (set(w for w in t if len(w) < 8) for t in texts)

    masks = [getrandbits(INT_SIZE) for _ in range(k)]

    def signature(s: Set[str]) -> List[int]:
        return [min(hash(w) ^ masks[i] for w in s) for i in range(k)]

    def estimate_jaccard(sign_a: List[int], sign_b: List[int]) -> float:
        return sum(i == j for i, j in zip(sign_a, sign_b)) / k

    signatures = [signature(s) for s in sets]
    estimates = [
        estimate_jaccard(sign_a, sign_b)
        for (sign_a, sign_b) in combinations(signatures, 2)
    ]

    return {
        (a.name, b.name): estimate
        for ((a, b), estimate) in zip(combinations(texts, 2), estimates)
    }


def task33() -> Dict[Tuple[str, str], float]:
    texts = (text1, text2, text3)
    sets = (set(w for w in t if len(w) < 8) for t in texts)
    return {
        (a.name, b.name): jaccard(sa, sb)
        for (a, b), (sa, sb) in zip(
            combinations(texts, 2),
            combinations(sets, 2),
        )
    }
