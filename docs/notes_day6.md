# ForgeTensor — Day 6 Notes

# Day 6 Goal

Day 5 me jo Chain Rule aur Gradient Accumulation implement kiya tha,

Day 6 ka goal tha:

- Verify karna ki implementation mathematically correct hai
- Multiple graphs par dry run karna
- Gradient flow ko deeply samajhna
- Gradient accumulation ko prove karna

---

# Main Idea

Code chal jana enough nahi hai.

Hume verify karna hai ki:

```text
Computed gradients
=
Actual mathematical gradients
```

---

# Test 1

```python
a = Value(2)
b = Value(3)

c = a * b
```

Graph:

```text
a ----*
      \
       c
      /
b ----*
```

---

# Backward

```python
c.backward()
```

---

# Gradients

```text
dc/da = b = 3

dc/db = a = 2
```

Result:

```text
a.grad = 3

b.grad = 2
```

---

# Learning

Multiplication local gradient:

```text
dx/da = b

dx/db = a
```

---

# Test 2

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

# Chain Rule

```text
dy/da = dy/dx × dx/da
```

---

# Local Gradients

```text
dx/da = b

dx/db = a

dy/dx = c

dy/dc = x
```

---

# Final Gradients

```text
x.grad = c

a.grad = b × c

b.grad = a × c

c.grad = x
```

---

# Example

```python
a = 2
b = 3
c = 4
```

Result:

```text
x.grad = 4

a.grad = 12

b.grad = 8

c.grad = 6
```

---

# Learning

Gradient graph me travel karta hai.

```text
Output
↓
Intermediate Nodes
↓
Input Nodes
```

---

# Test 3

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

# Mathematical Derivative

```text
b = a + a

db/da = 2
```

---

# Why?

First path:

```text
1
```

Second path:

```text
1
```

Total:

```text
1 + 1 = 2
```

---

# Learning

Same node multiple paths se gradient receive kar sakta hai.

---

# Test 4

```python
a = Value(2)

b = a * a
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

# Mathematical Derivative

```text
b = a²

db/da = 2a
```

---

# For a = 2

```text
db/da = 4
```

---

# Why?

First contribution:

```text
2
```

Second contribution:

```text
2
```

Total:

```text
4
```

---

# Biggest Discovery Of Day 6

Why:

```python
+=
```

is necessary.

---

# Wrong

```python
a.grad = contribution
```

Problem:

```text
Previous gradient lost
```

---

# Correct

```python
a.grad += contribution
```

Benefit:

```text
All path contributions accumulate
```

---

# Shared Node Concept

A node can appear multiple times in graph.

Examples:

```python
a + a

a * a
```

---

# Gradient Accumulation

When multiple paths reach same node:

```text
Total Gradient
=
Sum Of All Contributions
```

---

# Day 6 Verification

Verified:

✅ Chain Rule

✅ Gradient Flow

✅ Local Gradient

✅ Incoming Gradient

✅ Gradient Accumulation

✅ Shared Nodes

✅ Why += is mandatory

---

# Important Formula

```python
parent.grad += local_gradient * child.grad
```

---

# Meaning

```text
Parent Gradient
=
Incoming Gradient
×
Local Gradient
```

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
- Chain Rule + Gradient Flow

Day 6:
- Gradient Verification + Shared Nodes + Gradient Accumulation Proof