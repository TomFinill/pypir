from pypir.pir import IPIR
from abc import ABC, abstractmethod
from typing import Collection, Callable, Sequence, Generator
from random import choice
from itertools import islice
from pyfinite import FField, FElement


class IReplica(ABC):
    @abstractmethod
    def __call__(self, *g):
        pass


def chi(j: int) -> Callable[[int], int]:
    return lambda l: int(bin(j)[2:][l])


class PIR(IPIR):
    def __init__(
            self, field: FField, replicas: Collection[IReplica]
    ) -> None:
        self.field = field
        self.replicas = replicas
        self._s = len(self._replicas) - 1
        self._r = [self.field.GetRandomElement() for _ in range(self._s)]
        self._p = [*range(1, self._s + 2)]

    def __call__(self, id: int) -> int:
        for replica, g in zip(self.replicas, self.build_g()):
            replica(*g)

    def _g(self, id: int, r: int, z: FElement) -> FElement:
        return self._r[l] * z + chi(id)(l)

    def build_g(self, id: int) -> Generator[Sequence[FElement]]
        for z in self._p:
            yield tuple(self._g(id, l, z) for l in range(self._s))
