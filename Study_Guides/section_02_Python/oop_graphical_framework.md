# Framing Object-Oriented Programming Visually: Classes, Objects, and Exceptions

To better understand Object-Oriented Programming (OOP), it's helpful to visualize how **classes**, **objects**, and **exceptions** relate to one another. Think of your codebase as a modular system where objects act as **components**, classes are **blueprints**, and exceptions serve as **signals** between those components.

---

## Visual Metaphor: Blueprint and Network

### 1. **Class as Blueprint**

- Think of a **class** as a template—a design plan.
- Every time you create an object, you're building an instance from this blueprint.

```
[Class: Character]
     |
     v
[Object: hero]   [Object: villain]
```

### 2. **Objects as Nodes**

- Objects hold state (attributes) and can perform actions (methods).
- In a program, they can communicate or interact with each other.

```
[hero] --> attack() --> [villain]
```

### 3. **Exceptions as Warnings or Signals**

- Exceptions behave like messages sent when something goes wrong.
- These are also objects—specialized ones for handling errors.

```
[process_scene()] ---> [raises SceneNotFoundError]
                       --> [caught and redirected in handle_error()]
```

---

## Concept Map: How It All Connects

```
           [BaseException]
                  |
          -------------------
          |                 |
     [ValueError]     [CustomError]
                            |
                    [SceneNotFoundError]

[Class] --> [Object] --> [Interaction]
                    \-> [Exception Raised] --> [Handled in try/except]
```

### How to Read This:

- **Hierarchy**: `SceneNotFoundError` is a specific kind of `CustomError`, which is a subclass of `BaseException`. Similarly, `ValueError` is a built-in subclass of the same base.
- **Usage Flow**:
  - You write a `Class` (e.g., `Scene`).
  - You create an `Object` from that class (e.g., `scene1`).
  - The object performs some `Interaction` (e.g., `scene1.render()`).
  - During that interaction, something might go wrong.
  - An `Exception` is raised (`SceneNotFoundError`).
  - This is then caught and handled using `try/except`.

This map illustrates how exceptions fit naturally into an object-oriented design. They’re just another kind of object—but one that signals and responds to failure states.

---

## Practice-Based Organization

- **Define classes** for each entity in your system (e.g., `Character`, `Scene`, `Inventory`)
- **Use methods** for behaviors, and raise **custom exceptions** to handle invalid states
- **Catch exceptions** at the boundaries of your system, where input/output or major transitions happen
- **Design exception hierarchies** like you would any other object system—group related issues under a shared base class

---

## Summary

- Visualizing OOP helps you grasp how parts of your program are structured and connected
- Exceptions are just objects with a special purpose: signaling and managing errors
- Organizing code visually and conceptually around classes and their relationships leads to cleaner, more maintainable architecture

Seeing OOP this way turns abstract design into a tangible, interactive framework you can build and expand through deliberate practice.

