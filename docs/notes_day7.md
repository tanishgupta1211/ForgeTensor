# ForgeTensor — Day 7 Notes

# Day 7 Goal

Day 7 ka main goal tha:

- Non-linearity samajhna
- ReLU activation function samajhna
- ReLU ka forward pass implement karna
- ReLU ka backward pass implement karna
- Samajhna ki neural networks me ReLU ki zarurat kyun hoti hai

---

# Problem Before Day 7

Humare paas:

```python
y = w*x + b
```

tha.

Aur hum multiple layers bana sakte the:

```python
y = w1*x + b1

z = w2*y + b2
```

---

# Discovery

Suppose:

```python
y = 2x + 3
```

and

```python
z = 5y + 1
```

Substitute:

```python
z = 5(2x+3)+1
```

Result:

```python
z = 10x + 16
```

---

# Important Realization

Multiple linear layers:

```text
Linear
↓
Linear
↓
Linear
```

still produce:

```text
Linear
```

---

# Problem

Linear functions can only create:

```text
Straight Lines
```

---

# Example

Curve:

```text
y = x²
```

cannot be represented perfectly using:

```text
y = mx + b
```

---

# Need For Non-Linearity

Neural networks need:

```text
Curves
Complex Patterns
Decision Boundaries
```

To achieve this we need:

```text
Non-Linearity
```

---

# ReLU

ReLU stands for:

```text
Rectified Linear Unit
```

Definition:

```text
ReLU(x) = x    if x > 0

ReLU(x) = 0    if x < 0
```

---

# Examples

```text
ReLU(5)  = 5

ReLU(2)  = 2

ReLU(10) = 10
```

---

```text
ReLU(-1) = 0

ReLU(-5) = 0

ReLU(-10)= 0
```

---

# Intuition

Positive values:

```text
Pass through
```

Negative values:

```text
Killed
```

---

# ReLU And Graphs

Without ReLU:

```text
Straight Line
```

With ReLU:

```text
Broken Line
```

---

# Important Discovery

ReLU does NOT create curves directly.

ReLU:

```text
Breaks lines
```

---

Many ReLUs:

```text
Broken Line
+
Broken Line
+
Broken Line
```

approximate:

```text
Curves
```

---

# Why ReLU Is Powerful

Without ReLU:

```text
100 Linear Layers
=
1 Linear Layer
```

---

With ReLU:

```text
Linear
↓
ReLU
↓
Linear
↓
ReLU
```

Now the network can learn:

```text
Images

Speech

Language

Complex Patterns
```

---

# ReLU Forward Pass

Implementation:

```python
out = Value(
    self.data if self.data > 0 else 0,
    (self,),
    'ReLU'
)
```

---

# ReLU Backward Pass

Derivative:

For:

```text
x > 0
```

Derivative:

```text
1
```

---

For:

```text
x < 0
```

Derivative:

```text
0
```

---

# Why?

Example:

```text
ReLU(5)=5
```

If:

```text
5 → 5.1
```

Output also changes:

```text
5 → 5.1
```

Derivative:

```text
1
```

---

Example:

```text
ReLU(-5)=0
```

If:

```text
-5 → -4.9
```

Output:

```text
0
```

No change.

Derivative:

```text
0
```

---

# ReLU Backward Rule

```python
self.grad += (1 if self.data > 0 else 0) * out.grad
```

---

# New Method Added

```python
def relu(self):
```

---

# Day 7 Code Changes

Added:

```python
def relu(self):
```

Forward pass.

---

Added:

```python
def relu_backward():
```

Backward pass.

---

# Key Terms Learned

| Term | Meaning |
|--------|--------|
| Activation Function | Adds non-linearity |
| ReLU | Most common activation |
| Non-Linearity | Allows learning complex patterns |
| Forward Pass | Compute output |
| Backward Pass | Compute gradients |
| Derivative of ReLU | 1 (positive), 0 (negative) |

---

# Biggest Learning Of Day 7

ReLU does not directly create curves.

Instead:

```text
It breaks straight lines.
```

Many broken lines together:

```text
Approximate curves.
```

This is why deep neural networks are powerful.

---

# Project Status

Day 1:
- Computational Graph

Day 2:
- Gradient Storage

Day 3:
- Single Node Backward

Day 4:
- Topological Ordering

Day 5:
- Chain Rule

Day 6:
- Gradient Accumulation Verification

Day 7:
- ReLU Activation Function
- First Non-Linearity