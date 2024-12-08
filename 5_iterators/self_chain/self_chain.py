from typing import Generator, Iterable, TypeVar

T = TypeVar("T")

def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    for iterable in iterables:
        for item in iterable:
            yield item

class Chain:
    def __init__(self, *iterables: Iterable[T]):
        self.iterables = iterables
        self.current_iter = iter(self.iterables)
        self.current = iter([])

    def __iter__(self):
        return self

    def __next__(self) -> T:
        while True:
            try:
                return next(self.current)
            except StopIteration:
                self.current = iter(next(self.current_iter))
