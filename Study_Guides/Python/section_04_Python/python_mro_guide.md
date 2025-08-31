# Python Method Resolution Order (MRO)

Python's **Method Resolution Order (MRO)** determines the order in which base classes are searched when executing a method or looking up an attribute. This becomes particularly important in multiple inheritance scenarios to avoid ambiguity and ensure consistency.

---

## 🔹 MRO in Single Inheritance

In single inheritance, the MRO is straightforward. Python looks for methods in the following order:

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    pass

b = B()
b.greet()  # Output: Hello from A
```

**MRO for class B:**

```python
B -> A -> object
```

---

## 🔸 MRO in Multiple Inheritance

Python uses the **C3 linearization algorithm** to determine the MRO. This algorithm ensures a consistent order by respecting the order in which classes are inherited and by maintaining monotonicity.

### Example 1:

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

print(D.__mro__)
d = D()
d.greet()  # Output: Hello from B
```

**MRO for class D:**

```python
D -> B -> C -> A -> object
```

Python resolves the method `greet` by checking `D`, then `B`, then `C`, and so on.

### Example 2 (Diamond Problem):

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()  # Output: B
```

**MRO:**

```python
D -> B -> C -> A -> object
```

---

## 🔹 How to View MRO

Use either of these to inspect the MRO of a class:

```python
print(ClassName.__mro__)
# or
help(ClassName)
```

---

## 🔸 Summary

- **Single inheritance:** Linear and intuitive MRO.
- **Multiple inheritance:** Resolved using C3 linearization.
- Ensures predictability and consistency even in complex hierarchies.
- Avoids ambiguity with the diamond problem.

---

> ⚠️ Tip: Always be cautious with multiple inheritance. Use it wisely to keep the MRO clear and maintainable.

