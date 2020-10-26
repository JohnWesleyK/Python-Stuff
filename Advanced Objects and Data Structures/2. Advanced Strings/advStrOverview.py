str = 'ez clap'
str.capitalize()    # 'Ez clap'
str.upper()         # 'EZ CLAP'
str.lower()         # 'ez clap'

str                 # 'ez clap'
str = str.upper()
str                 # 'EZ CLAP'
str = str.lower()
str                 # 'ez clap'

# returns the number of occurrences, without overlap
str.count('z')      # 1

# returns the starting index position of the first occurence
str.find('a')       # 5


str.center(11,'-')  # '--ez clap--'

'tabs\ttabs'.expandtabs()   # 'tabs    tabs'

str = 'nospace'
str.isalnum()       # True
str.isalpha()       # True
str.islower()       # True
str.isspace()       # False
str.istitle()       # False
str.isupper()       # False
str.endswith('e')   # True

str = 'nospace'
str.split('p')      # ['nos', 'ace']
str.partition('p')  # ('nos', 'p', 'ace')