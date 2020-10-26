def func_one(n):
    return [str(num) for num in range(n)]

func_one(10)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def func_two(n):
    return list(map(str,range(n)))
func_two(10)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

import time

# Current time before running
start_time = time.time()

# Run code
result = func_one(10000)

# Current time after running
end_time = time.time()

# elapsed time
elapsed_time = end_time - start_time

print(end_time)
print(elapsed_time)

# Current time before running
start_time = time.time()

# Run code
result = func_two(10000)

# Current time after running
end_time = time.time()

# elapsed time
elapsed_time = end_time - start_time

print(elapsed_time)

import timeit
stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
# timeit.timeit(stmt,setup,number=100000)
# 5.769111
print(timeit.timeit(stmt,setup,number=100000))

stmt = '''
func_two(100)
'''
setup = '''
def func_two(n):
    return list(map(str,range(n)))
'''
# timeit.timeit(stmt,setup,number=100000)
# 4.3454992
print(timeit.timeit(stmt,setup,number=100000))