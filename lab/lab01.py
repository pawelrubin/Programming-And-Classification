from collections import Counter
from math import sqrt
from random import randint
from typing import Iterable, List, Set, Tuple, TypeVar, Union

Vector = Iterable[float]
T = TypeVar("T")


def dot_product(a: Vector, b: Vector) -> float:
    return sum(a * b for a, b in zip(a, b))


def vector_length(a: Vector) -> float:
    return sqrt(sum(x ** 2 for x in a))


def task01() -> None:
    number = input("Number please: ")

    try:
        print(f"The number is {'even' if int(number) % 2 == 0 else 'odd'}")
    except ValueError:
        print("It's not a number!")


def task02() -> Tuple[float, int]:
    numbers = [randint(10, 99) for _ in range(20)]
    return sum(numbers) / len(numbers), max(numbers)


def task03(a: Vector, b: Vector) -> float:
    return dot_product(a, b) / vector_length(a) * vector_length(b)


def task04(integers: List[int], c: int) -> List[int]:
    return [x for x in integers[1:-1] if x % c == 0]


def task05(x: List[T], y: List[T]) -> List[T]:
    return List(set(x).intersection(set(y)))


def task06(x: str) -> str:
    return x.replace("a", "")


def task07(sentence: str) -> Tuple[int, int]:
    letters, digits = 0, 0

    for c in sentence:
        if c.isalpha():
            letters += 1
        elif c.isdigit():
            digits += 1

    return letters, digits


# task 08
def subsets(xs: List[T]) -> List[List[T]]:
    return subsets(xs[1:]) + [x + [xs[0]] for x in subsets(xs[1:])] if xs else [[]]


def task09(s: str) -> str:
    return Counter(s).most_common(1)[0][0]


def task10(number: str) -> str:
    return f"{int(number):b}"


def task11(xs: List[int]) -> List[int]:
    return [x for x in xs if x >= 0]


def task12(xs: List[str]) -> List[str]:
    return [x for x in xs if len(x) <= 5]


def task13(strings: Set[str]) -> str:
    return max(strings, key=len)


def task14(a: List[T], b: List[T]) -> List[T]:
    return sum(([x, y] for x, y in zip(a, b)), [])


def task15(xs: List[Union[str, int]]) -> List[Union[str, int]]:
    return sorted(filter(lambda x: isinstance(x, str), xs)) + sorted(
        filter(lambda x: isinstance(x, int), xs)
    )
