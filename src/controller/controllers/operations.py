from src.model.models.conjunct import Conjunct


class Operations:
    """Controlador de operaciones, todos los elementos reciben dos conjuntos y se retorna un conjunto de resultado
    """

    def union(A: Conjunct, B: Conjunct):
        result = Conjunct(name="Result")
        for element in A.values:
            result.add(element)
        for element in B.values:
            result.add(element)
        return result

    def intersection(A: Conjunct, B: Conjunct):
        result = Conjunct(name="Result")
        for element in A.values:
            if element in B.values:
                result.add(element)
        return result

    def difference(A: Conjunct, B: Conjunct):
        result = Conjunct(name="Result")
        for element in A.values:
            if element not in B.values:
                result.add(element)
        return result

    def symmetricDifference(A: Conjunct, B: Conjunct):
        result = Conjunct(name="Result")
        for x in A.values:
            if not B.contains(x) and not result.contains(x):
                result.add(x)
        for y in B.values:
            if not A.contains(y) and not result.contains(y):
                result.add(y)
        return result

    def disjunctive(A: Conjunct, B: Conjunct):
        for x in A.values:
            if B.contains(x):
                return Conjunct(name="Result", values=set(["Los conjuntos NO cumplen con la disyuntiva"]))
        return Conjunct(name="Result", values=set(["Los conjuntos  cumplen con la disyuntiva"]))

    def symmetricProduct(A: Conjunct, B: Conjunct):
        result = Conjunct(name="Result")
        for x in A.values:
            for y in B.values:
                par = (x, y)
                if not result.contains(par):
                    result.add(par)
        return result
