#W7A1
def binary_search(arr,l,r,k):
  while l<=r:
    m=(l+r)//2
    if arr[m] == k:
      return True
    elif arr[m] < k:
      l=m+1
    else:
      r=m-1
  return False
arr = list(map(int,input().split()))
k=int(input())
if binary_search(arr,0,len(arr)-1,k):
  print(arr.index(k))
else:
  print(-1)


#W7A2
def count_occurrences(arr,k):
  cnt = 0
  for x in arr:
    if x == k:
      cnt += 1
  return cnt
arr = list(map(int,input().split()))
k = int(input())
print(count_occurrences(arr,k))


#W7A3
def bubble_sort(arr):
  n=len(arr)
  for i in range(n):
    swap = False
    for j in range(0,n-i-1):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
        swap = True
    if not swap:
        break
  return arr
def selection_sort(arr):
  n=len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i+1,n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i],arr[min_idx] = arr[min_idx],arr[i]
  return arr


arr = list(map(int,input().split()))
print(' '.join(map(str,bubble_sort(arr))))
print(' '.join(map(str,selection_sort(arr))))


#W7A4
def max_count(a):
  d=dict({})
  for x in a:
    d[x] = d.get(x,0)+1
  max_fre = max(d.values())
  for k,v in d.items():
    if v == max_fre:
      return f"{k} xuat hien nhieu nhat,som nhat,{v} lan"
a = list(map(int,input().split()))
print(max_count(a))


#W7A5
s=list(map(int,input().split()))
x=int(input())
n=len(s)
cnt=0
for i in range(n):
  for j in range(i+1,n):
    if s[i] + s[j] == x:
      cnt+=1
print(cnt)

#W7A6
a = eval(input())
n=len(a)
b=[]
for x in a:
  for i in x:
    b.append(i)
print(b)


#W7A7
a = eval(input())
n = len(a)
dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))


#W7A8

a=eval(input())
q=eval(input())
d=[]
for x in q:
    min_l = 10**18
    found= False
    for k in a:
        if k[0] <= x <= k[1]:
            found = True
            leng = k[1] - k[0] + 1
            if leng < min_l:
                min_l = leng
    if not found:
        min_l = -1
    d.append(min_l)
print(d)


#W7A9
a=eval(input())
n=len(a)
d=[0 for i in range(n)]
for i in range(n):
    k=a[i+1:]
    for x in k:
        if x < a[i]:
            d[i]+=1
print(d)


#W7A10
a=eval(input())
m=int(input())
n=len(a)
max_mod = 0
for i in range(n):
    for j in range(i+1,n):
        tong = sum(a[i:j+1])
        mod = tong % 7
        if mod > max_mod:
            max_mod = mod
print(max_mod)


#W7A11
s=input().strip()
k=input().strip()
a=s.split()
cnt=0
for x in a:
    if x == k:
        cnt += 1
print(cnt)


#W7A12
a=input()
b=input()
c=input()
d=input()
s=[(a,'A'),(b,'B'),(c,'C'),(d,'D')]
s.sort(key = lambda x : x[0].lower())
for x in s:
    print(x[1],end=' ')


#w7A13
def harmonic_sequence(a):
    a.sort()
    b=list(set(a))
    b.sort()
    max_len=0
    for i in range(len(b)-1):
        if b[i+1] - b[i] == 1:
            leng = a.count(b[i]) + a.count(b[i]+1)
            if leng > max_len:
                max_len = leng
    return max_len
a=list(map(int,input().split()))
print(harmonic_sequence(a))


#W7A14
n=int(input())
a=list(map(int,input().split()))
d=[]
found= False
for i in range(n):
    if a[i] == 7:
        found = True
        d.append(i)
if found:
    d.sort(reverse= True)
    print(' '.join(map(str,d)))
else:
    print(-1)


#W7A15
from sys import stdin
n=int(input())
a=[]
for _ in range(n):
    a.append(input())
idx = a.index('Nemo')
print(f"{a[idx-1]} and {a[idx + 1]}")


    
    
    

            
            