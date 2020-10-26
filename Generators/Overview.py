'''
def create_square(n):
    squares = []
    for i in range(n):
        squares.append(i**2)
    return squares
def create_square(n):
    for i in range(n):
        yield i**2
both the functions give the same result when called as follows
yield-ing is memory effiecient
'''

def create_square(n):
    for i in range(n):
        yield i**2

# def fibbo(n):
#     a=1
#     b=1
#     for i in range(n):
#         yield a
#         a,b=b,a+b

# def fibbo(n):
#     a = 1
#     b = 1
#     output = []
#     for i in range(n):
#         output.append(a)
#         a, b = b, a + b
#     return output

# for x in create_square(10):
#     print(x)
# print(list(create_square(10)))

# for number in fibbo(10):
#     print(number)

def simple_generator():
    for x in range(3):
        yield x

# for number in simple_generator():
#     print(number)

# g = simple_generator()
# print(g)
# print(next(g))

s = 'hello'
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))