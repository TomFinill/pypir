from abc import ABC, abstractmethod
from typing import Iterator


class IDatabase(ABC):

    @abstractmethod
    def __getitem__(self, id: int) -> int:
        pass

    @abstractmethod
    def __iter__(self) -> Iterator:
    	pass

    @abstractmethod
    def __len__(self) -> int:
    	pass

    @abstractmethod
    def pad(self, padding: int) -> None:
    	pass

class IPIR(ABC):
	
	@abstractmethod
	def __call__(self, id: int) -> int:
		pass 
