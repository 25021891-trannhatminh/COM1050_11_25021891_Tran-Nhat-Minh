#W8A1
try:
  a,b = map(int,input().split())
  print('%.2f' % (a/b))
except ZeroDivisionError:
  print("Loi chia khong")


#W8A2

try:
    lst = list(map(int,input().split()))
    n = int(input())
    print(lst[n])
except IndexError:
    print("Index out of range")

#W8A3
def happy_num(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    return n == 1
try:
    a = int(input())
    if happy_num(a):
        print('YES')
    else:
        print('NO')

except ValueError:
    print('Nhập vào 1 số nguyên dương')


#W8A4
try:
    a,b = map(int,input().split())
    sum = a + b

except ValueError:
    print('Nhập sai giá trị')
else:
    print(sum)
finally:
    print('Kết thúc chương trình sau khi chạy')


#W8A5
a = input().split(" ")
convert_a = []
for x in a:
    try:
        x = int(float(x))
        convert_a.append(x)
    except:
        print(f'Không chuyển {x} sang int được')
print(convert_a)


#W10A6
from math import*
try:
    n = int(input())
    print(f'{sqrt(n):.2f}')
except ValueError:
    print('So am')


#W10A7
try:
    age = int(input())
    if age < 0 :
        raise ValueError
except ValueError:
    print('Tuoi khong hop le')
else:
    print(2025 - age)


#W10A8
try:
    file = input().lower()
    if file[-3:] not in ['txt','zip']:
        raise ValueError
except ValueError:
    print('File khong hop le')
else:
    print('Doc file thanh cong')


#W10A9
try :
    s = input()
    n = int(s)
    print(n)
except ValueError:
    print('Chuoi khong hop le')


#W10A10
try:
    a = list(map(int,input().split()))
    n=a[0]
    a = a[1:]
    if len(a) != len(set(a)):
        raise ValueError
    print(sum(a))
except ValueError:
    print('Mang khong hop le')


#W8A11
import re

try:
    t = int(input())
    
    for _ in range(t):
        s = input().strip()
        try:
            re.compile(s)
            print("Valid")
        except re.error:
            print("Invalid")
except EOFError:
    pass