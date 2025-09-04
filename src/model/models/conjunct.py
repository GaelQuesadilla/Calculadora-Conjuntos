from dataclasses import dataclass, field
from typing import List, Set, Union


@dataclass
class Conjunct:
    """Clase que guarda el conjunto
    """

    values: Set[Union[float, List[float]]] = field(default_factory=set)
    name: str = field(default="A")

    def contains(self, value: Union[float, List[float]]) -> bool:
        """Checa si el valor ingresado se encuentra en el conjunto

        Parameters
        ----------
        value : Union[float, List[float]]
            Valor a buscar

        Returns
        -------
        bool
            Verdadero si se encuentra, falso si no se encuentra
        """
        return value in self.values

    def add(self, value: Union[float, List[float]]):
        """Añade un elemento al conjunto

        Parameters
        ----------
        value : Union[float, List[float]]
            Valor a añadir
        """
        self.values.add(value)
