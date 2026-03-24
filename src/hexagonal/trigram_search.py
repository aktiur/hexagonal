import heapq
import operator
import string
from functools import reduce
from typing import Iterable, NewType, Tuple

from pyroaring import BitMap

Trigram = NewType("Trigram", str)


class TrigramIndex[T]:
    ALPHABET = f" {string.ascii_lowercase}{string.digits}"
    B = len(ALPHABET)

    def __init__(self, words: Iterable[Tuple[str, T]] | None = None):
        self.direct_index: dict[str, BitMap] = {}
        self.inverted_index: dict[Trigram, set[str]] = {}
        self.metadata: dict[str, T] = {}

        if words is not None:
            for word, metadata in words:
                self.add(word, metadata)

    @classmethod
    def _trigram_number(cls, tri: Trigram):
        return (
            cls.ALPHABET.index(tri[0])
            + cls.B * cls.ALPHABET.index(tri[1])
            + cls.B**2 * cls.ALPHABET.index(tri[2])
        )

    @staticmethod
    def _trigrams(word):
        return [
            Trigram(f"{a}{b}{c}")
            for a, b, c in zip(f"  {word}", f" {word} ", f"{word}  ", strict=True)
        ]

    def add(self, word: str, metadata: T):
        trigrams = self._trigrams(word)
        bm = self.direct_index[word] = BitMap()

        if metadata is not None:
            self.metadata[word] = metadata

        for trigram in trigrams:
            i = self._trigram_number(trigram)
            bm.add(i)
            self.inverted_index.setdefault(trigram, set()).add(word)

    def search(self, word, n=1) -> list[Tuple[float, T]]:
        trigrams = self._trigrams(word)

        candidates = reduce(
            operator.or_,
            (self.inverted_index.get(trigram, set()) for trigram in trigrams),
        )
        bm = BitMap([self._trigram_number(trigram) for trigram in trigrams])

        heap: list[Tuple[float, T]] = []

        for c in candidates:
            score = len(bm & self.direct_index[c]) / min(
                len(bm), len(self.direct_index[c])
            )
            m = self.metadata[c]

            if len(heap) < n:
                heap.append((score, m))
                if len(heap) == n:
                    heapq.heapify(heap)
            elif score > heap[0][0]:
                heapq.heapreplace(heap, (score, m))

        return sorted(heap, reverse=True)
