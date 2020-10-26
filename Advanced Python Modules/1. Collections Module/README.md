# Collections Module
## Counter
Counter is a dict subclass which helps count hashable objects. Inside of it elements are stored as dictionary keys and the counts of the objects are stored as the value.
```python
from collections import Counter
```
### Counter() with lists
```python
List = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
Counter(List)
```
Counter({5: 5, 4: 4, 3: 3, 2: 2, 1: 1})
### Counter with strings
```python
Counter('aaabuebxub')
```
Counter({'a': 3, 'b': 3, 'u': 2, 'e': 1, 'x': 1})
### Counter with words in a sentence
```python
Sentence = 'Let us check, how many times each word shows up in this line'
Words = Sentence.split()
Counter(Words)
```
Counter({'Let': 1, 'us': 1, 'check,': 1, 'how': 1, 'many': 1, 'times': 1, 'each': 1,'word': 1, 'shows': 1, 'up': 1, 'in': 1, 'this': 1, 'line': 1})

Methods with Counter()
```python
co = Counter(Words)
co.most_common()
```
[('Let', 1), ('us', 1), ('check,', 1), ('how', 1), ('many', 1), ('times', 1), ('each', 1), ('word', 1), ('shows', 1), ('up', 1), ('in', 1), ('this', 1), ('line', 1)]
## Common patterns when using the Counter() object
```python
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
```
## defaultdict
defaultdict is a dictionary-like object which provides all methods provided by a dictionary but takes a first argument (default_factory) as a default data type for the dictionary. Using defaultdict is faster than doing the same using dict.set_default method.
##### A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.
```python
from collections import defaultdict

d = {}
d = defaultdict(object)
d['one']
for item in d:
    print(item)
```
```python
# initialize with default values
d = defaultdict(lambda: 0)
d['one']  # 0
```
## namedtuple
namedtuples can be used a very quick way of creating a new object/class type with some attribute fields.
```python
from collections import namedtuple

Cat = namedtuple('Cat', ['age', 'breed', 'name'])
belle = Cat(age=2, breed='Lad', name='Belle')
belle       # Cat(age=2, breed='Lab', name='Belle')
belle.age   # 2
belle.breed # Lad
belle[2]    # Belle
```
