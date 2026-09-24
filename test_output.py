year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

s = 'Hello, world.'
print(str(s))

print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# 字符串的 repr() 会添加引号和反斜杠：
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# repr() 的参数可以是任何 Python 对象：
repr((x, y, ('spam', 'eggs')))

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')