# ForgeTensor — Day 4 Notes

# Day 4 Goal

Day 4 ka main goal tha:

- Computational graph ko traverse karna
- Recursion samajhna
- Topological ordering samajhna
- Reverse topological traversal samajhna
- Framework ko poore graph me backward travel karna sikhana

---

# Problem Before Day 4

Day 3 tak:

```python
a = Value(2)
b = Value(3)

c = a * b

c.backward()
```

work kar raha tha.

Lekin:

```python
e = a * b
d = e + c

d.backward()
```

properly work nahi kar raha tha.

---

# Why?

Framework sirf:

```python
d._backward()
```

run kar raha tha.

Lekin usse ye nahi pata tha:

```text
d kis se bana?
e aur c

e kis se bana?
a aur b
```

---

# Main Realization

Backward propagation ke liye:

```text
Output
↓
Parents
↓
Grandparents
↓
...
```

travel karna padega.

---

# Example Graph

```python
e = a * b
d = e + c
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

# New Concept: Graph Traversal

Graph traversal ka matlab:

```text
Current node
↓
Parents
↓
Parents ke parents
↓
...
```

visit karna.

---

# Important Property

Every node stores:

```python
self.prev
```

Meaning:

```text
Main kis kis se bana hu?
```

Example:

```python
d.prev = {e, c}
e.prev = {a, b}
```

---

# Leaf Nodes

Leaf nodes:

```text
a
b
c
```

Ye kisi aur operation se nahi bane.

---

# Why Leaf Nodes Matter?

Traversal eventually leaf nodes par ruk jata hai.

Example:

```python
a.prev
```

returns:

```python
set()
```

---

# Recursion

Humne recursive thinking use ki.

Idea:

```text
Node visit karo
↓
Uske parents visit karo
↓
Phir current node process karo
```

---

# build_topo()

New helper function:

```python
build_topo(node)
```

Purpose:

```text
Poore graph ke nodes collect karna
```

---

# Why visited Set?

```python
visited = set()
```

Purpose:

```text
Same node ko multiple times visit hone se bachana
```

---

# Traversal Logic

For current node:

```python
if node not in visited:
```

Then:

```python
visited.add(node)
```

Then:

```python
for child in node.prev:
```

Parents visit karo.

---

# Most Important Rule

Current node ko:

```python
topo.append(node)
```

tabhi add karo

jab uske saare parents visit ho chuke hon.

---

# Why?

Example:

```text
a ----*
      \
       e ----+
             \
              d
             /
c ----------+
```

Hum nahi chahte:

```text
d
e
a
b
c
```

---

Hum chahte:

```text
a
b
e
c
d
```

---

# Topological Order

Definition:

> Aisa order jisme dependencies pehle aati hain aur dependent nodes baad me.

Example:

```text
a
b
e
c
d
```

---

# Topological Order For Example Graph

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

Topo order:

```text
[a, b, e, c, d]
```

---

# Why Is This Useful?

Because:

```text
e depends on a,b
d depends on e,c
```

---

# Backward Propagation Direction

Forward:

```text
a,b,c
↓
e
↓
d
```

Backward:

```text
d
↓
e,c
↓
a,b
```

---

# Reverse Topological Order

Backward pass ke liye:

```python
topo[::-1]
```

use kiya.

Example:

```text
[a, b, e, c, d]
```

becomes:

```text
[d, c, e, b, a]
```

---

# Why Reverse?

Backward propagation:

```text
Output
↓
Inputs
```

direction me hoti hai.

---

# Difference Between backward() And _backward()

## backward()

Purpose:

```text
Poora backward pass start karna
```

Responsibilities:

- build topo
- reverse topo
- call node backward rules

---

## _backward

Purpose:

```text
Current node ka local gradient rule
```

Example:

For multiplication:

```text
dc/da = b
dc/db = a
```

---

# Important Understanding

## prev

Stores:

```text
Dependency information
```

Example:

```text
Main kis se bana hu?
```

---

## _backward

Stores:

```text
Local gradient rule
```

Example:

```text
Addition rule
Multiplication rule
```

---

## build_topo()

Stores nothing.

It only:

```text
Traverses graph
```

---

# Day 4 Code Flow

```text
backward()
↓
build_topo()
↓
topological order
↓
reverse order
↓
call _backward()
```

---

# Limitation Discovered

Current implementation uses:

```python
self.grad = ...
```

instead of:

```python
self.grad += ...
```

This is not the final autograd implementation.

---

# Important Bug Found

Output node gradient:

```python
self.grad
```

starts as:

```python
0.0
```

But real backward propagation requires:

```python
output.grad = 1.0
```

before traversal begins.

---

# Key Terms Learned

| Term | Meaning |
|--------|--------|
| Graph Traversal | graph me travel karna |
| Recursion | function khud ko call kare |
| Leaf Node | node with no parents |
| Dependency | kis se bana |
| Topological Order | dependency-first order |
| Reverse Topological Order | backward traversal order |
| prev | parent nodes |
| _backward | local gradient rule |
| backward() | full backward pass |

---

# Main Learning Of Day 4

Humne:

"Single-node backward"

se

"Whole-graph backward traversal"

tak ka safar complete kiya.

---

# Day 5 Goal

- Chain Rule
- Gradient Flow
- Gradient Accumulation
- Why += is needed
- Real gradient propagation
- Proper autograd behavior

---

# Project Status

Day 1:
- Computational graph creation

Day 2:
- Gradient storage

Day 3:
- First backward propagation

Day 4:
- Graph traversal + topological ordering + reverse traversal