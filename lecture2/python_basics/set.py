s = set()
x = int(input())

s.add(1)
s.add(3)
s.add(5)
s.add(3)

for i in range(x):
    s.add(i)
    
print(s)