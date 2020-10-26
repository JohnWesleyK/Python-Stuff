# Advanced Numbers
## Binary
With the function <code>bin()</code> you can obtain their [binary](https://en.wikipedia.org/wiki/Binary_number) equivalent.
```python
bin(256)    # '0b100000000'
bin(2)      # '0b10'
bin(123456) # '0b11110001001000000'
```
## Hexadecimal
With the function <code>hex()</code> you can obtain [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) equivalent.
```python
hex(123)    # '0x7b'
hex(1024)   # '0x400'
```
## Exponentials
This function <code>pow()</code> takes two arguments, equivalent to ```x^y```.  With three arguments it is equivalent to ```(x^y)%z```, but may be more efficient for long integers.
```python
pow(10,3)   # 1000
pow(10,3,7) # 6
```
## Round
The function <code>round()</code> will round a number to a given precision in decimal digits (default 0 digits).
It does not convert integers to floats.
```python
round(1.23456,3)    # 1.235
round(math.pi, 5)   # 3.14159
```
## Absolute Value
The function <code>abs()</code> returns the absolute value of a number. 
The argument may be an integer or a floating point number. 
If the argument is a complex number, its magnitude is returned.
```python
abs(-12.34)     # 12.34
```
