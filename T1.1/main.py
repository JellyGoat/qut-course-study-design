from typing import overload


class Complex():
    def __init__(self, __real__: float, __imaginary__: float = 0.0) -> None:
        self.Real = __real__
        self.Imaginary = __imaginary__

    def __add__(self, Fuck):
        B = Complex(Fuck)
        return Complex(self.Real + B.Real, self.Imaginary + B.Imaginary)

    def __sub__(self, Fuck):
        B = Complex(Fuck)
        return Complex(self.Real - B.Real, self.Imaginary - B.Imaginary)

    def __mul__(self, Fuck):
        B = Complex(Fuck)
        return Complex(self.Real * B.Real - self.Imaginary * B.Imaginary,
                       self.Real * B.Imaginary + self.Imaginary * B.Real)

    def __div__(self, Fuck):
        B = Complex(Fuck)
        return self * Complex(B.Real, -B.Imaginary) * (1 / (B.Real * B.Real - B.Imaginary * B.Imaginary))

    def __str__(self) -> str:
        return "{} + {} i(i as sqrt(-1))".format(self.Real, self.Imaginary)

print(Complex(12, 14) + 3.75)