from MemLoc import MemLoc
from LMCErrors import MemoryIndexError


class Memory:
    def __init__(self, size: int):
        self.__mem = []
        for i in range(size):
            self.__mem.append(MemLoc(-999, 999))

    def mem(self) -> list:
        return self.__mem

    def __len__(self) -> int:
        return len(self.__mem)

    def __getitem__(self, key: int) -> int:
        if 0 <= key < len(self.__mem):
            return self.__mem[key].read()
        else:
            raise MemoryIndexError(key, len(self.__mem))

    def __setitem__(self, key: int, value: int):
        if 0 <= key < len(self.__mem):
            self.__mem[key].write(value)
        else:
            raise MemoryIndexError(key, len(self.__mem))
