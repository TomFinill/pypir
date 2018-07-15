from pypir.poly_int_pir import IReplica, chi
from pypir.pir import IDatabase
from typing import Sequence
from pyfinite import FElement
from operator import mul

class Replica(IReplica):

	def __init__(self, db: IDatabase) -> None:
		self.db = db

	def __call__(self, g: Sequence[FElement]) -> FElement:
		return sum(self._h(g, j) * x_j for j, x_j in enumerate(self.db))

	@staticmethod
	def _h(g: Sequence[FElement], j: int) -> FElement:
		return reduce(mul, (_f(g, j, l) for l in len(g)), 1)

	@staticmethod
	def _f(g: Sequence[FElement], j: int, l: int) -> FElement:
		chi_j_l = chi(j)(l)
		return chi_j_l * g[l] + (1 - chi_j_l) * (1 - g[l])

	@classmethod
	def create_required(cls, db: IDatabase) -> Sequence[IReplica]:
		s = math.ciel(math.log(len(db), 2))
		db.pad((2 ** s) - len(db))
		return [cls(db) for _ in range s + 1]

