from dataclasses import dataclass, field
from typing import List, Set


@dataclass
class Conjunct:
    values: Set[float] = field(default_factory=set)
    name: str = field(default="A")
