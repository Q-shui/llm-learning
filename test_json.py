import test

# 这是第一条注释
spam = 1  # 而这是第二条注释
          # ... 而这是第三条！
text = "# 这不是注释因为它是在引号之内。"
print("111")
'''
print("hello")
'''

'''
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
'''
'''
# 度量一些字符串：
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
'''

# 创建示例多项集
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

#如果在遍历字典，就不能改变字典的数量，只能遍历字典的副本
'''
for usr in users:
    if users[usr] == 'inactive':
        del users[usr]  # 这会引发 RuntimeError

print(users)

# 策略：迭代一个副本
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# 策略：创建一个新多项集
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # 循环到底未找到一个因数
        print(n, 'is a prime number')

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

#while True:
#    pass  # 无限等待键盘中断 (Ctrl+C)

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(http_error(400))

# point 是一个 (x, y) 元组

class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
var = 1
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

def fib(n):    # 打印小于 n 的斐波那契数列
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# 现在调用我们刚定义的函数：
fib(2000)

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#ask_ok('Do you really want to quit?')

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
#普通参数
def standard_arg(arg):
    print(arg)

#只允许位置参数
def pos_only_arg(arg, /):
    print(arg)

#arg只允许关键字参数
def kwd_only_arg(*, arg):
    print(arg)

#第一个是位置参数，第二个都可以，第三个只允许关键字参数
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

#把没有被前面参数接收的其他关键字参数，统一收集到一个字典 kwds 中。
#foo("Tom", name="Jack")
#此时python会认为你给name传了两次值
def foo(name, **kwds):
    return 'name' in kwds

def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")

concat("earth", "mars", "venus", sep=".")

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

#返回一个函数
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)

f(1)

#文档字符串是写在函数内部第一行的用于解释函数的
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything:

        >>> my_function()
        >>>
    """
    pass

print(my_function.__doc__)


#函数注解是指明参数类型，返回值类型的
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana')

fruits.index('banana', 4)  # 从 4 号位开始查找下一个 banana

fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.sort()
fruits

fruits.pop()

#numbers = [1, 2, 3, 4, 5, 6]

#带条件的
#result = [x for x in numbers if x % 2 == 0]
numbers = [-2, -1, 0, 1, 2]
print([x for x in numbers if x > 0])#实际上挑选部分元素
print([x if x > 0 else 0 for x in numbers])#实际上还是挑选整个数组
[x for x in range(20) if x > 5 if x % 2 == 0]

dict(sape=4139, guido=4127, jack=4098)
{x: x**2 for x in (2, 4, 6)}

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

print(dir())