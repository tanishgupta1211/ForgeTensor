# ForgeTensor — Day 3 Notes

# Day 3 Goal

Day 3 ka goal tha:

- First working backward propagation banana
- Gradient calculation ka intuition samajhna
- Contribution concept samajhna
- `_backward()` function introduce karna

Aaj pehli baar framework ne gradient calculate kiya.

---

# Biggest Understanding of Day 3

Humara framework sirf calculation history store nahi kar raha.

Ab wo history use karke:

- contribution calculate kar sakta hai
- gradients calculate kar sakta hai

---

# Revision

Suppose:

```python
a = 2
b = 3

c = a * b
```

Then:

```text
c = 6
```

---

# Important Question

Output `c` par:

- a ka kitna effect hai?
- b ka kitna effect hai?

Ye information:
# gradient
deti hai.

---

# Contribution Concept

For:

```text
c = a * b
```

Contribution rules:

```text
dc/da = b
dc/db = a
```

---

# Example

If:

```python
a = 2
b = 3
```

Then:

```text
dc/da = 3
dc/db = 2
```

So:

```python
a.grad = 3
b.grad = 2
```

---

# Intuition

Agar:

```python
a = 2
b = 3
```

Aur a ko thoda increase kare:

```python
a = 3
```

Then:

```text
c = 9
```

Output:

```text
+3
```

increase hua.

---

# Similarly

Agar:

```python
b = 4
```

Then:

```text
c = 8
```

Output:

```text
+2
```

increase hua.

---

# Observation

| Variable | Output Effect |
|-----------|-----------|
| a | 3 |
| b | 2 |

Contribution equal nahi hai.

---

# Why Gradients Matter?

Gradient batata hai:

> Output ko improve karne ke liye kis value ko kitna adjust karna hai.

---

# Student Analogy

Final Marks:

```text
40
```

Analysis:

```text
Algebra → 70% problem
Geometry → 30% problem
```

Toh:

- Algebra par zyada focus
- Geometry par kam focus

AI bhi exactly yehi karta hai.

---

# New Concept Added

## _backward()

Every node ke paas ek instruction hogi:

```text
Agar backward call hua,
toh gradient kaise distribute karna hai?
```

---

# Constructor Update

```python
self._backward = lambda: None
```

Meaning:

Default backward function.

Abhi kuch nahi karega.

---

# Multiplication Backward Rule

```python
def _backward():
    self.grad = other.data
    other.grad = self.data
```

Meaning:

For:

```text
c = a*b
```

Gradient distribute karo:

```text
a.grad = b
b.grad = a
```

---

# Why Store _backward?

Forward pass me:

```python
c = a*b
```

ke time hi future ke liye instruction save kar dete hain.

Taaki later:

```python
c.backward()
```

call kar sake.

---

# New Method Added

```python
def backward(self):
    self._backward()
```

Meaning:

```python
c.backward()
```

actually:

```python
c._backward()
```

run karta hai.

---

# Before Backward

```python
a = Value(2.0)
b = Value(3.0)

c = a*b
```

Output:

```text
a.grad = 0.0
b.grad = 0.0
```

---

# Why Zero?

Because:

```python
self.grad = 0.0
```

Initial value hai.

Abhi gradient calculate nahi hua.

---

# After Backward

```python
c.backward()
```

Output:

```text
a.grad = 3.0
b.grad = 2.0
```

---

# Why Did Gradient Change?

Gradient change nahi hua.

Gradient:
# pehli baar calculate hua.

Before:

```text
Unknown
```

After:

```text
Calculated
```

---

# Current Framework Capabilities

Framework now:

✅ stores value  
✅ stores operation  
✅ stores parent nodes  
✅ stores gradient  
✅ calculates multiplication gradients  
✅ supports backward()

---

# Current Limitation

This works:

```python
c = a*b
```

But not properly for:

```python
d = (a*b) + c
```

---

# Why?

Because:

Framework abhi graph me travel nahi karta.

Sirf current node ka `_backward()` run karta hai.

---

# Graph Example

```python
d = (a*b) + c
```

Graph:

```text
a ----*
      \
       e ----+
             \
              d
             /
c ----------+
```

---

# What Is Missing?

Framework ko seekhna hai:

```text
Output
↓
Parents
↓
Grandparents
↓
...
```

peeche kaise travel karna hai.

---

# Important Terms Learned

| Term | Meaning |
|--------|--------|
| Gradient | contribution / rate of change |
| Contribution | output par effect |
| backward() | gradient calculation start karna |
| _backward() | gradient distribution rule |
| Dependency | value kis se bani |
| Graph Traversal | graph me backward move karna |

---

# Main Understanding of Day 3

Humne:

"History store karne wale framework"

se

"Gradient calculate karne wale framework"

ki taraf pehla step liya.

---

# Day 4 Goal

- Graph traversal
- Topological ordering
- Multi-step backward propagation
- Real autograd engine foundation

---

# Project Status

Day 1:
- Graph tracking

Day 2:
- Gradient storage

Day 3:
- First working backward propagation
