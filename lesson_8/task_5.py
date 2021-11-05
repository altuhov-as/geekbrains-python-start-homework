class ComplexNumber:
    real: float
    indeterminate: float

    def __init__(self, real: float, indeterminate: float):
        self.real = real
        self.indeterminate = indeterminate

    def __str__(self):
        return f"({self.real}{'+' if self.indeterminate > 0 else ''}{self.indeterminate}i)"
