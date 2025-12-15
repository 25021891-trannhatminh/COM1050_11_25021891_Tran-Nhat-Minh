#W4A1
sum = 0
for i in range (int(input())+ 1):
    sum += i
print(sum)

#W4A2
while (True):
    n = int(input())
    if (n > 0):
        break
for i in range (2,n**0.5):
    if (n % i == 0):
        print ("False")
    else: 
        print("True")

#W4A3
result = 1
for i in range(1,int(input())+1):
    result *= i
print(result)

#W4A4
n = int(input())
n = abs(n)
count = 0
while (n > 0):
    count +=1
    n = n // 10
print (count)

#W4A5
n = int(input())
numbers = input()
if len(numbers.split()) == n:
    list = [int(x) for x in numbers.split()]
else:
    exit()

check = 0
for i in list:
    if i == 42:
        print("I've found the meaning of life!")
        check = 1
        break
if check == 0:
    print("It's a joke!")

#W4A6
list = list(map(int,input().split()))
if len(list) != 2:
    exit()
def isPrime (n):
    if n < 2:
        return False
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return False
        i+=1
    return True

sum = 0
for i in range(list[0],list[1]):
    if isPrime(i):
        sum+=i
print(sum)

#W4A7
n = int(input())
if n < 2:
    exit()
def isPrime (n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return False
        i+=1
    return True
i = n
while i >= 1:
    if n % i == 0 and isPrime(i):
        print(int(i))
        break
    i-=1

#W4A8
n = int(input())
def reverse(n):    
    result = 0
    while (n != 0):
        result += (n % 10)*(10**(len(str(n))-1))
        n = n // 10
    return result
count = 0
while (n != reverse(n)):
    n+= reverse(n)
    count+=1
print(count , n)

#W4A9
n = int(input())
arr = []
i = 1
while (i < n**0.5):
    arr.append(i**2)
    i+=1
for i in arr:
    print(i, end = " ")

#W4A26


#W4A27
n = input()
count = 1 if (n[0] != " ") else 0
temp = ""
for i in n:
    if temp == " " and i != " ":
        count += 1
    temp = i
print(count)

#W4A28
n = input()
checkfirst = 0
for i in n:
    if (i != " "):
        checkfirst = 1
    if checkfirst == 1:
        if i == " ":
            break 
        print(i,end="")

#W4A29
arr = list(input().split(", "))
sum = 0
for i in arr:
    sum+= int(i)
print(sum)
#W4A30
n = input()
lower = 0
upper = 0
number = 0
for i in n:
    if (i.islower()):
        lower+=1
    if (i.isupper()):
        upper+=1
    if (i.isnumeric()):
        number+=1
print("Upper: " , upper)
print("Lower: " , lower)
print("Number: " , number)

#W4A31
n = input()
sum = 0
for i in n:
    if (i.isnumeric()):
        sum += int(i)
print(sum)

#W4A32
n = input()
lower = 0
upper = 0
sign = 0
number = 0
for i in n:
    if (32 <= ord(i) <= 47 or 58 <= ord(i) <= 64 or 91 <= ord(i) <= 96 or 123 <= ord(i)):
        sign+=1
    if (48 <= ord(i) <= 57):
        number+=1
    if (65 <= ord(i) <= 90):
        upper+=1
    if (97 <= ord(i) <= 122):
        lower+=1
print(True if (len(n) > 6 and lower!= 0 and upper!=0 and sign != 0 and number!=0) else False)

#W4A33
n = input()
first = len(n) % 3
for i in range(first):
    print(n[i],end="")
print(".",end="")
i = 0
while i + first < len(n):
    if (i % 3 == 0 and i != 0):
        print(".", end="")
    print(n[i+first],end="")
    i+=1

#W4A34
a = input()
b = input()
arr = []
for i in range (len(a)):
    if (i < a.find(b) or i >= a.find(b) + len(b)):
        arr.append(a[i])
for i in arr:
    print(i, end = "")