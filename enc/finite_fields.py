import galois


class GF:
    _fields: dict[int, type[galois.FieldArray]] = dict()

    @staticmethod
    def get(order: int):
        result = GF._fields.get(order)
        if result is None:
            result = galois.GF(order)
            GF._fields[order] = result
        return result
