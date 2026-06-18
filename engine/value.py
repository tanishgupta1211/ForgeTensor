class Value:

    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0.0
        self.prev = set(_children)
        self.op = _op

        self._backward = lambda: None

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"

    def __add__(self, other):

        out = Value(
            self.data + other.data,
            (self, other),
            '+'
        )

        def add_backward():
            self.grad = 1.0
            other.grad = 1.0

        out._backward = add_backward

        return out

    def __mul__(self, other):

        out = Value(
            self.data * other.data,
            (self, other),
            '*'
        )

        def mul_backward():
            self.grad = other.data
            other.grad = self.data

        out._backward = mul_backward

        return out

    def backward(self):

        topo = []
        visited = set()

        def build_topo(node):

            if node not in visited:

                visited.add(node)

                for child in node.prev:
                    build_topo(child)

                topo.append(node)

        build_topo(self)

        self.grad = 1.0

        for node in topo[::-1]:
            node._backward()


a = Value(2.0)
b = Value(3.0)
c = Value(4.0)

e = a * b
d = e + c

print("Before backward:")
print("a =", a)
print("b =", b)
print("c =", c)
print("e =", e)
print("d =", d)

d.backward()

print("\nAfter backward:")
print("a.grad =", a.grad)
print("b.grad =", b.grad)
print("c.grad =", c.grad)
print("e.grad =", e.grad)
print("d.grad =", d.grad)