# ForgeTensor — Day 1 Notes

## Goal of the Project

ForgeTensor ek deep learning framework hoga jo scratch se build kiya jayega taaki hum samajh sake:

- Autograd
- Computational Graphs
- Tensor Operations
- Neural Network Internals
- GPU Execution
- Compiler Optimizations

Hum sirf AI models train nahi karenge.

Hum:
# AI frameworks ke internal systems
samjhenge aur build karenge.

---

# What is a Framework?

Framework = ready-made system/tool.

Example:
PyTorch ek framework hai jo:
- tensors handle karta hai
- gradients calculate karta hai
- neural networks train karta hai

Hum:
# mini PyTorch
build kar rahe hain.

---

# What is a Node?

Node = ek value/object.

Example:

a = 2
b = 3
c = a + b

Yahan:
- a node hai
- b node hai
- c node hai

---

# What is a Graph?

Graph = connected values/objects.

Example:

c = a + b

Graph:

a ----+
       \
        c
       /
b ----+

---

# What is a Computational Graph?

Mathematical operations ka graph.

Example:

z = x*y + x

Graph:

x ----*
      \
       + ---> z
      /
y ----

Framework graph use karta hai taaki:
- operations track ho sake
- backward pass possible ho
- gradients calculate ho sake

---

# What is Gradient?

Gradient = rate of change.

Simple meaning:
“input change karne se output kitna change hota hai”

Example:

y = 2x

x me +1 change:
y me +2 change

Gradient = 2

---

# Why are Gradients Important?

Neural networks gradients use karke learn karte hain.

Gradient batata hai:
- kis direction me improve karna hai
- weights ko kitna adjust karna hai

---

# What is Autograd?

AUTOmatic GRADient.

Autograd automatically:
- graph build karta hai
- derivatives calculate karta hai
- gradients propagate karta hai

---

# Why Are We Building This Project?

Taaki hum deeply samajh sake:
- AI frameworks internally kaise kaam karte hain
- gradients kaise flow karte hain
- graph kaise build hota hai
- learning kaise hoti hai

---

# Git Concepts Learned

## git init
Repository initialize karta hai.

## git add .
Files tracking me add karta hai.

## git commit -m "message"
Current project state ka snapshot save karta hai.

---

# Project Structure

ForgeTensor/

├── engine/
├── tests/
├── docs/
├── examples/
├── notebooks/
└── README.md

---

# Python Concepts Learned

## Class

Custom object banane ke liye use hoti hai.

Example:

class Value:
    pass

---

## __init__

Object create hone par automatically call hota hai.

---

## __repr__

Object ko readable format me print karta hai.

---

## Operator Overloading

Hum operators ka custom behavior define kar sakte hain.

Example:

a + b

internally:

a.__add__(b)

call karta hai.

---

# Current Value Class

```python
class Value:

    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.prev = set(_children)
        self.op = _op

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        out = Value(
            self.data + other.data,
            (self, other),
            '+'
        )

        return out