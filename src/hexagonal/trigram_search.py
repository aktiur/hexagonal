import heapq
import operator
import string
from functools import reduce
from typing import Iterable, NewType, Tuple

from pyroaring import BitMap

Trigram = NewType("Trigram", str)


DEFAULT_ALPHABET = f" {string.ascii_lowercase}{string.digits}"


class TrigramIndex[T]:
    def __init__(
        self,
        words: Iterable[Tuple[str, T]] | None = None,
        *,
        alphabet=DEFAULT_ALPHABET,
        empty_character=" ",
    ):
        self._alphabet = alphabet
        self._empty_character = empty_character

        assert len(alphabet) ** 4 < 2**32, "Alphabet too large"

        self._direct_index: dict[str, BitMap] = {}
        self._inverted_index: dict[Trigram, set[str]] = {}
        self._metadata: dict[str, T] = {}

        if words is not None:
            for word, metadata in words:
                self.add(word, metadata)

    def _trigram_number(self, tri: Trigram):
        alphabet = self._alphabet
        b = len(alphabet)
        return (
            alphabet.index(tri[0])
            + b * alphabet.index(tri[1])
            + b**2 * alphabet.index(tri[2])
        )

    def _trigrams(self, word):
        e = self._empty_character
        return [
            Trigram(f"{a}{b}{c}")
            for a, b, c in zip(
                f"{e}{e}{word}", f"{e}{word}{e}", f"{word}{e}{e}", strict=True
            )
        ]

    def add(self, word: str, metadata: T):
        trigrams = self._trigrams(word)
        bm = self._direct_index[word] = BitMap()

        if metadata is not None:
            self._metadata[word] = metadata

        for trigram in trigrams:
            i = self._trigram_number(trigram)
            bm.add(i)
            self._inverted_index.setdefault(trigram, set()).add(word)

    def search(self, word, n=1) -> list[Tuple[float, T]]:
        trigrams = self._trigrams(word)

        candidates = reduce(
            operator.or_,
            (self._inverted_index.get(trigram, set()) for trigram in trigrams),
        )
        bm = BitMap([self._trigram_number(trigram) for trigram in trigrams])

        heap: list[Tuple[float, T]] = []

        for c in candidates:
            score = len(bm & self._direct_index[c]) / min(
                len(bm), len(self._direct_index[c])
            )
            m = self._metadata[c]

            if len(heap) < n:
                heap.append((score, m))
                if len(heap) == n:
                    heapq.heapify(heap)
            elif score > heap[0][0]:
                heapq.heapreplace(heap, (score, m))

        return sorted(heap, reverse=True)
