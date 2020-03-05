from itertools import permutations
num=input()
l1=num.split(',')
l2=[]
n=l1.sort()
for i in range(len(l1)):
    n=max(l1)
    l2.append(n)
    l1.pop()
perm = permutations(l2, 3)
count=0
a=[]
for i in list(perm):
  a.append(i)
b = set()
unique = []
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
for i in range(len(unique)):
  count=count+1
l=len(l2)
if(l<4):
    print(''.join(l2),',',count)
else:
    h=l2[0:3]
    print(''.join(h),',',count)
