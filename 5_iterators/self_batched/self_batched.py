from typing import Generator, Iterable, TypeVar, Tuple

T = TypeVar("T")

def batched(obj: Iterable[T], n: int) -> Generator[Tuple[T, ...], None, None]:
    batch = []
    for item in obj:
        batch.append(item)
        if len(batch) == n:
            yield tuple(batch)
            batch = []
    if batch:
        yield tuple(batch)

class Batched:
    def __init__(self, obj: Iterable[T], n: int):
        self.obj = obj
        self.n = n
        self.iterator = iter(obj)
        self.batch = []

    def __iter__(self):
        return self

    def __next__(self) -> Tuple[T, ...]:
        while len(self.batch) < self.n:
            try:
                self.batch.append(next(self.iterator))
            except StopIteration:
                break

        if self.batch:
            result = tuple(self.batch)
            self.batch = []
            return result

        raise StopIteration