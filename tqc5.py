#501 學號 訊息判斷
'''
def compute():
    Department = input()
    StudentID = input()
    Name = input()
    print("Department: %s" %Department)
    print("Student: %s"%StudentID )
    print("Name : %s "%Name )

compute()


#502  相乘
def compute():
    a = eval(input())
    b = eval(input())
    print(a * b )

compute()

#503 連加 居有個值為和
def compute(a,b):
    sum = 0 
    for i in range(a,b+1):
        sum += i 
    return sum    

a = eval(input())
b = eval(input())

print(compute(a,b))    

#504 次方
def compute(a,b):
    print(a **b )

a = eval(input())
b = eval(input())

compute(a,b)

#505 參數格式化輸出 直列橫行
def compute( a, x,y):
    for i in range(y):#表示列數
        for j in range(x):#表示個數
            print('%s'%a, end = '')
        print('')    
a = input()
x = eval(input())
y = eval(input())

compute(a,x,y)
#506  一元二次方程式 判別式大於0 
def compute(a, b, c):
    condition = b ** 2 - 4 * a * c 
    if condition >= 0:
        ans1 = (-b + condition ** 0.5)/(2*a)
        ans2 = (-b - condition ** 0.5)/(2*a)
    else:
        return 0 
a = eval(input())
b = eval(input())
c = eval(input())
if compute(a,b,c)== 0:
    print("Your equuation has not root")
else :
    ans1,ans2 = compute(a,b,c)
    print("%s,%s " %(ans1,ans2))

#507 判斷是否為質數 砍半前有因數
def compute(x):
    ans = True
    if (x<2):
        ans = False
    else:
        for i in range(2,x):
            if x % i == 0:#代表為因數
                ans = False
                break 
            return ans 

x = eval(input())
if compute(x):
    print("Prime")
else:
    print("Not Prime")    

#508   最大公因數 輾轉相除法
def compute(x,y):
    if y == 0:
        return x 
    else:
        return compute(y,x%y)

x,y = eval(input())
print(compute(x,y))

#508
import math 
x,y = eval(input())
print(math.gcd(x,y))

#509 最簡分數
from lzma import FILTER_LZMA2
import math 
# def compute(p,q):
#     return math.gcd(p,q)
x,y = eval(input())
m,n = eval(input())
q = y * n 
p = x * n + y * m 
GCD = math.gcd(p,q)
p = p / GCD
q = q / GCD
print("%d/%d + %d/%d = %d/%d "%(x,y,m,n,p,q))
'''
#510 費式數列
def compute(n):
    F0 = 0; F1 = 1 
    print("0 1 ",end='')
    for i in range(2,n):
        F2 = F0 + F1
        print("%d " %F2,end='')
        F0 = F1; F1 = F2

num = eval(input())
compute(num)        
# ANS 
def compute(num):
    F = [0, 1]
    for n in range(2, num):
        F.append(F[n - 1] + F[n - 2])
        
    for i in F:
        print(i, end=' ')

num = eval(input())
compute(num)
