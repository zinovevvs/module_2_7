def print_params(a=1, b='strong', c=True):
    print(a,b,c)

print_params()

def print_params(*args):
    print(*args)

print_params(65, 45, 'strong', '94t')

def print_params(a=1, b='strong', c=True):
    print(a, b, c)

print_params(b=25, c=[1,2,3])

def print_params(a=1, b='strong', c=True):
    print(a, b, c)

values_list = [1, '32', [2,4,6]]
values_dict = {'a': 23, 'b': 398, 'c': True}
print_params(*values_list)
print_params(**values_dict)

def print_params(a=1, b='strong', c=True):
    print(a, b, c)

values_list_2 = [54.32, 'turbo']

print_params(*values_list_2, 42)
