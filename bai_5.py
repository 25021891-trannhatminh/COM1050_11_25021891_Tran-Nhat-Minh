def W5A1(a, b):
    return max(a,b)

def W5A2(a,b):
    return b, a
def W5A3(n):
    if n < 2:
        return False
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return False
        i+=1
    return True

def W5A4(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum+=i
    return True if (sum == n) else False

def W5A5(string, num):
    arr = list(map(int,string.split()))
    for i in range (len(arr)):
        if arr[i] == num:
            return i+1
    return -1

def W5A6(n):
    if n == 0:
        return 1
    return n * W5A6(n-1)

def W5A7(string):
    a , operator , b = string.split()
    if operator == "+":
        return f"{(float(a) + float(b)):.2f}"
    elif operator == "-":
        return f"{(float(a) - float(b)):.2f}"
    elif operator == "*":
        return f"{(float(a) * float(b)):.2f}"
    else:
        return f"{(float(a) / float(b)):.2f}"

def W5A8(string):
    a , b = map(int,string.split())
    count = 0
    for i in (bin(a^b)):
        if i == "1":
            count+=1
    return count
        

def W5A9(n):
    n = int(n)
    sum = 0
    while (n != 0):
        sum += (n % 10)
        n //= 10
    return sum


def W5A10(string):
    a , b = string.split()
    check = {}
    if (len(a) != len(b)):
        return False
    for i in range (len(a)):
        if (check.get(a[i]) == None):
            check[a[i]] = b[i]
        elif (check[a[i]] != b[i]):
            return False
    return True