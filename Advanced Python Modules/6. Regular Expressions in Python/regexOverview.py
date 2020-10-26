text = "The phone number is 123-1234-12345 "

import re

pattern = 'phone'

re.search(pattern,text)
# <re.Match object; span=(4, 9), match='phone'>

match = re.search(pattern,text)

match.span()
# (4, 9)

match.start()
# 4

match.end()
#9

text_with_multiple_words = "this has two phones, phones"
matches = re.findall(pattern,text_with_multiple_words)
# ['phone', 'phone']

for match in re.finditer(pattern,text_with_multiple_words):
    print(match.group())
# phone
# phone


#phone_number = re.search(r'\d\d\d-\d\d\d\d-\d\d\d\d\d',text)
phone_number = re.search(r'\d{3}-\d{4}-\d{5}',text)
phone_number.group()
# 123-1234-12345

phone_number_pattern = re.compile(r'(\d{3})-(\d{4})-(\d{5})')
result = re.search(phone_number_pattern,text)
result.group()
# 123-1234-12345

# group() indexing starts from 1 not 0
result.group(1)
# 123
result.group(2)
# 1234
result.group(3)
# 12345


# Additional Regex Syntax
# or operator |
re.search(r'ios|android','I have an android device')
print(re.search(r'ios|android','I have an android device'))
# wildcard operator, putting a . before text
re.findall(r'ab','ab aba abc abcd')
# ['ab', 'ab', 'ab', 'ab']

re.findall(r'.ab','cab crab fab dab')
# ['cab', 'rab', 'fab', 'dab']

re.findall(r'..ab','cab crab fab dab')
# ['crab', ' fab', ' dab']

# ^ starts with
re.findall(r'^\d','1 this starts with a num')
# ['1']

# $ ends with
re.findall(r'\d$','this ends with a num 0')
# ['0']

sentence = 'there are 2 numbers 12 inside this 2'
pattern = r'[^\d]+'
re.findall(pattern,sentence) # number exclusion
# ['there are ', ' numbers ', ' inside this ']

punc_phrase = 'This is a string! But it has punctuation. How will you remove it?'
clean = re.findall(r'[^!.? ]+',punc_phrase)
# ['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'How', 'will', 'you', 'remove', 'it']
sentence_without_punc = ' '.join(clean)
# This is a string But it has punctuation How will you remove it

text = 'only find the hypen-words clap-ish ez'
pattern = r'[\w]+'
re.findall(pattern,text)
# ['only', 'find', 'the', 'hypen', 'words', 'clap', 'ish', 'ez']

pattern = r'[\w]+-[\w]+'
re.findall(pattern,text)
# ['hypen-words', 'clap-ish']

text = "word occurs again word"
matches = re.findall("word", text)

for match in re.finditer("word",text):
    print(match.span())


text = 'Call 123-456-7890'
phone = re.search(r'\d{3}-\d{3}-\d{4}',text)

phrase = 'Barbell'
phrasetwo = "Barpath"
phrasethree = "Barsnatch"
print(re.search(r'Bar(bell|path|snatch)',phrase))
print(re.search(r'Bar(bell|path|snatch)',phrasetwo))
print(re.search(r'Bar(bell|path|snatch)',phrasethree))

# <re.Match object; span=(0, 7), match='Barbell'>
# <re.Match object; span=(0, 7), match='Barpath'>
# <re.Match object; span=(0, 9), match='Barsnatch'>
