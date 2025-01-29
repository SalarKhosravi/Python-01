# Generators response for each yield, step by step
def func():
    return 1, 2, 3

def func_generator():
    yield 1
    yield 2
    yield 3

print(func())
print(func_generator())
print(list(func_generator()))


# create first n func that print numbers from 1 to n
def first_n(n):
    all_num = []
    num = 0
    while num < n:
        all_num.append(num)
        num += 1
    return all_num

print(first_n(100))


# do create first with Gens
def first_n_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1

for i in first_n_gen(100):
    print(i)
