#Name Shuffler

"""
def name_shuffler(str_):
    return ' '.join((str_.split())[::-1])

print(name_shuffler('john McClane'))
"""

#Capitalization and Mutability

"""
def capitalize_word (word : str):
    return word.title()

print(capitalize_word("nimadur"))
"""

#Multiplication table for number

"""
def multi_table(n):
    str = []
    for i in range(1, 11):
        str.append(f'{i} * {n} = {i*n}')
    return '\n'.join(str)

print(multi_table(3))
"""

#Welcome to the City
"""
def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"

print(say_hello(["Humoyun"], "Yunusabad", "Tashkent"))
"""


#Exclamation marks series #1: Remove an exclamation mark from the end of string

"""
def remove(s):
    return s if len(s)==0 else s[:-1] if s[-1]=='!' else s

print(remove("Hello!!!"))
"""

