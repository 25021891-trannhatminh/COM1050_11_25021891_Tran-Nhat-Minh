#W9A1
def merge_recursive(a,b):
  if not a:
    return b
  if not b:
    return a
  res = []
  if a[0]>b[0]:
    res = [b[0]] + merge_recursive(a,b[1:])
  else:
    res = [a[0]] + merge_recursive(a[1:],b)
  return res
a= list(map(int,input().split()))
b= list(map(int,input().split()))
print(*merge_recursive(a,b))


#W9A2
def findk(a):
  res = []
  if not a:
    return []
  else:
    min_val = min(a)
    a.remove(min(a))
    res = [min_val] + findk(a)
  return res
a = []
n = int(input())
for i in range(n):
  a.extend(list(map(int,input().split())))
k = int(input())
res = findk(a)
print(res[k-1])


#W9A3
def swap_to_min(a,idx = 0):
    a = list(a)
    if idx >= len(a) - 1:
        return ''.join(a)
    target_idx = -1
    min_val = a[idx]
    for j in range(len(a) - 1,idx,-1):
        if a[j] == '0' and idx == 0:
            return swap_to_min(a,idx + 1)
        if a[j] < min_val:
            target_idx = j
            min_val = a[j]
    if target_idx != -1:
        a[idx],a[target_idx] = a[target_idx],a[idx]
        return "".join(a)
    return swap_to_min(a,idx + 1)
a = input()
print(swap_to_min(a,0))
        

#W9A4
t = int(input())
for _ in range(t):
    a = input()
    lst_a = list(a)
    b = input()
    check = True
    tmp = list(a)
    for ch in lst_a:
        if ch.upper() not in b:
            tmp.remove(ch)
    if len(tmp) != len(b):
        check = False
    else:
        a = "".join(tmp)
        if a.upper() != b:
          check = False
    if check:
        print('YES')
    else:
        print('NO')


#W9A5
a = list(map(int,input().split()))
b = list(map(int,input().split()))
n = len(a)
check = False
if n <= len(b):
    res = []
    for i in range(len(b)):
        if a[0] == b[i]:
            res.append(i)
    for x in res:
        if b[x:x+n] == a:
            check = True
            break
    if check :
        print("YES")
    else:
        print('NO')
else:
    print('NO')
    
    
#W9A6
n = int(input())
a = list(map(int,input().split()))
i = n - 2
while i >= 0 and a[i] >= a[i+1]:
    i -= 1
if i == -1:
    a.reverse()
else:
    j = n-1
    while a[j] <= a[i]:
        j -= 1
    a[i],a[j] = a[j],a[i]
    a[i+1:] = reversed(a[i+1:])
print(*a)


#W9A7
def canplaceflower(flower,k):
    
    flower = [0] + flower + [0]
    n = len(flower)
    for i in range(1,n-1):
        if flower[i] == 0 and flower[i+1] == 0 and flower[i-1] == 0:
            k -= 1
            flower[i] = 1
    return k <= 0
flower = list(map(int,input().split()))
k = int(input())
print('True' if canplaceflower(flower,k) else "False")

            
True
#W9A8
path = {'R':[0,1],'L':[0,-1],'U':[-1,0],'D':[1,0]}
a={(0,0)}
def is_path_crossing(moves):
    i,j = 0,0
    for ch in moves:
        i1 = i + path[ch][0]
        j1 = j + path[ch][1]
        if (i1,j1) in a:
            return True
        a.add((i1,j1))
        i,j = i1,j1
    return False
moves = input()
if is_path_crossing(moves):
    print('True')
else:
    print('False')

        
True
#W9A9
def Median(nums):
    a,b,c,d,e = nums
    if a > b:
        a,b=b,a
    if c>d:
        c,d=d,c
    if a>c:
        a,c=c,a
        b,d=d,b
    if e < b:
        return b
    if e > c:
        return c
    return e
nums = list(map(int,input().split()))
print(Median(nums))


#W9A10
def findRadius(houses,heaters):
    houses.sort()
    heaters.sort()
    i = 0
    r = 0
    for h in houses:
        while i < len(heaters) -1 and abs(heaters[i+1]-h) <= abs(heaters[i]-h):
            i+=1
        r = max(r,abs(heaters[i] - h))
    return r
houses = list(map(int,input().split()))
heaters = list(map(int,input().split()))
print(findRadius(houses,heaters))