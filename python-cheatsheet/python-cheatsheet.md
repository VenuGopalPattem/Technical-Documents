# Python CheatSheet

## Definition

<ul style="display:flex; gap:40px;">
  <li>Simple</li>
  <li>Interpreted</li>
  <li>Dynamically Typed</li>
  <li>Platform Independent</li>
  <li>High Level</li>
</ul>



<b> Variable </b> - Container  Stores the value / Data <br>
<b>Rules </b>
<ul style="display:flex; gap:40px;">
  <li>Can be Alpha nums but cant Start with Num</li>
  <li>First letter Alpha or underscore</li>
  <li> Special Symbols not Allowed Except UnderScore</li>
  <li>No Keywords </li>
  <li>Case Sensitive</li>
</ul>

<b>Data Types </b> - To allocate sufficient space for the variables

- Total 14 types

| Category     | Type                                   |
|-------------|----------------------------------------|
| Fundamental | int, float, complex, bool              |
| Sequence    | str, bytes, bytearray, range           |
| List        | list, tuple                            |
| Set         | set, frozenset                         |
| Dict        | dict                                   |
| None        | None                                   |



<b>Base Conversions </b> 
<ul style="display:flex; gap:40px;">
    <li>bin()</li>
    <li>oct()</li>
    <li>hex()</li>
    </ul>


## Python Type Conversion Table

| From \ To     | int | float | complex | bool | str |
|--------------|-----|-------|---------|------|-----|
| int          | ✔   | ✔     | ✔       | ✔    | ✔   |
| float        | ✔   | ✔     | ✔       | ✔    | ✔   |
| complex      | ✘   | ✘     | ✔       | ✔    | ✔   |
| bool         | ✔   | ✔     | ✔       | ✔    | ✔   |
| pure string ("hello") | ✘ | ✘ | ✘ | ✔ | ✔ |
| number string ("123") | ✔ | ✔ | ✔ | ✔ | ✔ |
| int string ("10") | ✔ | ✔ | ✔ | ✔ | ✔ |
| float string ("10.5") | ✘ | ✔ | ✔ | ✔ | ✔ |
| bool string ("True") | ✘ | ✘ | ✘ | ✔ | ✔ |



<b> STRING </b> 
- stores sequence of data
- Allows Indexing and Slicing
- Immutable 




## Difference Between list, tuple, set, dict

| Feature                  | list        | tuple       | set            | dict              |
|--------------------------|------------|------------|---------------|------------------|
| Order                    | Ordered    | Ordered    | Unordered     | Ordered (3.7+)   |
| Mutable                  | Yes        | No         | Yes           | Yes              |
| Denoted By               | []         | ()         | {}            | {key: value}     |
| Allows Duplicate Values  | Yes        | Yes        | No            | Keys: No, Values: Yes |
| Indexing                 | Yes        | Yes        | No            | Keys Only        |
| Slicing                  | Yes        | Yes        | No            | No               |
| Stores                   | Values     | Values     | Unique Values | Key–Value Pairs  |


## Python String Handling Functions

| Method | Definition | Syntax | Example |
|--------|------------|--------|---------|
| capitalize() | Capitalizes first character | str.capitalize() | "hello".capitalize() → "Hello" |
| title() | Capitalizes first letter of each word | str.title() | "hello world".title() |
| upper() | Converts to uppercase | str.upper() | "abc".upper() |
| lower() | Converts to lowercase | str.lower() | "ABC".lower() |
| swapcase() | Swaps upper to lower and vice versa | str.swapcase() | "AbC".swapcase() |
| isupper() | True if all characters uppercase | str.isupper() | "ABC".isupper() |
| islower() | True if all characters lowercase | str.islower() | "abc".islower() |
| isalpha() | True if all characters are alphabets | str.isalpha() | "abc".isalpha() |
| isdigit() | True if all characters are digits | str.isdigit() | "123".isdigit() |
| isalnum() | True if alphanumeric | str.isalnum() | "abc123".isalnum() |
| isspace() | True if only whitespace | str.isspace() | "   ".isspace() |
| startswith() | Checks prefix | str.startswith(value) | "hello".startswith("he") |
| endswith() | Checks suffix | str.endswith(value) | "hello".endswith("lo") |
| find() | Returns index or -1 if not found | str.find(value) | "hello".find("e") |
| index() | Returns index (error if not found) | str.index(value) | "hello".index("e") |
| replace() | Replaces substring | str.replace(old,new) | "hello".replace("l","x") |
| split() | Splits string into list | str.split(delimiter) | "a,b,c".split(",") |
| join() | Joins iterable into string | delimiter.join(iterable) | ",".join(["a","b"]) |
| strip() | Removes leading & trailing spaces | str.strip() | " hello ".strip() |
| lstrip() | Removes left spaces | str.lstrip() | " hello".lstrip() |
| rstrip() | Removes right spaces | str.rstrip() | "hello ".rstrip() |
| count() | Counts occurrences | str.count(value) | "hello".count("l") |
| format() | Formats string | str.format(value) | "Hi {}".format("Venu") |



## Python List Methods

| Method   | Definition | Syntax | Example |
|----------|------------|--------|---------|
| append() | Adds one element to the end of the list | list.append(item) | nums = [1,2]; nums.append(3) → [1,2,3] |
| insert() | Inserts element at specific index | list.insert(index, item) | nums.insert(1, 10) |
| remove() | Removes first occurrence of value | list.remove(value) | nums.remove(2) |
| pop() | Removes and returns element (last by default) | list.pop(index) | nums.pop() |
| index() | Returns index of first occurrence | list.index(value) | nums.index(3) |
| clear() | Removes all elements | list.clear() | nums.clear() |
| copy() | Returns shallow copy of list | list.copy() | new_list = nums.copy() |
| count() | Counts occurrence of value | list.count(value) | nums.count(2) |
| reverse() | Reverses list in-place | list.reverse() | nums.reverse() |
| extend() | Adds multiple elements from iterable | list.extend(iterable) | nums.extend([4,5]) |
| sort() | Sorts list in ascending order | list.sort() | nums.sort() |
| del | Deletes element using index | del list[index] | del nums[0] |


## Python Tuple Methods

| Method   | Definition | Syntax | Example |
|----------|------------|--------|---------|
| count()  | Returns number of occurrences of value | tuple.count(value) | t = (1,2,2); t.count(2) → 2 |
| index()  | Returns index of first occurrence | tuple.index(value) | t.index(2) → 1 |


## Python Set Methods

| Method | Definition | Syntax | Example |
|--------|------------|--------|---------|
| add() | Adds single element | set.add(value) | s = {1,2}; s.add(3) |
| update() | Adds multiple elements (iterable) | set.update(iterable) | s.update([4,5]) |
| remove() | Removes element (error if not found) | set.remove(value) | s.remove(2) |
| discard() | Removes element (no error if not found) | set.discard(value) | s.discard(10) |
| pop() | Removes random element | set.pop() | s.pop() |
| clear() | Removes all elements | set.clear() | s.clear() |
| copy() | Returns shallow copy | set.copy() | new_s = s.copy() |
| union() | Combines two sets | s1.union(s2) | s1.union(s2) |
| intersection() | Common elements | s1.intersection(s2) | s1.intersection(s2) |
| difference() | Elements in first not in second | s1.difference(s2) | s1.difference(s2) |
| symmetric_difference() | Elements not common in both | s1.symmetric_difference(s2) | s1.symmetric_difference(s2) |
| issubset() | Checks if subset | s1.issubset(s2) | s1.issubset(s2) |
| issuperset() | Checks if superset | s1.issuperset(s2) | s1.issuperset(s2) |
| isdisjoint() | Checks if no common elements | s1.isdisjoint(s2) | s1.isdisjoint(s2) |
| del | Deletes entire set | del s | del s |


## Python Dict Methods

| Method | Definition | Syntax | Example |
|--------|------------|--------|---------|
| get() | Returns value for key (no error if missing) | dict.get(key) | d.get("name") |
| keys() | Returns all keys | dict.keys() | d.keys() |
| values() | Returns all values | dict.values() | d.values() |
| items() | Returns key-value pairs | dict.items() | d.items() |
| update() | Updates dictionary with another dict | dict.update(other_dict) | d.update({"age": 21}) |
| pop() | Removes key and returns its value | dict.pop(key) | d.pop("name") |
| popitem() | Removes last inserted key-value pair | dict.popitem() | d.popitem() |
| clear() | Removes all items | dict.clear() | d.clear() |
| copy() | Returns shallow copy | dict.copy() | new_d = d.copy() |
| setdefault() | Returns value of key, inserts if not present | dict.setdefault(key, value) | d.setdefault("city","Delhi") |
| fromkeys() | Creates dictionary from iterable | dict.fromkeys(iterable, value) | dict.fromkeys(["a","b"],0) |
| del | Deletes key from dictionary | del dict[key] | del d["age"] |


---

# Python Operators 

## 1️⃣ Arithmetic Operators

| Operator | What It Does | Syntax | Example |
|----------|-------------|--------|---------|
| + | Addition | a + b | 5 + 2 → 7 |
| - | Subtraction | a - b | 5 - 2 → 3 |
| * | Multiplication | a * b | 5 * 2 → 10 |
| / | Division (float result) | a / b | 5 / 2 → 2.5 |
| // | Floor Division | a // b | 5 // 2 → 2 |
| % | Modulus (remainder) | a % b | 5 % 2 → 1 |
| ** | Exponent | a ** b | 2 ** 3 → 8 |

---

## 2️⃣ Assignment Operators

| Operator | What It Does | Syntax | Example |
|----------|-------------|--------|---------|
| = | Assign value | a = 5 | a = 5 |
| += | Add and assign | a += 2 | a = a + 2 |
| -= | Subtract and assign | a -= 2 | a = a - 2 |
| *= | Multiply and assign | a *= 2 | a = a * 2 |
| /= | Divide and assign | a /= 2 | a = a / 2 |
| //= | Floor divide and assign | a //= 2 | a = a // 2 |
| %= | Modulus and assign | a %= 2 | a = a % 2 |
| **= | Power and assign | a **= 2 | a = a ** 2 |
| &= | Bitwise AND assign | a &= b | a = a & b |
| \|= | Bitwise OR assign | a \|= b | a = a \| b |
| ^= | Bitwise XOR assign | a ^= b | a = a ^ b |
| >>= | Right shift assign | a >>= 1 | a = a >> 1 |
| <<= | Left shift assign | a <<= 1 | a = a << 1 |

---

## 3️⃣ Relational (Comparison) Operators

| Operator | What It Does | Syntax | Example |
|----------|-------------|--------|---------|
| == | Equal to | a == b | 5 == 5 → True |
| != | Not equal to | a != b | 5 != 3 → True |
| > | Greater than | a > b | 5 > 3 |
| < | Less than | a < b | 3 < 5 |
| >= | Greater or equal | a >= b | 5 >= 5 |
| <= | Less or equal | a <= b | 4 <= 5 |

---

## 4️⃣ Logical Operators

| Operator | What It Does | Syntax | Example |
|----------|-------------|--------|---------|
| and | True if both true | a and b | True and False |
| or | True if at least one true | a or b | True or False |
| not | Reverses boolean | not a | not True |

---

## 5️⃣ Bitwise Operators

| Operator | What It Does | Syntax | Example |
|----------|-------------|--------|---------|
| & | AND | a & b | 5 & 3 |
| \| | OR | a \| b | 5 \| 3 |
| ^ | XOR | a ^ b | 5 ^ 3 |
| ~ | NOT (invert bits) | ~a | ~5 |
| << | Left shift | a << n | 5 << 1 |
| >> | Right shift | a >> n | 5 >> 1 |

---

## 6️⃣ Membership Operators

| Operator | What It Does | Syntax | Example |
|----------|-------------|--------|---------|
| in | Checks if value exists | x in y | 3 in [1,2,3] |
| not in | Checks if value not present | x not in y | 4 not in [1,2,3] |

---

## 7️⃣ Identity Operators

| Operator | What It Does | Syntax | Example |
|----------|-------------|--------|---------|
| is | Checks memory identity | a is b | a is b |
| is not | Checks not same object | a is not b | a is not b |




## Python Control Flow Statements

| Category | Statement | Definition | Syntax | Example |
|----------|-----------|------------|--------|---------|
| Conditional | if | Executes block if condition is True | if condition: | if x > 10: print(x) |
| Conditional | if-else | Executes one block if True, another if False | if condition: else: | if x>0: print("Yes") else: print("No") |
| Conditional | if-elif-else | Checks multiple conditions | if... elif... else | if x>10: ... elif x>5: ... |
| Conditional | Nested if | if inside another if | if condition: if condition: | if x>0: if x<10: print(x) |
|----------|-----------|------------|--------|---------|
| Looping | for | Iterates over sequence | for var in iterable: | for i in range(5): |
| Looping | while | Repeats while condition is True | while condition: | while x > 0: |
| Looping | Nested loop | Loop inside another loop | for... for... | for i in range(3): for j in range(2): |
| Looping | loop-else | Executes else when loop ends normally | for... else | for i in range(3): else: print("Done") |
|----------|-----------|------------|--------|---------|
| Transfer | break | Exits loop immediately | break | if x==5: break |
| Transfer | continue | Skips current iteration | continue | if x==5: continue |
| Transfer | pass | Does nothing (placeholder) | pass | if x>5: pass |
| Transfer | return | Exits function and returns value | return value | return x |


    
## Python Functions

### Definition
A function is a reusable block of code that performs a specific task.
It helps improve code readability, reusability, and modularity.

---

## Types of Functions

| Type | Definition | Syntax | Example |
|------|-----------|--------|---------|
| Built-in Function | Predefined functions provided by Python | function_name() | len([1,2,3]) |
| User-defined Function | Functions created by user using def | def function_name(): | def greet(): print("Hello") |
| Function with Parameters | Accepts input values | def func(param): | def add(a,b): return a+b |
| Function with Return Value | Returns a value using return | return value | return a+b |
| Anonymous Function (Lambda) | Small unnamed function | lambda arguments: expression | square = lambda x: x*x |
| Recursive Function | Function that calls itself | def func(): func() | def fact(n): return 1 if n==1 else n*fact(n-1) |

---

## Basic Function Syntax

```python
def function_name(parameters):
    # block of code
    return value
```

---

## Simple Examples

### 1. User Defined Function
```python
def greet():
    print("Hello World")

greet()
```

### 2. Function with Parameters
```python
def add(a, b):
    return a + b

print(add(5, 3))
```

### 3. Lambda Function
```python
square = lambda x: x * x
print(square(4))
```

### 4. Recursive Function
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
```

---

## Important Notes

- Functions improve modularity
- Parameters are inputs
- return sends value back
- Without return → function returns None
- Lambda is used for short one-line functions
- Recursion must have base condition


## Parameters and Arguments in Python

### Definition

- Parameter → Variable defined in function definition.
- Argument → Actual value passed to the function when calling it.

Example:
def add(a, b):   # a and b are parameters
    return a + b

add(5, 3)        # 5 and 3 are arguments

---

## Types of Parameters / Arguments

| Type | Definition | Syntax | Example |
|------|------------|--------|---------|
| Positional Arguments | Passed in correct order | func(a,b) | add(5,3) |
| Keyword Arguments | Passed using parameter name | func(a=, b=) | add(a=5, b=3) |
| Default Parameters | Predefined default value | def func(a=10): | def add(a=5,b=2): |
| Variable Length (*args) | Multiple positional arguments | def func(*args): | def add(*nums): |
| Keyword Variable Length (**kwargs) | Multiple keyword arguments | def func(**kwargs): | def user(**data): |
| Required Parameters | Must be passed | def func(a): | add(5,3) |
| Arbitrary Combination | Mix of all types | def func(a,b=10,*args,**kwargs): | func(1,2,3,x=4) |

---

## Examples

### 1. Positional Argument
```python
def add(a, b):
    return a + b

add(5, 3)
```

### 2. Keyword Argument
```python
add(b=3, a=5)
```

### 3. Default Parameter
```python
def greet(name="Guest"):
    return f"Hello {name}"

greet()
```

### 4. *args (Variable Positional Arguments)
```python
def total(*nums):
    return sum(nums)

total(1,2,3,4)
```

### 5. **kwargs (Variable Keyword Arguments)
```python
def info(**data):
    return data

info(name="Venu", age=21)
```

---

## Important Notes

- Parameters are defined in function.
- Arguments are passed during call.
- Order matters in positional arguments.
- *args stores values as tuple.
- **kwargs stores values as dictionary.
- Default parameters must come after required parameters.


## Python Exception Handling

### Definition

Exception handling is used to handle runtime errors so that the program does not crash.
It allows the program to continue execution gracefully.

---

## Basic Syntax

```python
try:
    # risky code
except ExceptionType:
    # handling code
else:
    # executes if no exception
finally:
    # always executes
```

---

## Exception Handling Components

| Keyword | Definition | Syntax | Example |
|----------|------------|--------|---------|
| try | Block containing risky code | try: | try: x = 10/0 |
| except | Handles specific error | except ErrorType: | except ZeroDivisionError: |
| else | Executes if no exception | else: | else: print("Success") |
| finally | Always executes | finally: | finally: print("Done") |
| raise | Manually raises exception | raise Exception("msg") | raise ValueError("Invalid") |
| assert | Checks condition, raises error if False | assert condition | assert x > 0 |
| custom exception | User-defined exception class | class MyError(Exception): | class AgeError(Exception): |

---

## Examples

### 1. Basic Exception Handling
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### 2. Multiple Exceptions
```python
try:
    num = int("abc")
except ValueError:
    print("Invalid number")
except TypeError:
    print("Type error")
```

### 3. try-except-else-finally
```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success")
finally:
    print("Always runs")
```

### 4. Raising Exception
```python
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")
```

### 5. Custom Exception
```python
class AgeError(Exception):
    pass

age = 15
if age < 18:
    raise AgeError("Not eligible")
```

---

## Common Built-in Exceptions

- ZeroDivisionError
- ValueError
- TypeError
- IndexError
- KeyError
- FileNotFoundError
- AttributeError

---

## Important Notes

- try block must have at least one except or finally
- except without specifying type catches all exceptions
- finally always runs (even if return is used)
- Use specific exception types for better debugging
- assert is mainly used for debugging



## Python File Handling

### Definition

File handling is used to read, write, append, and manage files stored on the system.

Python mainly provides two approaches to open files:
1. Traditional open() method
2. with statement (recommended approach)

---

## File Opening Syntax

```python
file_object = open("filename", "mode")
```

Recommended (Auto closes file):

```python
with open("filename", "mode") as file:
    # operations
```

---

## File Modes (Opening Types)

| Mode | Meaning | Description |
|------|----------|-------------|
| "r" | Read | Opens file for reading (default) |
| "w" | Write | Creates new file or overwrites existing |
| "a" | Append | Adds data at end of file |
| "x" | Exclusive create | Creates file, error if exists |
| "b" | Binary mode | Used with rb, wb etc |
| "t" | Text mode | Default text mode |
| "r+" | Read + Write | Read and write |
| "w+" | Write + Read | Overwrites and allows reading |
| "a+" | Append + Read | Append and read |

---

## Reading from File

### 1. Read Entire File
```python
with open("file.txt", "r") as f:
    data = f.read()
```

### 2. Read Line by Line
```python
f.readline()
```

### 3. Read All Lines into List
```python
f.readlines()
```

---

## Writing to File

### 1. Write (Overwrite)
```python
with open("file.txt", "w") as f:
    f.write("Hello World")
```

### 2. Append
```python
with open("file.txt", "a") as f:
    f.write("\nNew Line")
```

---

## Important File Methods

| Method | Purpose |
|--------|----------|
| read() | Reads entire file |
| readline() | Reads one line |
| readlines() | Reads all lines into list |
| write() | Writes text |
| writelines() | Writes multiple lines |
| close() | Closes file manually |

---

## File Pointer Methods

```python
f.tell()   # Returns current cursor position
f.seek(n)  # Moves cursor to position n
```

---

## Important Notes

- Always prefer with statement (auto close).
- "w" will delete existing content.
- "a" will add content at end.
- File must exist when using "r".
- Use binary mode for images, videos, etc.


## Pickle and Unpickle in Python

### Definition

Pickle is used to convert a Python object into a byte stream (serialization).
Unpickle is used to convert the byte stream back into a Python object (deserialization).

It is mainly used to store Python objects into files and retrieve them later.

---

## Syntax

### Import Module
```python
import pickle
```

---

## Pickling (Saving Object)

```python
import pickle

data = {"name": "Alice", "age": 25}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
```

- dump() → writes object into file
- "wb" → write binary mode

---

## Unpickling (Loading Object)

```python
import pickle

with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)
```

- load() → reads object from file
- "rb" → read binary mode

---

## Important Functions

| Function | Purpose |
|-----------|----------|
| pickle.dump(obj, file) | Save object to file |
| pickle.load(file) | Load object from file |
| pickle.dumps(obj) | Convert object to bytes |
| pickle.loads(bytes) | Convert bytes to object |

---

## Important Notes

- Works only for Python objects.
- Always use binary mode ("wb", "rb").
- Not secure for untrusted files (can execute malicious code).
- Cannot pickle some objects like open file handles or database connections.



## OOP (Object-Oriented Programming) in Python

### Definition

OOP is a programming paradigm based on objects and classes.
It helps organize code using real-world concepts like inheritance, encapsulation, and polymorphism.

---

## 1️⃣ Class

A class is a blueprint or template for creating objects.

### Syntax
```python
class ClassName:
    def __init__(self, value):
        self.value = value
```

### Example
```python
class Car:
    def __init__(self, brand):
        self.brand = brand
```

---

## 2️⃣ Object

An object is an instance of a class.

### Example
```python
car1 = Car("Toyota")
print(car1.brand)
```

---

## 3️⃣ Encapsulation

Encapsulation means hiding internal details and restricting direct access to variables.

Python uses:
- Public → variable
- Protected → _variable
- Private → __variable

### Example
```python
class Person:
    def __init__(self, name):
        self.__name = name  # private
```

---

## 4️⃣ Abstraction

Abstraction means hiding implementation details and showing only necessary information.

Done using:
- Abstract classes
- Methods

### Example
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

---

## 5️⃣ Inheritance

Inheritance allows one class to inherit properties and methods from another class.

### Example
```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    pass
```

---

## 6️⃣ Polymorphism

Polymorphism means one method behaves differently for different objects.

### Example (Method Overriding)
```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
```

---

## Summary

| Concept | Meaning |
|----------|----------|
| Class | Blueprint of object |
| Object | Instance of class |
| Encapsulation | Hiding data |
| Abstraction | Hiding implementation |
| Inheritance | Reusing parent class |
| Polymorphism | One interface, many forms |



## Python Classes

### Definition

A class is a blueprint used to create objects.  
It can contain variables (data members) and functions (methods).

---

# 1️⃣ Instance Data Members

### Definition
Variables that belong to each object.
Each object has its own copy.

### Syntax
```python
class ClassName:
    def __init__(self):
        self.variable = value
```

### Example
```python
class Student:
    def __init__(self, name):
        self.name = name   # instance variable

s1 = Student("John")
print(s1.name)
```

---

# 2️⃣ Class Level Data Members (Class Variables)

### Definition
Variables shared by all objects of the class.

### Syntax
```python
class ClassName:
    variable = value
```

### Example
```python
class Student:
    school = "ABC School"   # class variable

print(Student.school)
```

---

# 3️⃣ Data Methods (Instance Methods)

### Definition
Methods that operate on instance variables.
They use `self` as first parameter.

### Syntax
```python
def method_name(self):
    pass
```

### Example
```python
class Student:
    def greet(self):
        print("Hello")
```

---

# 4️⃣ Method Types in Class

## a) Instance Method

### Definition
Works with instance variables.
Uses `self`.

```python
class Demo:
    def show(self):
        print("Instance Method")
```

---

## b) Class Method

### Definition
Works with class variables.
Uses `cls` and `@classmethod`.

### Syntax
```python
@classmethod
def method(cls):
    pass
```

### Example
```python
class Demo:
    count = 0

    @classmethod
    def display(cls):
        print(cls.count)
```

---

## c) Static Method

### Definition
Does not access instance or class variables.
Uses `@staticmethod`.

### Syntax
```python
@staticmethod
def method():
    pass
```

### Example
```python
class Demo:
    @staticmethod
    def greet():
        print("Hello")
```

---

# Quick Summary Table

| Concept | Uses | Keyword |
|----------|--------|----------|
| Instance Variable | Object-specific data | self |
| Class Variable | Shared data | ClassName.var |
| Instance Method | Works on object data | self |
| Class Method | Works on class data | @classmethod |
| Static Method | Utility method | @staticmethod |



