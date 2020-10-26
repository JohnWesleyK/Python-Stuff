from collections import Counter

List = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
Counter(List)  # Counter({5: 5, 4: 4, 3: 3, 2: 2, 1: 1})
Counter('aaabuebxub')  # Counter({'a': 3, 'b': 3, 'u': 2, 'e': 1, 'x': 1})

Sentence = 'Let us check, how many times each word shows up in this line'
Words = Sentence.split()
Counter(Words)
# Counter({'Let': 1, 'us': 1, 'check,': 1, 'how': 1, 'many': 1, 'times': 1, 'each': 1, 'word': 1, 'shows': 1, 'up': 1, 'in': 1, 'this': 1, 'line': 1})

# Methods with Counter()
co = Counter(Words)
co.most_common()
# [('Let', 1), ('us', 1), ('check,', 1), ('how', 1), ('many', 1), ('times', 1), ('each', 1), ('word', 1), ('shows', 1), ('up', 1), ('in', 1), ('this', 1), ('line', 1)]

# defaultdict
from collections import defaultdict

d = {}
d = defaultdict(object)
d['one']
for item in d:
    item    # print(item)
# initialize with default values
d = defaultdict(lambda: 0)
d['one']  # 0

# namedtuple
from collections import namedtuple

Cat = namedtuple('Cat', ['age', 'breed', 'name'])
belle = Cat(age=2, breed='Lad', name='Belle')
belle       # Cat(age=2, breed='Lab', name='Belle')
belle.age   # 2
belle.breed # Lad
belle[2]    # Belle