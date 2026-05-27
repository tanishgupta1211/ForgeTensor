# ForgeTensor — Day 2 Notes

# Day 2 Goal

Day 2 ka main goal tha:

- gradients samajhna
- multiplication operation add karna
- learning-related information store karna
- backward propagation ka intuition build karna

Humne:
# real autograd foundation
start ki.

---

# Big Picture Understanding

Hum:
AI model nahi bana rahe.

Hum:
# AI ko seekhne wali machinery
build kar rahe hain.

---

# Main Idea of Day 2

AI ko improve karne ke liye system ko pata hona chahiye:

- kis value ki wajah se output bana
- kis value ka kitna effect tha
- kis direction me improve karna hai

Ye information:
# gradients
deti hain.

---

# What is a Gradient?

Gradient = rate of change.

Simple meaning:

> “Input change hone par output kitna change hota hai?”

---

# Example

For:

y = 2x

If:
x me +1 change

Then:
y me +2 change

So derivative/gradient:

2

---

# Why Gradients Matter?

Neural networks gradients use karke learn karte hain.

Gradient batata hai:
- kis parameter ko adjust karna hai
- kitna adjust karna hai

---

# Differentiation Intuition

Differentiation basically:
# change measure karta hai.

Example:

y = x²

Derivative:

2x

Meaning:
x change hone par:
y kitni fast change karega.

---

# Computational Graph Revision

Example:

d = (a*b) + c

Graph:

a ----*
      \
       e ----+
             \
              d
             /
c ----------+

---

# Graph Meaning

- e depends on a and b
- d depends on e and c

This dependency structure:
# computational graph
kehlata hai.

---

# Why Computational Graphs Are Needed?

Because:
framework ko backward jaana hota hai.

Forward:

inputs → output

Backward:

output → inputs

Backward traversal:
gradients calculate karne ke liye hota hai.

---

# Multiplication Gradient

For:

z = x*y

Derivatives:

dz/dx = y

dz/dy = x

Meaning:

x me tiny change
→ z me y times effect

---

# New Concepts Added in Code

## Gradient Storage

```python
self.grad = 0.0