# Object Oriented Programming (OOP) in Python

## What is OOP?

Object Oriented Programming (OOP) is a programming paradigm that organizes code using objects instead of only functions and logic.  
It models real-world entities by combining data (variables) and behavior (methods) into a single structure called a class.

Core Concepts of OOP:
- Class
- Object
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

---

# 1️⃣ Class

## Definition

A class is a blueprint or template used to create objects.  
It defines data members (variables) and methods (functions).

## Basic Syntax

```python
class ClassName:
    pass
```

---

## Instance Variables

Instance variables belong to each object individually.  
Each object has its own copy.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name      # instance variable
        self.marks = marks    # instance variable
```

---

## Class Level Variables

Class variables are shared by all objects of the class.

```python
class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name
```

---

## Data Methods (Instance Methods)

Methods operate on instance variables and use `self`.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)
```

---

## Complete Program: Student Marks Management

```python
class Student:

    # Class level variable (shared among all objects)
    school = "XYZ Public School"

    def __init__(self, name, marks):
        # Instance variables (unique for each object)
        self.name = name
        self.marks = marks

    # Instance method to read/display data
    def display_data(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("School:", Student.school)

    # Instance method to update marks
    def update_marks(self, new_marks):
        self.marks = new_marks


# Creating objects
obj1 = Student("Rahul", 85)
obj2 = Student("Priya", 92)

# Accessing data using object
obj1.display_data()
print()

obj2.display_data()

# Updating marks using method
obj1.update_marks(95)

print("\nAfter updating marks:")
obj1.display_data()
```

---

# 2️⃣ Object

## Definition

An object is an instance of a class.  
Memory is allocated when the object is created.

## Syntax

```python
obj = ClassName(arguments)
```

## Example

```python
s1 = Student("John", 80)
```

The constructor `__init__` runs automatically when object is created.

---

# 3️⃣ Encapsulation

## Definition

Encapsulation means hiding internal data and restricting direct access to it.

Access Types:
- Public → variable
- Protected → _variable
- Private → __variable

## Example

```python
class Bank:

    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = Bank(1000)
account.deposit(500)
print(account.get_balance())
```

Direct access like `account.__balance` is not allowed.

---

# 4️⃣ Abstraction

## Definition

Abstraction hides internal implementation and shows only essential functionality.

## Example

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


c = Circle(5)
print(c.area())
```

Only the method `area()` is exposed to the user.

---

# 5️⃣ Inheritance

## Definition

Inheritance allows one class to acquire properties and methods of another class.

---

## 1. Single Inheritance

```python
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    pass

obj = Child()
obj.show()
```

Flow:
Parent → Child

---

## 2. Multilevel Inheritance

```python
class A:
    def methodA(self):
        print("Class A")

class B(A):
    def methodB(self):
        print("Class B")

class C(B):
    pass

obj = C()
obj.methodA()
obj.methodB()
```

Flow:
A → B → C

---

## 3. Hierarchical Inheritance

```python
class Parent:
    def show(self):
        print("Parent method")

class Child1(Parent):
    pass

class Child2(Parent):
    pass
```


Flow:
```
        Parent
        /     \
   Child1   Child2
```

---

## 4. Multiple Inheritance

```python
class A:
    def methodA(self):
        print("Class A")

class B:
    def methodB(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.methodA()
obj.methodB()
```
```
Flow:

A      B  
 \    /  
    C
```

---

## 5. Hybrid Inheritance

Combination of hierarchical and multiple inheritance.

```
        A
       / \
      B   C
       \ /
        D
```

---

# 6️⃣ Polymorphism

## Definition

Polymorphism means one interface, many forms.

---

## Method Overriding

Child class redefines parent method.

```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

a = Animal()
d = Dog()

a.sound()
d.sound()
```

Output:
```
Animal sound
Bark
```

Method execution depends on object type at runtime.

---

# Summary

Object Oriented Programming in Python includes:

- Class (Blueprint)
- Object (Instance)
- Encapsulation (Data hiding)
- Abstraction (Hiding implementation)
- Inheritance (Code reuse)
- Polymorphism (Multiple forms)

These concepts allow building modular, reusable, and structured programs.
