
# The Python hypot function returns the square root of the sum of squares of the specified arguments.
from math import hypot

class Vector:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "Vector(%r, %r)"%(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


print((4 or 5))
print((4 and 5))
print(bool(4 or 5))

# Python语言参考手册中的“Data Model”一章列出了83个特殊方法的名字，其中47个用于实现算术运算、位运算和比较操作