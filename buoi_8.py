
#W8A1
class Cylinder:
  def __init__(self,r,h):
    self.h=h
    self.r=r
  def thetich(self):
    return 3.14*((self.r)**2)*(self.h)
  def dientich(self):
    return (2*3.14*(self.r)*(self.h)+2*3.14*((self.r)**2))
  def __str__(self):
    return f'Diên tích là {self.dientich():.2f} , Thể tích là {self.thetich():.2f}'
  
s=Cylinder(float(input('Nhập bán kính : ')),float(input('Nhập chiều cao : ')))
print(s)


#W8A2
class Date:
    def __init__(self, birth):
        self.birth = birth
    def chuanhoa(self):
        if self.birth[1] == '/':
            self.birth = '0' + self.birth
        if self.birth[4] == '/':
            self.birth = self.birth[0:3] + '0' + self.birth[3:]
    def is_valid(self):
        self.chuanhoa()
        try:
            day = int(self.birth[0:2])
            month = int(self.birth[3:5])
            year = int(self.birth[6:]) 
            days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                days_in_month[2] = 29  
            return 1 <= month <= 12 and 1 <= day <= days_in_month[month]
        except:
            return False
    def next_day(self):
        if not self.is_valid():
            print("INVALID")
            return
        day = int(self.birth[0:2])
        month = int(self.birth[3:5])
        year = int(self.birth[6:])
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[2] = 29
        day += 1
        if day > days_in_month[month]:
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
        print(f"{day:02d}/{month:02d}/{year:04d}")
s = Date(input().strip())
s.next_day()

#W8A3
from math import*
class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def __str__(self):
    return "%.2f" %(sqrt(self.x**2 + self.y**2))
s=Point(int(input('Nhập x : ')),int(input('Nhập y : ')))
if s.x == 0 and s.y == 0 :
  print('M là gốc tọa độ')
else:
  print(s)

#W8A4
class Calculator:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def add(self):
    return self.x+self.y
  def subtract(self):
    return self.x - self.y
  def product(self):
    return self.x*self.y
  def divide(self):
    if self.y == 0:
      return 'Không hợp lệ'
    else:
      return self.x /self.y
  def power(self):
    return self.x ** self.y
  def mod(self):
    return self.x % self.y
  def set_numbers(self,new_x,new_y):
    self.x=new_x
    self.y=new_y
  def menu(self):
    print('1:Phép cộng')
    print('2:Phép trừ')
    print('3:Phép nhân')
    print('4:Phép chia')
    print('5:Phép lũy thừa')
    print('6:Phép chia dư')
    print('7:Cập nhật số mới')
    n=input("Nhập mục cần tìm ")
    while 1:
      if n == '1':
        print(self.add())
      elif n == '2':
        print(self.subtract())
      elif n == '3':
        print(self.product())
      elif n == '4':
        print(self.divide())
      elif n =='5':
        print(self.power())
      elif n == '6':
        print(self.mod())
      elif n =='7':
        self.set_numbers(int(input('Nhập x mới : ')),int(input('Nhập y mới : ')))
      elif n == 'yes' or n =='YES' or n == 'Yes':
        break
      n=input('Nhập mục cần tìm ')
s=Calculator(int(input('Nhập x : ')),int(input('Nhập y :')))
s.menu()

#W8A5
class ShoppingCart:
  def __init__(self):
    self.items = []
  def add(self,name,price):
    self.items.append((name,price))
  def remove_item(self,name,price):
    try:
      self.items.remove((name, price))
      print("Đã xóa sản phẩm")
    except ValueError:
      print("Không tìm thấy sản phẩm")
  def check(self):
    if not self.items:
      return 'Giỏ hàng rỗng'
    else:
      return 'Giỏ hàng không rỗng'
  def sum_price(self):
    return sum(y for x,y in self.items)
  def show_all(self):
    if not self.items:
      print('Giỏ hàng rỗng')
    else:
      for name,price in self.items:
        print(f'{name} - {price}')
  def remove_all(self):
    self.items = []
    print('Đã xóa thành công')
  def menu(self):
    print('1:Thêm vào giỏ hàng')
    print('2:Xóa khỏi giỏ hàng')
    print('3:Kiểm tra giỏ hàng')
    print('4:Tổng giá trị')
    print('5:Hiển thị toàn bộ giỏ hàng')
    print('6:Xóa toàn bộ giỏ hàng')
    n=input('Chọn mục : ')
    while 1:
      if n == '1':
        self.add(input('Nhập tên sản phẩm '),int(input('Nhập giá sản phẩm ')))
      elif n == '2':
        self.remove_item(input('Nhập tên sản phẩm '),int(input('Nhập giá sản phẩm ')))
      elif n == '3':
        print(self.check())
      elif n == '4':
        print(self.sum_price())
      elif n == '5':
        self.show_all()
      elif n == '6':
        self.remove_all()
      elif n == 'yes':
        break
      n=input('Chọn mục : ')

s=ShoppingCart()
s.menu()

#W8A6
class Rectangle:
  def __init__(self,w,h,k):
    self.w =w
    self.h=h
    self.k=k
  def area(self):
    return '%.2f' %((self.w * self.h)*self.k*self.k)
  def perimeter(self):
    return '%.2f' %((self.h+self.w)*self.k*2)
  
w,h,k=map(float,input().split())
s=Rectangle(w,h,k)
print(s.area(),s.perimeter(),sep=' ')

#W8A7
from math import*
class Fraction:
  def __init__(self,tu_1,mau_1,oper,tu_2,mau_2):
    self.tu_1=tu_1
    self.tu_2=tu_2
    if mau_1 == 0 or mau_2 == 0:
      raise ValueError('Mẫu khác 0')
    self.mau_2=mau_2
    self.mau_1=mau_1
    self.oper = oper
  def add(self):
    if self.mau_1 == self.mau_2:
      return f'{(self.tu_1+self.tu_2)//gcd(self.tu_1+self.tu_2,self.mau_1)}/{self.mau_1}'
    else:
      bcnn = lcm(self.mau_1,self.mau_2)
      self.tu_1 = bcnn // self.mau_1
      self.tu_2 = bcnn // self.mau_2
      return f'{(self.tu_1 + self.tu_2)//gcd(self.tu_1 + self.tu_2,bcnn)}/{bcnn // gcd(self.tu_1 + self.tu_2,bcnn)}'
  def sub(self):
    if self.mau_1 == self.mau_2:
      return f'{(self.tu_1-self.tu_2)//gcd(self.tu_1-self.tu_2,self.mau_1)}/{self.mau_1}'
    else:
      bcnn = lcm(self.mau_1,self.mau_2)
      self.tu_1 = bcnn // self.mau_1
      self.tu_2 = bcnn // self.mau_2
      return f'{(self.tu_1 - self.tu_2)//gcd(self.tu_1 - self.tu_2,bcnn)}/{bcnn // gcd(self.tu_1 - self.tu_2,bcnn)}'
  def mul(self):
    return f'{(self.tu_1 * self.tu_2)//gcd(self.tu_1 * self.tu_2,self.mau_1 * self.mau_2)}/{(self.mau_1 * self.mau_2)//gcd(self.tu_1 * self.tu_2,self.mau_1 * self.mau_2)}'
  def div(self):
    return f'{(self.tu_1 * self.mau_2)//gcd(self.tu_1 * self.mau_2,self.tu_2 * self.mau_1)}/{(self.mau_1 * self.tu_2)//gcd(self.tu_1 * self.mau_2,self.tu_2 * self.mau_1)}'
  def menu(self):
    if self.oper == '+':
      print(self.add())
    elif self.oper == '-':
      print(self.sub())
    elif self.oper == '*':
      print(self.mul())
    elif self.oper == '/':
      print(self.div())

tu_1,mau_1,oper,tu_2,mau_2 = map(str,input().split())
s=Fraction(int(tu_1),int(mau_1),oper,int(tu_2),int(mau_2))
s.menu()
#W8A8
class BankAccount:
  def __init__(self,owner,balance):
    self.owner=owner
    self.balance=balance
  def deposit(self,dep):
    self.balance += dep
  def withdraw(self,wdr):
    if self.balance >= wdr:
      self.balance -= wdr
  def __str__(self):
    return ('%.2f' %self.balance)
owner,balance = map(str,input().split())
s=BankAccount(owner,float(balance))
n=int(input())
for _ in range(n):
  method, money = map(str,input().split())
  money = float(money)
  if method == 'WITHDRAW':
    s.withdraw(money)
  elif method == 'DEPOSIT':
    s.deposit(money)
print(s)

#W8A9
class Student:
  def __init__(self,name):
    self.name = name
    self.scores = []
  def add(self,sub,score):
    self.scores.append((sub,score))
  def avg(self):
    b=[x[1] for x in self.scores]
    return round(sum(b)/len(b),2)
  def rank(self):
    if self.avg() >=8:
      return 'Excellent'
    elif 6.5<=self.avg() < 8:
      return 'Good'
    elif 5 <= self.avg() < 6.5:
      return 'Average'
    else:
      return 'Poor'
name=input()
s=Student(name)
n=int(input())
for _ in range(n):
  sub,score = map(str,input().split())
  s.add(sub,float(score))
print(f'{name} {s.avg():.2f} {s.rank()}')

#W8A10
a=[]
class Book:
  def __init__(self):
    self.items = []
class Library(Book):
  def __init__(self):
    super().__init__()
  def add(self,title,author,year):
    self.items.append([title,author,year])
    return self.items
n=int(input())
s = Library()
for i in range(n):
  if 0<= i <= n-2:
    title,author,year = map(str,input().split(';'))
    s.add(title,author,year)
  else:
    k = input().split()
    sum = 0
    if k[0] == 'COUNT':
      a = [x[1] for x in s.items]
      for x in a:
        if x == k[1]:
          sum += 1
    elif k[0] == "COUNTYEAR":
      a=[x[2] for x in s.items]
      for x in a:
        if int(x) == int(k[1]):
          sum += 1
    print(sum)

#W8A11
from math import*
class space:
  def __init__(self,a1,a2,a3,b1,b2,b3,c1,c2,c3,d1,d2,d3):
    self.a1=a1
    self.a2=a2
    self.a3=a3
    self.b1=b1
    self.b2=b2
    self.b3=b3
    self.c1=c1
    self.c2=c2
    self.c3=c3
    self.d1=d1
    self.d2=d2
    self.d3=d3
  def mp1(self):
    n1,n2,n3=self.a1-self.b1,self.a2-self.b2,self.a3-self.b3
    k1,k2,k3=self.a1-self.c1,self.a2-self.c2,self.a3-self.c3
    return [n2*k3-k2*n3,n3*k1-k3*n1,n1*k2-k1*n2]
  def mp2(self):
    n1,n2,n3=self.c1-self.b1,self.c2-self.b2,self.c3-self.b3
    k1,k2,k3=self.d1-self.c1,self.d2-self.c2,self.d3-self.c3
    return [n2*k3-k2*n3,n3*k1-k3*n1,n1*k2-k1*n2]
  def goc(self):
    a,b,c=self.mp1()
    x,y,z=self.mp2()
    tu = abs(a*x + b*y + c*z)
    mau= sqrt(a**2 + b**2 +c**2) * sqrt(x**2 +y**2 +z**2)
    return round(degrees(acos(tu/mau)),2)
a1,a2,a3 = map(float,input().split())
b1,b2,b3 = map(float,input().split())
c1,c2,c3 = map(float,input().split())
d1,d2,d3 = map(float,input().split())
s = space(a1,a2,a3,b1,b2,b3,c1,c2,c3,d1,d2,d3)
print(s.goc())

#W8A12
class ComplexNumber:
  def __init__(self,real1,imag1,real2,imag2):
    self.real1 = real1
    self.imag1 = imag1
    self.real2 = real2
    self.imag2 = imag2
  def mul(self):
    return f'{self.real1*self.real2 - self.imag1*self.imag2} {self.real1*self.imag2 + self.imag1*self.real2}'
real1,imag1 = map(int,input().split())
real2,imag2 = map(int,input().split())
s = ComplexNumber(real1,imag1,real2,imag2)
print(s.mul())

#W8A13
from math import*
class Triangle:
  def __init__(self,edge1,edge2,edge3):
    self.edge1=edge1
    self.edge2=edge2
    self.edge3=edge3
  def check(self):
    if (self.edge1 <= 0 or self.edge2 <= 0 or self.edge3 <= 0) or (self.edge1 + self.edge2 <= self.edge3 or self.edge1 + self.edge3 <= self.edge2 or self.edge3 + self.edge2 <= self.edge1):
      return False
    else: return True
  def dientich(self):
    if self.check():
      p = (self.edge1 + self.edge2 + self.edge3)/2
      s= sqrt(p*(p-self.edge1)*(p-self.edge2)*(p-self.edge3))
      return f'{s:.2f}'
    else:
      return "invalid"
a,b,c=map(float,input().split())
s = Triangle(a,b,c)
print(s.dientich())