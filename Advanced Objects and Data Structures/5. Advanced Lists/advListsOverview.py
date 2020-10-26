List1 = [10,20,30]

List1.append(40)
List1           # [10, 20, 30, 40]

List1.count(1)  # 0
List1.count(20) # 1

List2 = [1,2,3]
List2.append([4,5])
print(List2)        # [1, 2, 3, [4, 5]]

List2=[1,2,3]
List2.extend([4,5])
print(List2)        # [1, 2, 3, 4, 5]

List1.index(20)     # 1
List1.index(12)     # Error

List1                           # [10, 20, 30, 40]
List1.insert(2,'new element')
List1                           # [10, 20, 'new element', 30, 40]

element = List1.pop(1)  # pop the second elementment
List1                   # [10, 'new element', 30, 40]
element                 # 20

List1                   # [10, 'new element', 30, 40]
List1.remove('new element')
List1                   # [10, 30, 40]
List2 = [1,2,3,4,3]
List2.remove(3)         # removes first instance
List2                   # [1, 2, 4, 3]

List2.reverse()
List2                   # [3, 4, 2, 1]

List2                   # [3, 4, 2, 1]
List2.sort()
List2                   # [1, 2, 3, 4]

x = 'hello world'
y = x.upper()
y               # 'HELLO WORLD'


x=[1,2,3]
y = x.append(4)
print(y)        # None

x = [1,2,3]
y = x.copy()
y.append(4)
x               # [1, 2, 3]
y               # [1, 2, 3, 4]

