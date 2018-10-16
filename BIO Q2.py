flipflop = input().lower()
initial = input().lower()
length = int(input())
a = ['a', 'd', 'f', 'e', True]
b = ['b', 'c', 'h', 'g', True]
position = ''
nextPoint = initial[1]
c = ['c', 'b', 'j', 'i', True]
d = ['d', 'a', 'l', 'k', True]
e = ['e', 'a', 'n', 'm', True]
f = ['f', 'a', 'o', 'n', True]
g = ['g', 'b', 'p', 'o', True]
h = ['h', 'b', 'q', 'p', True]
i = ['i', 'c', 'r', 'q', True]
j = ['j', 'c', 's', 'r', True]
k = ['k', 'd', 't', 's', True]
l = ['l', 'd', 'm', 't', True]
m = ['m','u', 'l', 'e', True]
n = ['n','u', 'e', 'f', True]
o = ['o','v', 'f', 'g', True]
p = ['p','v', 'g', 'h', True]
q = ['q','w', 'h', 'i', True]
r = ['r','w', 'i', 'j', True]
s = ['s','x', 'j', 'k', True]
t = ['t','x', 'k', 'l', True]
u = ['u','v', 'm', 'n', True]
v = ['v','u', 'o', 'p', True]
w = ['w','x', 'q', 'r', True]
x = ['x','w', 's', 't', True]


points = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x]
for i in range(len(points)):
    check = points[i]
    check.append('l')
for i in range(len(points)):
    check = points[i]
    for j in flipflop:
        if check[0] == j:
            check[4] = False



for i in range(length):
    exec('if ' + nextPoint + '[4] == False:\n   if ' + nextPoint + '[5] == l:\n        position = nextPoint' + '\n        ' + position + '[5] = "r"\n       nextPoint = '
         + position + '[1]\n    elif ' + nextPoint + '[5] == r:\n        position = nextPoint\n        ' + position + '[5] = "l"' + '\n        nextPoint = '
         + position + '[2]')



