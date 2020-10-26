# Python Decorators 
## Decorators
Decorators ~ functions that modify the functionality of another function.
* These help to make your code shorter
```python
def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")
```
```python
func_needs_decorator()
```
This function is in need of a Decorator
```python
# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)
```
```python
func_needs_decorator()
```
Code would be here, before executing the func 

This function is in need of a Decorator

Code here will execute after the func()
```python
@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")
```
```python
func_needs_decorator()
```
Code would be here, before executing the func

This function is in need of a Decorator

Code here will execute after the func()
###### Notes from PIERIAN DATA PYTHON BOOTCAMP