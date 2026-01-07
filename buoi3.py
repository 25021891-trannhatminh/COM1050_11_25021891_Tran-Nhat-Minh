#1
number = input()
print(number[::-1])

#2
list1 = list(map(int,input().split()))
list1[0] = list1[0] ^ list1[1]
list1[1] = list1[0] ^ list1[1]
list1[0] = list1[0] ^ list1[1]
print (list1[0] , list1[1])

#3
n = int(input())
if ( n & (n-1) == 0):
    print(True)
else:
    print(False)

#4
list2 = list(map(int,input().split()))
print(list2[0] // list2[1])

#5
list3 = list(map(int,input().split()))
print(int((list3[0] / list3[1]) + 0.5))

#6
m = int(input())
print("Even" if (m % 2 == 0) else "Odd")

#7
list4 = list(map(int,input().split()))
print("Yes" if (list4[0] < 0 and list4[1] < 0) else "No")

#8
a = input()
b = input()
print("True" if(len(a) > len(b)) else "False")

#9
a = int(input())
b = int(input())
c = int(input())
print("Yes" if (a + b > c and a + c > b and b + c > a  and a >0 and b > 0 and c > 0 )else "No")

#10
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(max(a,b,c,d))

#11
a = int(input())
b = int(input())
c = int(input())
if not (a + b > c and a + c > b and b + c > a  and a >0 and b > 0 and c > 0 ):
    print ("Không phải tam giác")
elif (a == b and b == c):
    print("Tam giác đều")
elif ((a == b != c ) or (b == c != a) or (c == a != b)):
    print("Tam giác cân")
else: 
    print("Tam giác thường")

#12
year = int(input())
print("Yes" if (year % 4 == 0 and year % 100 != 0) else "No")

#13 
kWh = int(input())
if (0 <= kWh <= 50):
    print(1500*kWh)
elif (51 <= kWh <= 100):
    print(50*1500 + (kWh-50)*2000)
else:
    print(50*1500 + 50*2000 + (kWh-100)*3000)

#14
a = float(input())
b = float(input())
if (a == 0 and b != 0):
    print("Vô nghiệm")
elif (a == 0 and b == 0):
    print("Vô số nghiệm")
else:
    print(f"{-b/a :.2f}")

#15
mark = float(input())
if (mark >= 8):
    print ("Giỏi")
elif (mark >= 6.5):
    print("Khá")
elif (mark >= 5):
    print("Trung bình")
else:
    print("Yếu")

#16
n = float(input())
print(((int(n) + 1 if (n != int(n))else (int(n))), int(n), int(n+0.5)) if (n > 0) else (int(n),(int(n) - 1 if (n != int(n))else (n)),int(n-0.5)))

