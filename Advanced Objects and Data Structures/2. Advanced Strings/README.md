# Advanced String
## Changing case
```python
str = 'ez clap'
# Capitalize first word
str.capitalize()    # 'Ez clap'
str.upper()         # 'EZ CLAP'
str.lower()         # 'ez clap'
```
As strings are immutable. None of the above methods change the string in place, they only return modified copies of the original string
```python
str                 # 'ez clap'
str = str.upper()
str                 # 'EZ CLAP'
str = str.lower()
str                 # 'ez clap'
```
## Location and Counting
```python
# returns the number of occurrences, without overlap
str.count('z')      # 1
```
```python
# returns the starting index position of the first occurence
str.find('a')       # 5
```
## Formatting
The <code>center()</code> method allows you to place your string 'centered' between a provided string with a certain length
```python
str.center(11,'-')  # '--ez clap--'
```
The <code>expandtabs()</code> method will expand tab notations <code>\t</code> into spaces
```python
'tabs\ttabs'.expandtabs()   # 'tabs    tabs'
```
## is check methods
* <code>isalnum()</code> returns True if all characters in **str** are alphanumeric
* <code>isalpha()</code> returns True if all characters in **str** are alphabetic
* <code>islower()</code> returns True if all cased characters in **str** are lowercase and there is at least one cased character in **str**, False otherwise.
* <code>isspace()</code> returns True if all characters in **str** are whitespace.
* <code>istitle()</code> returns True if **str** is a title cased string and there is at least one character in **str**, i.e. uppercase characters may only follow uncased characters and lowercase characters only cased ones. It returns False otherwise.
* <code>isupper()</code> returns True if all cased characters in **s** are uppercase and there is at least one cased character in **str**, False otherwise.
* Another method is <code>endswith()</code> which is essentially the same as a boolean check on <code>str[-1]</code>
```python
str = 'nospace'
str.isalnum()       # True
str.isalpha()       # True
str.islower()       # True
str.isspace()       # False
str.istitle()       # False
str.isupper()       # False
str.endswith('e')   # True
```
## Built-in Reg. Expressions
* <code>split()</code> can split the string at a certain element and return a list of the results.
* <code>partition()</code> returns a tuple that includes the first occurrence of the separator sandwiched between the first half and the end half.
```python
str = 'nospace'
str.split('p')      # ['nos', 'ace']
str.partition('p')  # ('nos', 'p', 'ace')
```
