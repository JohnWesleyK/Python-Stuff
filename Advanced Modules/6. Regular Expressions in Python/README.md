# Regular Expressions 
#### a.k.a RegEx
## Overview
Regular Expressions (also called regex for short) allows a user to search for strings using almost any sort of rule or pattern they can come up.
Regular expressions are notorious for their seemingly strange syntax. This strange syntax is a byproduct of their flexibility. Regular expressions have to be able to filter out any string pattern you can imagine, which is why they have a complex string pattern format.

## Basic Patterns
```python
import re
pattern = 'name'
text = 'name is in text'
match = re.search(pattern,text)
match.span()
match.start()
match.end()
```
```text
<re.Match object; span=(0, 4), match='name'>
(0,4)
0
4
```
if the pattern is re-occurring
```python
text = "word occurs again word"
match = re.search("word", text)
match.span()
```
```text
(0,4)
```
we can use .findall() to find a list of all matches
```python
matches = re.findall("word", text)
matches
matches.group()
```
```text
['word', 'word']
```
we can use the iterator to get actual match objects
```python
for match in re.finditer("word",text):
    print(match.span())
```
```text
(0, 4)
(18, 22)
```
## Identifiers for Characters in Patterns
For defining a pattern string for regular expression we use the format:

r'your_pattern'

```text
 _____________________________________________________________________
| Character |   Description    | Example Pattern Code | Example Match |
|-----------|------------------|----------------------|---------------|
|    \d     |      a digit     |     file_\d\d\d      |   file_911    |
|    \w     |    alphanumeric  |     \w-\w\w\w\w      |    C-d_12     |
|    \s     |    white space   |       a\sb\sc        |    a b c      |
|    \D     |    a non digit   |       \D\D\D\D       |     QWER      |
|    \W     | non-alphanumeric |     \W\W\W\W\W\W     |    +=-*)(     |
|    \S     |  non-white space |      \S\S\S\S\S      |     swolo     |
|___________|__________________|______________________|_______________|
```
e.g:
```python
text = 'Call 123-456-7890'
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
phone.group()
```
```text
123-456-7890
```
## Quantifiers
```text
 ___________________________________________________________________________
| Character |     Description        | Example Pattern Code | Example Match |
|-----------|------------------------|----------------------|---------------|
|     +     |  occurs once or more   |     file \w-\w+      |   file A-b1_1 |
|    {2}    | occurs exactly 2 times |        \D{3}         |      abc      |
|   {1,4}   |  occurs 1 to 4 times   |       \d{2,4}        |      123      |
|   {5,}    | occurs 5 times or more |       \w{3,}         |   anyChars    |
|    \*     | occurs 0 or more times |      A\*B\*C*        |   AAABBBCC    |
|    ?      |     Once or none       |       swolos?        |     swolo     |
|___________|________________________|______________________|_______________|
```
using quantifiers
```python
phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
```
```text
<_sre.SRE_Match object; span=(5, 20), match='123-456-7890'>
```
## Groups
We can use groups for any general task that involves grouping together regular expressions (so that we can later break them down).
For the phone number example, we can separate groups of regular expressions using parenthesis:
```python
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)

# The entire result
results.group()

# Can then also call by group position.
# remember groups were separated by parenthesis ()
# Something to note is that group ordering starts at 1. Passing in 0 returns everything
results.group(1)
results.group(2)
results.group(3)
```
```text
'123-456-7890'
'123'
'456'
'7890'
```
## Additional Regex Syntax
### OR operator |
```python
re.search(r'ios|android','I have an android device')
```
```text
<re.Match object; span=(10, 17), match='android'>
```
### Wildcard Character
putting a . before text
```python
re.findall(r'ab','ab aba abc abcd')
re.findall(r'.ab','cab crab fab dab')
re.findall(r'..ab','cab crab fab dab')
```
```text
['ab', 'ab', 'ab', 'ab']
['cab', 'rab', 'fab', 'dab']
['crab', ' fab', ' dab']
```
### Starts with and Ends with
use the **^** to signal starts with, and the **$** to signal ends with
```python
re.findall(r'^\d','1 this starts with a num')
```
```text
['1']
```
```python
re.findall(r'\d$','this ends with a num 0')
```
```text
['0']
```
### Exclusion
use the **^** symbol in conjunction with a set of brackets **[]**. Anything inside the brackets is excluded
```python
entence = 'there are 2 numbers 12 inside this 2'
pattern = r'[^\d]+'
re.findall(pattern,sentence) # number exclusion
```
```text
['there are ', ' numbers ', ' inside this ']
```
```python
punc_phrase = 'This is a string! But it has punctuation. How will you remove it?'
clean = re.findall(r'[^!.? ]+',punc_phrase)
sentence_without_punc = ' '.join(clean)
```
```text
['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'How', 'will', 'you', 'remove', 'it']
'This is a string But it has punctuation How will you remove it'
```
## Brackets for Grouping
```python
text = 'only find the hypen-words clap-ish ez'
pattern = r'[\w]+'
re.findall(pattern,text)

pattern = r'[\w]+-[\w]+'
re.findall(pattern,text)
```
```text
['only', 'find', 'the', 'hypen', 'words', 'clap', 'ish', 'ez']
['hypen-words', 'clap-ish']
```
## Parenthesis for Multiple Options/Matches
```python
phrase = 'Barbell'
phrasetwo = "Barpath"
phrasethree = "Barsnatch"
re.search(r'Bar(bell|path|snatch)',phrase)
re.search(r'Bar(bell|path|snatch)',phrasetwo)
re.search(r'Bar(bell|path|snatch)',phrasethree)
```
```text
<re.Match object; span=(0, 7), match='Barbell'>
<re.Match object; span=(0, 7), match='Barpath'>
<re.Match object; span=(0, 9), match='Barsnatch'>
```
for more info check out the official [documentation](https://docs.python.org/3/howto/regex.html)
