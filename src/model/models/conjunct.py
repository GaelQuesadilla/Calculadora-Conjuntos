from dataclasses import dataclass, field
from typing import List, Set, Union, Tuple


@dataclass
class Conjunct:
    values: Set[Union[float, Tuple[float]]] = field(default_factory=set)
    name: str = field(default="A")

    def contains(self, value: float):
        return value in self.values

    def add(self, value: float):
        self.values.add(value)
