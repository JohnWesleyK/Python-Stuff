# Python Generators
## Generators and Iterators
Generators allow us to generate stuff as we go on, istead of holding everything in memory.
```python
def create_square(n):
    squares = []
    for i in range(n):
        squares.append(i**2)
    return squares
```
In the block of code above, we store the entire list of squares in memory
```python
def create_square(n):
    for i in range(n):
        yield i**2
```
Yield returns the same values but without storing them in memory,
both the functions give the same result when called as follows
yield-ing is memory effiecient. Here's one more example

```python
def fibbo(n):
     I = 1
     II = 1
     for i in range(n):
         yield I
         I, II = II, I + II
```
```python
def fibbo(n):
     I = 1
     II = 1
     result = []
     for i in range(n):
         result.append(I)
         I, II = II, I + II
     return result
```
Testing both the functions
```python
for n in create_square(10):
    print(n)
print(list(create_square(10)))
for num in fibbo(10):
    print(num)
```
### next() and iter()
next() function allows us to access the next element in a sequence
```python
def basic_generator():
    for x in range(3):
        yield x
for num in basic_generator():
    print(num)

gen = basic_generator()
print(gen)
print(next(gen))
```
If an object supports iteration, like string object for example, and if we can not directly iterate over it, as we can with a generator function, iter() allows us to do that.
```python
str = 'Wassup'
str_iter = iter(str)
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
```