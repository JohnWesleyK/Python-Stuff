# Python Debugger
You might've used a variety of print statements to try to find errors in your code, but a better way of doing this is by using Python's built-in debugger module (pdb). The pdb module implements an interactive debugging environment for Python programs.
It includes features to let you pause your program, look at the values of variables, and watch program execution step-by-step, so you can understand what your program actually does and find bugs in the logic.
This is a bit difficult to show since it requires creating an error on purpose, but hopefully this simple example illustrates the power of the pdb module.
```python
import pdb

a = [1,2,3]
b = 2
c = 3

sum = c + b
print(sum)

# Set a trace using Python Debugger
pdb.set_trace()

sum2 = a + b
print(sum2)
```
```text
5
> c:\users\th3j9\pycharmprojects\advanced-python-modules\5. python debugger\debuggeroverview.py(13)<module>()
-> sum2 = a+b
(Pdb) z
Traceback (most recent call last):
  File "C:/Users/th3j9/PycharmProjects/Advanced-Python-Modules/5. Python Debugger/DebuggerOverview.py", line 13, in <module>
    result2 = y+x
  File "C:/Users/th3j9/PycharmProjects/Advanced-Python-Modules/5. Python Debugger/DebuggerOverview.py", line 13, in <module>
    result2 = y+x
  File "C:\Users\th3j9\anaconda3\lib\bdb.py", line 88, in trace_dispatch
    return self.dispatch_line(frame)
  File "C:\Users\th3j9\anaconda3\lib\bdb.py", line 113, in dispatch_line
    if self.quitting: raise BdbQuit
bdb.BdbQuit
```
For more info on general debugging techniques and more methods, check out the [official documentation](https://docs.python.org/3/library/pdb.html)