# Advanced Lists
```python
List1 = [10,20,30]
```
## append
_this method merely appends an element to the end of a list_
```python
List1.append(40)
List1           # [10, 20, 30, 40]
```
## count
<code>count()</code> _takes in an element and returns the number of occurances in your list_
```python
List1.count(1)  # 0
List1.count(20) # 1
```
## extend
**append: appends a whole object at end:**
```python
List2 = [1,2,3]
List2.append([4,5])
print(List2)        # [1, 2, 3, [4, 5]]
```
**extend: extends list by appending elements from the iterable:**

<code>extend()</code> _appends each element from the passed-in list_
```python
List2=[1,2,3]
List2.extend([4,5])
print(List2)        # [1, 2, 3, 4, 5]
```
## index
<code>index()</code> _returns the index of the element specified_
```python
List1.index(20)     # 1
List1.index(12)     # Error
```
## insert
<code>insert()</code> _takes in two arguments: <code>insert(index,object)</code> This method places the object at the index supplied_
```python
List1                           # [10, 20, 30, 40]
List1.insert(2,'new element')
List1                           # [10, 20, 'new element', 30, 40]
```
## pop
<code>pop()</code> _allows us to "pop" off the last element of a list. However, by passing an index position you can remove and return a specific element_
```python
element = List1.pop(1)  # pop the second elementment
List1                   # [10, 'new element', 30, 40]
element                 # 20
```
## remove
<code>remove()</code> _method removes the first occurrence of a value_
```python
List1                   # [10, 'new element', 30, 40]
List1.remove('new element')
List1                   # [10, 30, 40]
List2 = [1,2,3,4,3]
List2.remove(3)         # removes first instance
List2  
```
## reverse
<code>reverse()</code> _reverses a list, it affects your list permanently_
```python
List2.reverse()
List2                   # [3, 4, 2, 1]
```
## sort
<code>sort()</code> _method will sort your list_
```python
List2                   # [3, 4, 2, 1]
List2.sort()
List2                   # [1, 2, 3, 4]
```
The <code>sort()</code> method takes an optional argument for reverse sorting, this is different than simply reversing the order of items. This is more like _sorting in **descending order**_.
```python
List2                   # [3, 4, 2, 1]
List2.sort(reverse = True)
List2                   # [4, 3, 2, 1]
```