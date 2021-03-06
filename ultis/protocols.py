from typing import Iterator, Iterable, Optional
from tqdm import tqdm


class IntList:
    def __init__(self, value: int, next: Optional['IntList']) -> None:
        self.value = value
        self.next = next

    def __iter__(self) -> Iterator[int]:
        current = self
        while current:
            yield current.value
            current = current.next


def print_numbered(items: Iterable[int]) -> None:
    for n, x in enumerate(items):
        print(n + 1, x)


x = IntList(3, IntList(5, None))
print_numbered(x)  # OK

print(10 * "=")
for x in tqdm(range(1000000)):
    pass
print_numbered([4, 5])
