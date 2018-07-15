from pypir.pir import IDatabase
from typing import Sequence

class ArrayDB(IDatabase):
	def __init__(self, data: Sequence[int]) -> None:
		self.data = data

	def __getitem__(self, id: int):
		return self.data[id]

	def __iter__(self):
		return iter(self.data)

    def __len__(self) -> int:
    	return len(self.data)

    def pad(self, padding: int) -> None:
    	self.data.extend([0 for _ in range(padding)])