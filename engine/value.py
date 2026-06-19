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

            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad

        out._backward = add_backward

        return out

    def __mul__(self, other):

        out = Value(
            self.data * other.data,
            (self, other),
            '*'
        )

        def mul_backward():

            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = mul_backward

        return out

    def relu(self):

        out = Value(
            self.data if self.data > 0 else 0,
            (self,),
            'ReLU'
        )

        def relu_backward():

            self.grad += (1 if self.data > 0 else 0) * out.grad

        out._backward = relu_backward

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


# -------------------------
# Testing ReLU
# -------------------------

a = Value(-3)

b = a.relu()

print("Forward:")
print("a =", a)
print("b =", b)

b.backward()

print("\nBackward:")
print("a.grad =", a.grad)