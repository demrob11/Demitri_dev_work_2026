# What is Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is a way of organizing code using **objects**—bundles of data and functions that act on that data. Python supports OOP natively, and you're already using it if you've worked with exceptions, lists, or custom types.

---

## Core Concepts

- **Class**: A blueprint for objects.
- **Object**: An instance of a class.
- **Encapsulation**: Bundling data and behavior.
- **Polymorphism**: Different objects can be used interchangeably if they share the same interface.

---

## Example

```python
class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} says woof!"

class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} says meow!"

def make_it_talk(animal):
    print(animal.speak())

make_it_talk(Dog("Rex"))
make_it_talk(Cat("Whiskers"))
```

Here, `make_it_talk` demonstrates **polymorphism**—it works with any object that has a `speak()` method.

---

## Why It Matters

- Improves code **clarity** and **modularity**
- Makes components **reusable** and **extensible**
- Helps model real-world systems naturally

---

## Summary

- OOP structures code around **classes** and **objects**.
- It supports reuse, clarity, and flexibility.
- Concepts like **encapsulation** and **polymorphism** are powerful tools for scalable design.

If you've used Python exceptions, you're already working with OOP. Learning its patterns makes your code stronger and more adaptable.

