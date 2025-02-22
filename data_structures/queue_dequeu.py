# Description: Queue and Dequeu usage in Python
from typing import List
from pathlib import Path
import queue

que = queue.Queue()
que.put("1")
que.put("2")
que.put("3")
print(que.get()) # 1

# -----------------------------------------------------------------------

from collections import deque

de_que = deque(["Eric", "John", "Michael"])
print(de_que.popleft(), de_que.pop())


class ListQueue(List[Path]):
    def put(self, item: Path) -> None:
        self.append(item)

    def get(self) -> Path:
        return self.pop(0)
        
    def empty(self) -> bool:
        return len(self) == 0

print(ListQueue())
