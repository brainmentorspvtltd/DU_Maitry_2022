Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Pen()
t.shape("turtle")
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.reset()
for i in range(4):
    t.forward(200)
    t.left(90)

    
t.reset()
for i in range(50):
    print(i)
    t.forward(5 * i)
    t.left(90)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
t.reset()
for i in range(30):
    t.circle(5 * i)
    t.left(90)

    
t.reset()
t.speed(0)
for i in range(60):
    t.circle(5 * i)
    t.left(90)

    
t.reset()
t.speed(0)
for i in range(60):
    t.circle(5 * i)
    t.left(45)

    
t.reset()
t.speed(0)
for i in range(60):
    t.circle(5 * i)
    t.left(45)

    
t.reset()
