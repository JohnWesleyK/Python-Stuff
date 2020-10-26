# Timing python code
We have two functions that do the same thing differently, we will be timing them to check efficiency.
```python
def func_one(n):
    return [str(num) for num in range(n)]

func_one(10)
```
```text
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```
```python
def func_two(n):
    return list(map(str,range(n)))

func_two(10)
```
```text
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```
## Timing Start and Stop
We can use time module to simply calculate the elapsed time for the code, but due to the time module's precision, the code needs to take at least 0.1 seconds to complete.
```python
import time

# Current time before running
start_time = time.time()

# Run code
result = func_one(10000)

# Current time after running
end_time = time.time()

# elapsed time
elapsed_time = end_time - start_time
```
```text
0.008975982666015625
```
## timeit Module
If we have two blocks of code that are quite fast, then we can use the timeit module.
The timeit module takes in two strings, a statement (stmt) and a setup. It then runs the setup code and runs the stmt code some n number of times and reports back average length of time it took.
The setup (anything that needs to be defined beforehand, such as def functions.)
```python
import timeit
stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
timeit.timeit(stmt,setup,number=100000)
```
```text
5.769111
```
```python
stmt = '''
func_two(100)
'''
setup = '''
def func_two(n):
    return list(map(str,range(n)))
'''
timeit.timeit(stmt,setup,number=100000)
```
```text
4.3454992
```