# ForgeTensor — Day 5 Notes

# Day 5 Goal

Day 5 ka main goal tha:

- Chain Rule samajhna
- Gradient Flow samajhna
- Gradient Accumulation samajhna
- Real Backpropagation implement karna
- Day 4 ke simplified backward rules ko improve karna

---

# Problem Before Day 5

Day 4 me hum graph traverse kar pa rahe the.

Example:

```python
x = a * b
y = x * c
```

Graph:

```text
a ----*
      \
       x ----*
             \
              y
             /
c ----------*
```

Backward pass bhi chal raha tha.

Lekin gradient propagation mathematically correct nahi tha.

---

# Day 4 Limitation

Day 4 code:

```python
self.grad = other.data
other.grad = self.data
```

Problem:

```text
Incoming gradient use nahi ho raha tha.
```

Chain Rule apply nahi ho rahi thi.

---

# New Concept: Chain Rule

Suppose:

```python
x = a * b
y = x * c
```

Graph:

```text
a ----*
      \
       x ----*
             \
              y
             /
c ----------*
```

---

# Question

Gradient:

```text
dy/da
```

kaise niklega?

---

# Chain Rule

Formula:

```text
dy/da = dy/dx × dx/da
```

---

# Example

```python
a = 2
b = 5
c = 10
```

---

Local Gradients:

```text
dx/da = b

dy/dx = c
```

---

Therefore:

```text
dy/da = b × c
```

---

# Main Learning

Gradient directly calculate nahi hota.

Gradient graph ke through travel karta hai.

---

# Gradient Flow

Backward direction:

```text
Output
↓
Intermediate Nodes
↓
Input Nodes
```

Example:

```text
y.grad
↓
x.grad
↓
a.grad
```

---

# Incoming Gradient

Suppose:

```python
y.backward()
```

Backward start:

```python
y.grad = 1
```

Because:

```text
dy/dy = 1
```

---

Then:

```text
x.grad = c × y.grad
```

---

Then:

```text
a.grad = b × x.grad
```

---

# New Concept: Local Gradient

For:

```python
x = a * b
```

Local rules:

```text
dx/da = b

dx/db = a
```

---

# Difference Between Local And Incoming Gradient

## Local Gradient

Current operation ka derivative.

Example:

```text
dx/da = b
```

---

## Incoming Gradient

Child node se aaya hua gradient.

Example:

```text
x.grad
```

or

```text
out.grad
```

---

# Most Important Formula Of Day 5

```text
Parent Gradient
=
Local Gradient
×
Incoming Gradient
```

Autograd form:

```python
parent.grad += local_gradient * child.grad
```

---

# Why Out.grad Is Needed?

Day 4:

```python
self.grad = other.data
```

Wrong.

---

Day 5:

```python
self.grad += other.data * out.grad
```

Correct.

---

# Why?

Because:

```text
other.data
```

represents:

```text
Local Gradient
```

And:

```text
out.grad
```

represents:

```text
Incoming Gradient
```

---

# New Multiplication Backward Rule

Old:

```python
def mul_backward():

    self.grad = other.data
    other.grad = self.data
```

---

New:

```python
def mul_backward():

    self.grad += other.data * out.grad
    other.grad += self.data * out.grad
```

---

# Addition Backward Rule

For:

```python
out = a + b
```

Derivatives:

```text
dout/da = 1

dout/db = 1
```

---

Implementation:

```python
def add_backward():

    self.grad += 1.0 * out.grad
    other.grad += 1.0 * out.grad
```

---

# New Concept: Gradient Accumulation

Question:

Why use:

```python
+=
```

instead of:

```python
=
```

---

# Example

```python
a = Value(3)

b = a + a
```

Graph:

```text
   a
  / \
 /   \
a     a
 \   /
   b
```

---

Derivative:

```text
db/da = 2
```

---

Using "="

```python
a.grad = 1
a.grad = 1
```

Result:

```text
1
```

Wrong.

---

Using "+="

```python
a.grad += 1
a.grad += 1
```

Result:

```text
2
```

Correct.

---

# Why Gradient Accumulation Matters?

A node can receive gradients from:

```text
Multiple Paths
```

All contributions must be added.

---

# Day 5 Code Changes

## Multiplication

Old:

```python
self.grad = other.data
```

New:

```python
self.grad += other.data * out.grad
```

---

## Addition

Old:

```python
self.grad = 1.0
```

New:

```python
self.grad += 1.0 * out.grad
```

---

# Key Terms Learned

| Term | Meaning |
|--------|--------|
| Chain Rule | Gradient multiplication across path |
| Local Gradient | Current operation derivative |
| Incoming Gradient | Child node gradient |
| Gradient Flow | Output → Input travel |
| Gradient Accumulation | Multiple path contributions add karna |
| out.grad | Incoming gradient |
| += | Gradient accumulation |
| = | Overwrite (usually wrong for autograd) |

---

# Main Learning Of Day 5

Day 4 me humne graph traverse karna seekha.

Day 5 me humne:

```text
Graph me gradient travel karna
```

seekha.

---

# Golden Formula

```python
parent.grad += local_gradient * child.grad
```

This single line represents:

- Chain Rule
- Gradient Flow
- Gradient Accumulation

---

# Project Status

Day 1:
- Computational Graph

Day 2:
- Gradient Storage

Day 3:
- Single Node Backward

Day 4:
- Graph Traversal + Topological Ordering

Day 5:
- Chain Rule + Gradient Flow + Gradient Accumulation + Real Backpropagation