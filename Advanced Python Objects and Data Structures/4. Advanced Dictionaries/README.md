# Advanced Dictionaries
## Dictionary Comprehensions
```python
{x:x*2 for x in range(10)}
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}

```
## Iteration over keys, values, and items
```python
d = {'k1':1,'k2':2}
```
```python
for k in d.keys():
    print(k)
#   k1
#   k2
```
```python
for v in d.values():
    print(v)
#   1
#   2
```
```python
for item in d.items():
    print(item)
# ('k1', 1)
# ('k2', 2)
```
## Viewing keys, values and items
```python
key_view = d.keys()
key_view            # dict_keys(['k1', 'k2'])
```
```python
d['k3'] = 3
d           # {'k1': 1, 'k2': 2, 'k3': 3}
```
```python
key_view    # dict_keys(['k1', 'k2', 'k3'])
```