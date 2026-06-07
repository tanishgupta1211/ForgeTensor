class Value:

    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0.0
        self.prev = set(_children)
        self.op = _op

        # Default backward function
        self._backward = lambda: None

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"

    def __add__(self, other):

        out = Value(
            self.data + other.data,
            (self, other),
            '+'
        )

        return out

    def __mul__(self, other):

        out = Value(
            self.data * other.data,
            (self, other),
            '*'
        )

        def _backward():
            self.grad = other.data
            other.grad = self.data

        out._backward = _backward

        return out

    def backward(self):
        self._backward()


# -------------------------
# Testing
# -------------------------

a = Value(2.0)
b = Value(3.0)

c = a * b

print("Before backward:")
print("a =", a)
print("b =", b)
print("c =", c)

c.backward()

print("\nAfter backward:")
print("a.grad =", a.grad)
print("b.grad =", b.grad)