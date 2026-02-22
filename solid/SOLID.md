
# SOLID Principles 

1. **S — Single Responsibility Principle (SRP)**

> A class should do **only one thing**.

2. **O — Open/Closed Principle (OCP)**

> Code should be **extendable without changing existing code**.

3. **L — Liskov Substitution Principle (LSP)**

> Child classes should **replace parent classes without breaking code**.

4. **I — Interface Segregation Principle (ISP)**

> Keep interfaces **small and specific**. Classes shouldn’t implement things they don’t need.

5. **D — Dependency Inversion Principle (DIP)**

> High-level code should depend on **abstractions, not concrete implementations**.

---

# Why SOLID is Important

* Makes code **clean, reusable, and maintainable**
* Reduces **bugs**
* Makes it easier to **extend functionality**

---


#  Payment Processing System (SOLID Demo)

```python
from abc import ABC, abstractmethod

# Payment Abstraction
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Payment Methods
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

# High-Level Module
class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, amount):
        print("Processing payment...")
        self.payment_method.pay(amount)


# Client Code
credit = CreditCardPayment()
upi = UPIPayment()

processor1 = PaymentProcessor(credit)
processor1.process(1000)

processor2 = PaymentProcessor(upi)
processor2.process(500)
```

---

#  What Is Happening Here?

---

## 1) Single Responsibility Principle (SRP)

Each class has **only one job**:

* `PaymentMethod` → defines payment contract
* `CreditCardPayment` → handles credit card payment
* `UPIPayment` → handles UPI payment
* `PaymentProcessor` → processes payment

No class is doing multiple responsibilities.

---

## 2) Open / Closed Principle (OCP)

If tomorrow your team says:

> “Add PayPal”

You do NOT modify existing classes.
You simply create:

```python
class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")
```

✅ Existing code untouched <br>

✅ System extended without modification

That’s Open/Closed.

---

## 3) Liskov Substitution Principle (LSP)

`PaymentProcessor` works with:

* CreditCardPayment
* UPIPayment
* PayPalPayment
* Any future payment class

As long as it follows `PaymentMethod`.

You can substitute any payment type — system still works.

---

## 4) Interface Segregation Principle (ISP)

Our interface (`PaymentMethod`) is very small:

```python
def pay(self, amount)
```

We didn’t force unnecessary methods like:

```python
refund()
check_balance()
verify_otp()
```

Each class only implements what it needs.

Clean and minimal.

---

## 5️) Dependency Inversion Principle (DIP)

Look at this line:

```python
def __init__(self, payment_method: PaymentMethod):
```

`PaymentProcessor` depends on **abstraction** (`PaymentMethod`) <br>

❌ Not on concrete class like `CreditCardPayment`

This makes the system flexible and loosely coupled.

---

What code does :

> “This system allows adding new payment methods without changing existing logic.
> Each class has one responsibility.
> High-level modules depend on abstraction, not concrete implementations.
> This is why the system is flexible, testable, and scalable.”
