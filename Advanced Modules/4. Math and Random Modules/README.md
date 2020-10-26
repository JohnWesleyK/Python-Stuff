# Math and Random Modules
## Useful Math Functions
```python
import math
help(math)
```
```text
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(...)
        acos(x)
        
        Return the arc cosine (measured in radians) of x.
    
    acosh(...)
        acosh(x)
        
        Return the inverse hyperbolic cosine of x.
    
    asin(...)
        asin(x)
        
        Return the arc sine (measured in radians) of x.
    
    asinh(...)
        asinh(x)
        
        Return the inverse hyperbolic sine of x.
    
    atan(...)
        atan(x)
        
        Return the arc tangent (measured in radians) of x.
    
    atan2(...)
        atan2(y, x)
        
        Return the arc tangent (measured in radians) of y/x.
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(...)
        atanh(x)
        
        Return the inverse hyperbolic tangent of x.
    
    ceil(...)
        ceil(x)
        
        Return the ceiling of x as an Integral.
        This is the smallest integer >= x.
    
    copysign(...)
        copysign(x, y)
        
        Return a float with the magnitude (absolute value) of x but the sign 
        of y. On platforms that support signed zeros, copysign(1.0, -0.0) 
        returns -1.0.
    
    cos(...)
        cos(x)
        
        Return the cosine of x (measured in radians).
    
    cosh(...)
        cosh(x)
        
        Return the hyperbolic cosine of x.
    
    degrees(...)
        degrees(x)
        
        Convert angle x from radians to degrees.
    
    erf(...)
        erf(x)
        
        Error function at x.
    
    erfc(...)
        erfc(x)
        
        Complementary error function at x.
    
    exp(...)
        exp(x)
        
        Return e raised to the power of x.
    
    expm1(...)
        expm1(x)
        
        Return exp(x)-1.
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(...)
        fabs(x)
        
        Return the absolute value of the float x.
    
    factorial(...)
        factorial(x) -> Integral
        
        Find x!. Raise a ValueError if x is negative or non-integral.
    
    floor(...)
        floor(x)
        
        Return the floor of x as an Integral.
        This is the largest integer <= x.
    
    fmod(...)
        fmod(x, y)
        
        Return fmod(x, y), according to platform C.  x % y may differ.
    
    frexp(...)
        frexp(x)
        
        Return the mantissa and exponent of x, as pair (m, e).
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(...)
        fsum(iterable)
        
        Return an accurate floating point sum of values in the iterable.
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(...)
        gamma(x)
        
        Gamma function at x.
    
    gcd(...)
        gcd(x, y) -> int
        greatest common divisor of x and y
    
    hypot(...)
        hypot(x, y)
        
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isclose(...)
        isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0) -> bool
        
        Determine whether two floating point numbers are close in value.
        
           rel_tol
               maximum difference for being considered "close", relative to the
               magnitude of the input values
            abs_tol
               maximum difference for being considered "close", regardless of the
               magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(...)
        isfinite(x) -> bool
        
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(...)
        isinf(x) -> bool
        
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(...)
        isnan(x) -> bool
        
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(...)
        ldexp(x, i)
        
        Return x * (2**i).
    
    lgamma(...)
        lgamma(x)
        
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x[, base])
        
        Return the logarithm of x to the given base.
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(...)
        log10(x)
        
        Return the base 10 logarithm of x.
    
    log1p(...)
        log1p(x)
        
        Return the natural logarithm of 1+x (base e).
        The result is computed in a way which is accurate for x near zero.
    
    log2(...)
        log2(x)
        
        Return the base 2 logarithm of x.
    
    modf(...)
        modf(x)
        
        Return the fractional and integer parts of x.  Both results carry the sign
        of x and are floats.
    
    pow(...)
        pow(x, y)
        
        Return x**y (x to the power of y).
    
    radians(...)
        radians(x)
        
        Convert angle x from degrees to radians.
    
    sin(...)
        sin(x)
        
        Return the sine of x (measured in radians).
    
    sinh(...)
        sinh(x)
        
        Return the hyperbolic sine of x.
    
    sqrt(...)
        sqrt(x)
        
        Return the square root of x.
    
    tan(...)
        tan(x)
        
        Return the tangent of x (measured in radians).
    
    tanh(...)
        tanh(x)
        
        Return the hyperbolic tangent of x.
    
    trunc(...)
        trunc(x:Real) -> Integral
        
        Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)

```
### Rounding Numbers
Python rounds based on even and odd, so that in calculations the result / margin of error will be levelled
```python
value = 5.75
math.floor(value)
```
```text
5
```
```python
math.ceil(value)
```
```text
6
```
```python
round(4.5)
```
```text
4
```
```python
round(5.5)
```
```text
6
```
```python
round(6.5)
```
```text
6
```
### Mathematical Constants
```python
print(math.pi)
```
```text
3.14159265358979
```
```python
print(math.e)
```
```text
2.718281828459045
```
```python
print(math.nan)
```
```text
nan
```
```python
print(math.inf)
```
```text
inf
```
```python
print(math.tau)
```
```text
6.283185307179586
```
### Logarithmic Values
```python
# log e base e
print(math.log(math.e))
```
```text
1.0
```
```python
print(math.log(10))
```
```text
2.302585092994046
```
```python
print(math.e ** 2.302585092994046)
```
```text
10.000000000000002
```
### Custom Base
```python
# math.log(x, base)
print(math.log(100,10))
```
```text
2.0
```
### Trigonometric Functions
```python
# Radians
print(math.sin(math.pi/2))
```
```text
1.0
```
```python
print(math.degrees(pi/4))
```
```text
45.0
```
```python
print(math.radians(180))
```
```text
3.141592653589793
```
## Random Module
This module allows us to create random numbers, a seed can even be set to produce the same random set everytime.
If you're Mathematically gifted, try checking this out.
* https://en.wikipedia.org/wiki/Pseudorandom_number_generator
* https://en.wikipedia.org/wiki/Random_seed
### Understanding a seed
Setting a seed allows us to start from a seeded psuedo random number generator, which means the same random numbers will show up in a series.
```python
import random
print(random.randint(0,10))
print(random.randint(0,10))
```
```text
5
2
```
```python
# The value 101 is completely arbitrary, you can pass in any number you want
random.seed(100)
# You can run this cell as many times as you want, it will always return the same number
print(random.randint(0,100))
```
```text
18
```
```python
random.randint(0,100)
```
```text
54
```
```python
# The value 101 is completely arbitrary, you can pass in any number you want
random.seed(101)
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
```
```text
18
58
58
98
22
```
### Random Integers
```python
print(random.randint(1,100))
```
```text
93
```
### Random with Sequences
*Grab a random item from a list*
```python
my_list = list(range(0,10))
print(my_list)
```
```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
```python
print(random.choice(my_list))
```
```text
5
```
### Sample with Replacement
*Take a sample size, allowing picking elements more than once*
```python
my_list = list(range(0,25))
print(random.choices(population=my_list,k=10))
print(random.choices(population=my_list,k=10))
```
```text
[14, 4, 24, 23, 11, 16, 5, 5, 7, 17]
[5, 24, 1, 4, 2, 19, 9, 11, 8, 15]
```
### Sample without Replacement
*Once an item has been randomly picked, it can't be picked again.*
```python
my_list = list(range(0,25))
print(random.sample(population=my_list,k=10))
print(random.sample(population=my_list,k=10))
```
```text
[18, 6, 17, 11, 14, 1, 16, 23, 7, 9]
[15, 22, 6, 10, 14, 2, 8, 23, 5, 19]
```
### Shuffle a list
##### Note: this affects the object in place
```python
my_list = list(range(0,10))
print(my_list)
random.shuffle(my_list)
print(my_list)
```
```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[6, 7, 2, 1, 4, 0, 8, 5, 3, 9]
```
### Random Distributions
#### [Uniform Distribution](https://en.wikipedia.org/wiki/Uniform_distribution) 
```python
# Continuous, random picks a value between a and b, each value has equal change of being picked.
print(random.uniform(a=0,b=100))
```
```text
58.11521325045646
```
#### [Normal/Gaussian Distribution](https://en.wikipedia.org/wiki/Normal_distribution)
```python
print(random.gauss(mu=0,sigma=1))
```
```text
-0.5744671730602267
```
