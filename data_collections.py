Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
text = "hello world, this is python programming"
text = 'hello world, this is python programming'
text = """hello world, this is python programming"""
text = '''hello world, this is python programming'''
del text[3]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    del text[3]
TypeError: 'str' object doesn't support item deletion
text[0] = 'b'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    text[0] = 'b'
TypeError: 'str' object does not support item assignment
data = [101,"Ram",45000.00,"IT","Delhi"]
data[0]
101
data[0] = 102
data
[102, 'Ram', 45000.0, 'IT', 'Delhi']
del data[0]
data
['Ram', 45000.0, 'IT', 'Delhi']
x = {3,2,5,8,2,7,12,23,7,9,6,5,3,6,9,11}
x
{2, 3, 5, 6, 7, 8, 9, 11, 12, 23}
data = {"name" : "Yash", "marks" : [80,90,60], "branch" : "CSE"}
data["phone"] = 9877374842
data
{'name': 'Yash', 'marks': [80, 90, 60], 'branch': 'CSE', 'phone': 9877374842}

data["name"] = "John"
data
{'name': 'John', 'marks': [80, 90, 60], 'branch': 'CSE', 'phone': 9877374842}
x = (4,3,6,8,1,67)
x[0] = 10
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    x[0] = 10
TypeError: 'tuple' object does not support item assignment
del x[0]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
text
'hello world, this is python programming'
len(text)
39
text[0]
'h'
text[20]
' '
text[21]
'p'
text[-1]
'g'
text[-11]
'p'
text[0:20]
'hello world, this is'
text[0:20:1]
'hello world, this is'
text[0:]
'hello world, this is python programming'
text[:10]
'hello worl'
text[0:20:2]
'hlowrd hsi'
text[10:0]
''
text[10:0:-1]
'dlrow olle'
text[10::-1]
'dlrow olleh'
text[::-1]
'gnimmargorp nohtyp si siht ,dlrow olleh'
text.lower()
'hello world, this is python programming'
text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
text.capitalize()
'Hello world, this is python programming'
text.title()
'Hello World, This Is Python Programming'
text.swapcase()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
text.index('y')
22
text.count('o')
4
text.index('o')
4
text.index('o',0)
4
text.index('o',5)
7
text.index('o',8)
25
text.index('o',26)
30
text.index('z')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    text.index('z')
ValueError: substring not found
text.find('z')
-1
data = []
data.append(5)
data
[5]
data.append(11)
data
[5, 11]
data.append(7)
data
[5, 11, 7]
data.append(7,6,2,5)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    data.append(7,6,2,5)
TypeError: list.append() takes exactly one argument (4 given)
data.extend([7,6,2,5])
data
[5, 11, 7, 7, 6, 2, 5]
data.pop()
5
data
[5, 11, 7, 7, 6, 2]
data.pop(3)
7
data
[5, 11, 7, 6, 2]
data.insert(3,10)
data
[5, 11, 7, 10, 6, 2]
data.remove(0)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    data.remove(0)
ValueError: list.remove(x): x not in list
data.remove(2)
data
[5, 11, 7, 10, 6]
data.sort()
data
[5, 6, 7, 10, 11]
data.sort(reverse=True)
data
[11, 10, 7, 6, 5]
len(data)
5
