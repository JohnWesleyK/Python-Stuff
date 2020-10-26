import math
# help(math)
value = 5.75
math.floor(value)       # 5
math.ceil(value)        # 6
round(4.5)              # 4
round(5.5)              # 5
round(6.5)              # 6
# Python rounds based on even and odd, so that in calcutaions the result / margin of error will be levelled
math.pi                 # 3.141592653589793
math.e                  # 2.718281828459045
math.nan                # nan
math.log(math.e)        # 1.0
math.log(100,10)        # 2.0
math.sin(math.pi/2)     # 1.0
math.degrees(math.pi/4) # 45.0
math.radians(180)       # 3.141592653589793

import random 
random.randint(0,1000)

random.seed(101)
# print(random.randint(0,100))
# print(random.gauss(mu=0,sigma=1))
# print(random.uniform(a=0,b=100))

my_list = list(range(0,10))
# print(my_list)
# random.shuffle(my_list)
# print(my_list)

# The value 101 is completely arbitrary, you can pass in any number you want
# random.seed(100)
# print(random.randint(0,100))
# print(random.randint(0,100))
# print(random.randint(0,100))
# print(random.randint(0,100))
# print(random.randint(0,100))

my_list = list(range(0,25))
print(random.choices(population=my_list,k=10))
print(random.choices(population=my_list,k=10))


# my_list = list(range(0,25))
# print(random.sample(population=my_list,k=10))
# print(random.sample(population=my_list,k=10))