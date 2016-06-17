x = range(5)
print(x)

a, b, *rest = x
print(a)
print(b)
print(rest)

t = (1, 2, [3, 4])
t[2].extend([50, 60])
print(t)
