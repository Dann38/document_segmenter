from abc import ABC, abstractmethod
from typing import List, Tuple


class BaseSegment(ABC):
    @abstractmethod
    def get_region(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        pass
