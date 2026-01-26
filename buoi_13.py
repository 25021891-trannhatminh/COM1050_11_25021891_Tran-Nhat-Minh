
#W11A1
def reverse(path):
    try:
        f1 = open(path,'r')
        num = f1.read().strip()
        reversed_num = str(num)[::-1]
        print(reversed_num)
    except FileNotFoundError:
        print(f'Không tìm thấy {path}')
    except ValueError:
        print('Không hợp lệ')
path = input()
reverse(path)


#W11A2
def canWinNim(path):
    f1 = open(path,'r')
    stones = f1.read().strip()
    if int(stones) % 4 == 0:
        return False
    return True
path = input()
if canWinNim(path):
    print('YES')
else:
    print('NO')


#W11A3
def housesOfHogwarts(path):
    with open(path,'r') as f1:
        data = []
        for line in f1:
            data.append(line.strip())
        n = len(data)
        for i in range(1,n):
            print(data[i])
path = input()
housesOfHogwarts(path)

        
#W11A4
def anagram(path):
    try:
        with open(path,'r') as f1:
            data = []
            for line in f1:
                data.append(line.strip())
            set1 = set()
            data = [x.lower() for x in data]
            for x in data:
                x = x.replace(" ",'')
                sorted_x = "".join(sorted(x))
                set1.add(sorted_x)
            return len(set1) == 1
    except FileNotFoundError:
        print('Khong tim thay file')

path = input()
if anagram(path):
    print("True")
else:
    print('False')

#W11A5
def count(path,character):
    try:
        with open(path,'r') as f:
            data = f.read().lower()
            print(data.count(character))
    except FileNotFoundError:
        print('Khong tim thay file')
path = input()
character = input()
count(path,character)


#W11A6
def countCharacter(path,letter):
    try:
        with open(path,'r') as f:
            data = f.read().lower()
            print(data.count(letter))
    except FileNotFoundError:
        print('Khong tim thay file')
path = input()
letter = input()
countCharacter(path,letter)


#W11A7
path = input()
try:
    with open(path,'r') as f:
        print('YES')
except FileNotFoundError:
    print('NO')


#W11A8
F = [0] * 21
F[0],F[1] = 0,1
for i in range(2,21):
    F[i] = F[i-1] + F[i-2]
try:
    n = int(input())
    with open('output.txt','w') as f:
        for i in range(0,n+1):
            f.write(str(F[i]) + '\n')
    if n < 0:
        raise ValueError ("Nhập giá trị dương")
except ValueError as e:
    print(e)
            
        
#W11A9
def grade10(path):
    try:
        with open(path,'r') as f:
            data = []
            for line in f:
                data.append(line.strip().split(','))
            name = []
            for x in data:
                if x[-2] == '10':
                    name.append(x[1] + ' ' + x[2])
            for s in name:
                print(s)
    except FileNotFoundError:
        print('Khong tim thay file')
path = input()
grade10(path)   


#W11A10
def getMoney(path):
    try:
        with open(path,'r') as f:
            data = f.read().split()
        return data
    except FileNotFoundError:
        return []
def rob(houses):
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    prev2,prev1 = 0,0
    for amount in houses:
        curr = max(prev2 + amount + prev1)
        prev2 = prev1
        prev1 = curr
    return prev1
path = input()
houses = list(map(int,input().split()))
print(getMoney(path))
print(rob(houses))

#W11A11
try :
    with open('input.txt','r') as f:
        data = [int(x) for x in f.read().strip().split()]
        print(max(data), min(data),sep = " ")
except FileNotFoundError:
    print('Mission failed')


#11A12
def maximumProduct(path):
    with open(path,'r') as f:
        data = [int(x) for x in f.read().strip().split()]
        data.sort()
        if len(data) < 3:
            return 0
        product1 = data[-1] * data[-2] * data[-3]
        product2 = data[0] * data[1] * data[-1]
        return max(product1,product2)
path = input()
print(maximumProduct(path))


#W11A13
def moveZeroes(path):
    with open(path,'r') as f:
        data = [int(line.strip()) for line in f]
        data = data[1:]
        non_zero = [x for x in data if x != 0]
        count_zero = [0] * data.count(0)
        return non_zero + count_zero
path = input()
print(moveZeroes(path))


#W11A14
def averageTime(path):
    try:
        with open(path,'r') as f:
            data = [list(map(float,line.strip().split(','))) for line in f]
            average = sum(x[1] for x in data)/len(data)
            print(round(average,2))
    except FileNotFoundError:
        print('Khong tim thay file')
path = input()
averageTime(path)


#W11A15
def findMovies(path):
    try:
        with open(path,'r') as f:
            data = [list(map(str,line.strip().split(','))) for line in f]
            find = []
            for x in data:
                if float(x[-1]) >= 8.0:
                    find.append(x[1])
            if not find:
                print('All are boring!')
            else:
                for x in find:
                    print(x)
    except FileNotFoundError:
        print('Khong tim thay file')
path = input()
findMovies(path)


#W11A16
try:
    with open('input.txt','r') as f:
        lines = [line.strip() for line in f if line.strip()]
        for i in range(0,len(lines),2):
            shape = lines[i].split(':')[1].strip()
            data = lines[i+1]
            perimeter = 0.0
            if shape == "SQUARE":
                side = float(data.split(':')[1].strip())
                perimeter = 4 * side
            elif shape == 'RECTANGLE':
                size = data.split()
                width = float(size[1])
                height = float(size[3])
                perimeter = 2 *(width + height)
            elif shape == "CIRCLE":
                radius = float(data.split(':')[1].strip())
                perimeter = 2 * 3.14 * radius
            print(perimeter)
except FileNotFoundError:
    print('Không tìm thấy file')


#W11A17
def productExceptSelf(path):
    try:
        with open(path,'r') as f:
            data = [int(x) for x in f.read().strip().split()]
            data = data[1:]
            sub = 1
            for x in data:
                sub *= x
            tmp = []
            for x in data:
                tmp.append(sub//x)
        return tmp
    except FileNotFoundError:
        return 'Khong tim thay file'
path = input()
for x in productExceptSelf(path):
    print(x,end = ' ')
                

#W11A18
from math import sqrt
def estimate(path):
    try:
        with open(path,'r') as f:
            data = [line.strip() for line in f]
            x1,y1 = int(data[0].split()[2]),int(data[0].split()[4])
            x2,y2 = int(data[1].split()[2]),int(data[1].split()[4])
            speed = int(data[2].split()[1])
            
            dis = sqrt((x1-x2)**2 + (y1-y2)**2)
            time = dis/speed
            return round(time,2)
    except FileNotFoundError:
        return "Khong tim thay file" 
path = input()
print(estimate(path))
            

#W11A19
try:
    path = input()
    with open(path,'r') as f:
        data = f.read().split()
        for x in data:
            print(f"{float(x):.5f}")
except FileNotFoundError:
    print('Khong tim thay file')


#W11A20
from math import*
neighbors = [[1,0],[0,1],[1,1],[1,-1],[-1,1],[-1,0],[0,-1],[-1,-1]]
def imageSmooth(path):
    try:
        with open(path,'r') as f:
            
            data = [list(map(int,line.strip().split())) for line in f]
            m = len(data)
            matrix = [[0 for i in range(m)] for i in range(m)]
            for i in range(m):
                for j in range(m):
                    total = data[i][j]
                    k = 1
                    for x,y in neighbors:
                        i1 = i + x
                        j1 = j + y
                        if 0 <= i1 < m and 0 <= j1 < m:
                            total += data[i1][j1]
                            k += 1
                    matrix[i][j] = total //k
            for i in range(m):
                for j in range(m):
                    print(matrix[i][j],end = ' ')
                print()
    except FileNotFoundError:
        print('Khong tim thay file')
path = input()
imageSmooth(path)

