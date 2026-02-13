# Decorators

## Definition

A **decorator** is a function that:
- **Takes a function as input**
- **Returns a function as output**

## Purpose

Decorators **add extra functionality** to the original function **without modifying** the function itself.

## Simple Example

```python
# ============================================
# DECORATOR 1: Quality Checker
# ============================================
def quality_checker(func):
    """Checks if all items are of good quality"""
    def wrapper():
        print(" Quality Checker: Checking all items quality...")
        print("   Rice quality: Good")
        print("   Chicken quality: Fresh")
        print("   Spices quality: Perfect")
        
        # Call the original function
        func()
        
    return wrapper


# ============================================
# DECORATOR 2: Time Checker
# ============================================
def time_checker(func):
    """Checks the cooking time"""
    def wrapper():
        import time
        
        print("\n Time Checker: Starting timer...")
        start = time.time()
        
        # Call the original function
        func()
        
        end = time.time()
        print(f" Time Checker: Cooking took {end - start:.2f} seconds\n")
        
    return wrapper


# ============================================
# ORIGINAL FUNCTION: Cook
# ============================================
@time_checker
@quality_checker
def cook():
    """The cook's simple job - just cook!"""
    print("\n Cook: Cooking the biryani...")
    print(" Cook: Done! Biryani is ready!")


# ============================================
# RUN IT
# ============================================
cook()
```

## Output

```
 Quality Checker: Checking all items quality...
    Rice quality: Good
    Chicken quality: Fresh
    Spices quality: Perfect

 Time Checker: Starting timer...

 Cook: Cooking the biryani...
 Cook: Done! Biryani is ready!

 Time Checker: Cooking took 0.00 seconds
```

## How It Works

1. The `cook()` function only does **one simple thing**: cook and print "Done!"

2. But we **wrapped** it with decorators:
   - `@quality_checker` - checks quality **BEFORE** cooking
   - `@time_checker` - measures time **BEFORE and AFTER** cooking

3. The `cook()` function **never changed**. It still just cooks.

4. All the extra features (quality check, time tracking) were **added by decorators**.

## Key Points

-  Decorator = Function that wraps another function
-  Adds functionality without changing original code
-  Use `@decorator_name` syntax above the function
-  Can stack multiple decorators
-  Applied from **bottom to top** (closest decorator runs first inside)

## Real-Life Analogy

**Cook** = Original function (just cooks)

**Quality Checker** = Decorator (checks ingredients before cook starts)

**Time Checker** = Decorator (tracks how long cooking takes)

The cook doesn't check quality or track time. He just cooks. The decorators handle everything else!

---


