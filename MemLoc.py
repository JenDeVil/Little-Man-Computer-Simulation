from LMCErrors import MemoryLocationValueError, AdditionError, SubtractionError


class MemLoc:
    def __init__(self, min_value: int, max_value: int, value: int = None):
        if value is None:
            value = 0
        self.__min_value = min_value
        self.__max_value = max_value
        self.__value = value

    def __str__(self, width: int = None) -> str:  # Gets the string of the value to be shown in memory
        # Sets the width of the string to use if none is provided using the max width the string could get
        if width is None:
            width = self.getMaxStrWidth()

        # Pads the value with leading 0s
        out = str(self.__value).rjust(width, "0")

        if self.__min_value < 0:  # Makes the first character of the string to be the sign of the value
            if out[0] != "-":  # Checks if the first value of the string is a -
                if out.count("-") > 0:  # Checks if the value is a negative number
                    out = out.replace("-", "0")  # Puts the minus sign at the front of the string
                    out = "-" + out[1:]
                else:
                    out = " " + out[1:]  # Puts nothing at the front of the string if the value is positive

        return out

    def add(self, value: int):
        add = self.__value + value
        if add <= self.__max_value:
            self.__value = add
        else:
            raise AdditionError(self.__value, value, self.__max_value)

    def sub(self, value: int):
        sub = self.__value - value
        if sub >= self.__min_value:
            self.__value = sub
        else:
            raise SubtractionError(self.__value, value, self.__min_value)

    def read(self) -> int:
        return self.__value

    def write(self, val: int):
        if self.isValid(val):
            self.__value = val

    def isValid(self, val: int) -> bool:
        if self.__min_value <= val <= self.__max_value:
            return True
        else:
            raise MemoryLocationValueError(self.__min_value, self.__max_value, val)

    def getMaxStrWidth(self) -> int:
        return max(len(str(self.__min_value)), len(str(self.__max_value)))