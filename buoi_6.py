
#W6A1
A=list(map(int,input().split()))
def W6A1(A):
     B=[]
     for i in A:
          if i not in B:
               B.append(i)
     return B

print(W6A1(A))   

#W6A2
A=list(map(int,input().split()))
def W6A2(A):
     B=[]
     bp=0

     for i in range(len(A)):
          for a in range(i+1):
               bp+=A[a]
          B.append(bp)
          bp=0
     return B 

print(W6A2(A))  
       
#W6A3
A=list(map(int,input().split()))
k=int(input())
def W6A3(A,k):
     for i in range(k):
          A.append(A[0])
          A.pop(0)
     return tuple(A)     
#W6A4
A=list(map(str,input().split()))
B={}
def W6A4(A):
     for i in A:
          a,b=map(str,i.split(":"))
          if a not in B:B[a]=[b]
          else: B[a]+=[b]
     return B

print(W6A4(A))    
{'name': ['Alice', 'Bob'], 'age': ['20']}
#W6A5
A=list(map(int,input().split()))
def W6A5(A):
     B={'positives':0,'negatives':0,'zeros':0}
     for i in A:
          if i>0:B['positives']+=1
          elif i<0:B['negatives']+=1
          else:B['zeros']+=1
     return B

print(W6A5(A))    
#W6A6
A=list(map(int,input().split()))
def W6A6(A):
     return sum(A)

print(W6A6(A))
#W6A7
A=list(map(int,input().split()))
def W6A7(A):
     return A[0] , A[-1] ,tuple(map(str,reversed(A)))
a,b,c = W6A7(A)

print(a,b,c)
#W6A8
A=list(map(str,input().split()))
B={}
def W6A9(A):
     for i in A:
          if i not in B: B[i]=1
          else:B[i]+=1
     return B 

print(W6A9(A))    
{'apple': 2, 'banana': 1}
#W6A9
A=input()
B=input()

def chuyen_dict(A):
     a=[]
     b={}
     for i in A:
          if i!="{" and i!="}" and i!="," and i!=":" and i!="'"and i!=" ":
               a.append(i)
     for i in range(0,len(a),2):
          b[a[i]]=int(a[i+1])
     return b     
     
def W6A9(A,B):
     A=chuyen_dict(A)
     B=chuyen_dict(B)
     for i in A:
          if i in B:B[i]=(B[i]+A[i])
          else:B[i]=A[i]
     return B

print(W6A9(A,B))   
#W6A10
A=list(map(int,input().split()))
k=int(input())
def W6A10(A,k):
     Tuple=[]
     for i in range(len(A)):
          for a in range(i+1,len(A)):
               if A[i]+A[a]==k and (A[i],A[a])not in Tuple:Tuple.append((A[i],A[a]))
     Tuple.sort(key=lambda x:x[0]) 
     return Tuple
 
print(W6A10(A,k))      
#W6A11
A=list(map(int,input().split()))
def W6A11(A):
     chan=()
     le=()
     for i in A:
          if i%2==0:chan.__add__(i)
          else:le.__add__(i)
     return chan,le
chan,le=W6A11(A)
print(chan,le)     
#W6A12
A=list(map(int,input().split()))
def W6A12(A):
     so_lan=0
     phan_tu=A[0]
     for i in A:
          if A.count(i)>so_lan or (A.count(i)==so_lan and i<phan_tu):
               so_lan=A.count(i)
               phan_tu=i
     return phan_tu          
#W6A13
A=list(map(str,input().split()))
def W6A13(A):
     B={}
     for i in range(1,len(A),2):
          B[A[i]]=A[i-1]
     return B
#W6A14
A=list(map(int,input().split()))
B=list(map(int,input().split()))
def W6A14(A,B):
     C=[]
     for i in A:
          if i in B:C.append(i)
     return C     
#W6A15
A=list(map(str,input().split()))
k=int(input())
def W6A15(A,k):
     B={}
     for i in range(1,len(A),2):
          if int(A[i])>k:B[A[i-1]]=A[i]
     return B     
#W6A16
n,m=map(int,input().split())
A=[]
for i in range(n):
     A.append(list(map(int,input().split())))

for i in range(n):
     for i in range(m):
          print(f"{A[n][m]:>4}",end="")
     print()     
#W6A17
n=int(input())
A=[]
for i in range(n):
     A.append(list(map(int,input().split())))

for i in range(n):
     print(A[i][i],end=" ")
print()     
for i in range(n):
     print(A[n-1-i][n-1-i],end=" ")
#W6A18
n,m,k=map(int,input().split())
A=[]
for i in range(n):
     A.append(list(map(int,input().split())))
tong=0
for i in range(n):
     tong+=A[i][k]
print(tong)     
#W6A19
A=list(map(int,input().split()))
def W6A19(A):
     return A.index(max(A))+1
#W6A20
A=list(map(int,input().split()))
k=int(input())
def W6A20(A,k):
     if k in A:return A.index(k)+1
     else:return -1
#W6A21
A=list(map(str,input().split()))
def W6A21(A):
     B={}
     for a,b in enumerate(A):
          if b not in B:B[b]=(a,)
          else:B[b]+=(a,)
     return B     
#W6A22
A=list(map(int,input().split()))
def W6A22(A):
     return A.index(max(A))+1