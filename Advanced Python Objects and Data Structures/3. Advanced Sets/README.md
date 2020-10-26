# Advanced Sets
```python
S = set()
```
## add
_add elements to a set_

A set **won't duplicate elements**; it will only present them once (that's why it's called a set!).
```python
S.add(100)
S.add(200)
S           # {100, 200}
```
## clear
_removes all elements from the set_
```python
S.clear()
S           # set()
```
## copy
_returns a copy of the set_
```python
S1 = {100,200,300}
S2 = S1.copy()
S2              # {100, 200, 300}

```
## difference
_difference returns the difference of two or more sets._
 
 The syntax is:

    set1.difference(set2)
```python
S1              # {100, 200, 300}
S1.add(500)
S1              # {100, 200, 300, 500}
S2              # {100, 200, 300}

S1.difference(S2)   # {500}
```
## difference_update
_This returns set1 after removing elements found in set2_

syntax:

    set1.difference_update(set2)

```python
S1 = {100,200,300}
S2 = {100,400,500}
S1.difference_update(S2)
S1      # {200, 300}
```
## discard
_Removes an element from a set if it is a member_
```python
S1      # {200, 300}
S1.discard(200)
S1      # {300}
```
## intersection & intersection_update
_Returns the intersection of two or more sets as a new set, intersection_update will update a set with the intersection of itself and another_
```python
S1 = {10,20,30}
S2 = {10,20,40}
S1.intersection(S2)     # {10, 20}
S1                      # {10, 20, 30}
S1.intersection_update(S2)
S1                      # {10, 20}
```
```python
S1 = {10,20}
S2 = {10,20,40}
S3 = {50}
```
## isdisjoint
_Returns True if two sets have a null intersection_
```python
S1.isdisjoint(S2)       # False
S1.isdisjoint(S3)       # True
```
## issubset
 _Returns whether another set contains this set_
```python
S1                      # {10, 20}
S2                      # {10, 20, 40}
S1.issubset(S2)         # True
```
## issuperset
_Returns if this set contains another set_
```python
S2.issuperset(S1)       # True
S1.issuperset(S2)       # False
```
## symmetric_difference & symmetric_update
_Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)_
```python
S1      # {10, 20}
S2      # {10, 20, 40}
S1.symmetric_difference(S2)     # {40}
```
## union
_Returns the union of two sets_
```python
S1.union(S2)    # {10, 20, 40}
```
## update
_Update a set with the union of itself and others._
```python
S1.update(S2)
S1              # {10, 20, 40}
```