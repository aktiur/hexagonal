import heapq
import operator
import string
from functools import reduce

from pyroaring import BitMap


class TrigramIndex:
    ALPHABET = f" {string.ascii_lowercase}"
    B = len(ALPHABET)

    def __init__(self, words=None):
        self.words = {}
        self.trigrams = {}

        if words is not None:
            for word in words:
                self.add(word)

    @classmethod
    def _trigram_index(cls, tri):
        return (
            cls.ALPHABET.index(tri[0])
            + cls.B * cls.ALPHABET.index(tri[1])
            + cls.B ** 2 * cls.ALPHABET.index(tri[2])
        )

    @staticmethod
    def _trigrams(word):
        return [f"{a}{b}{c}" for a, b, c in zip(f"  {word}", f" {word} ", f"{word}  ")]

    def add(self, word):
        trigrams = self._trigrams(word)
        bm = self.words[word] = BitMap()
        for trigram in trigrams:
            i = self._trigram_index(trigram)
            bm.add(i)
            self.trigrams.setdefault(trigram, set()).add(word)

    def search(self, word, n=5):
        trigrams = self._trigrams(word)

        candidates = reduce(
            operator.or_, (self.trigrams.get(trigram, set()) for trigram in trigrams)
        )
        bm = BitMap([self._trigram_index(trigram) for trigram in trigrams])

        heap = []

        for c in candidates:
            score = len(bm & self.words[c]) / min(len(bm), len(self.words[c]))

            if len(heap) < n:
                heap.append((score, c))
                if len(heap) == n:
                    heapq.heapify(heap)
            elif score > heap[0][0]:
                heapq.heapreplace(heap, (score, c))

        return sorted(heap, reverse=True)
