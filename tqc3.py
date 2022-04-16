'''
#301 迴圈整數相加

a = eval(input())
b = eval(input())
sum = 0 #總和值
for i in range(a,b+1):
    sum += i 
print(sum)    

#302 鄉佳偶數
a = eval(input())
b = eval(input())
sum = 0
for i in range(a,b+1):
    if i % 2 ==0:
        sum += i

 
#303 
n = eval(input())
for i in range(1,n+1):
    for u in range(1,i+1):
        print("%5d"%(u * i),end ='')#左右列的行
    print('')
  
#304 迴圈倍數總和
n = eval(input("?"))
sum = 0 
for i in range(1,n+1):
    if i % 5 == 0:
        sum += i 
print(sum)        

#305 反轉順序
n = input()
print(n[::-1])#反轉


#迴圈接成計算306
n = eval(input())
ans = 1 
for i in range(1,n+1):
    ans *= i 
print(ans)        

#乘法表 307
n = eval(input("?"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("%-2d* %-2d= %-4d"%(j,i,i * j), end='') 
    print('')

# 每位數相加總 308
n = eval(input())# 幾筆測試
for i in range(n):
    tem = num = eval(input())#tem暫時存數
    sum = 0 
    while tem != 0:
        sum += tem % 10#餘數
        tem = tem //10#整除十
    print("Sum of all dights of %d is %d" %(num,sum))    

#另解
n = eval(input())
for i in range(n):
    s = input()
    L = [int(j) for j in s ]
    print("Sum of all dights of %s is %d"%(s,sum(L)))

#存款總額 309 
total = eval (input())#輸入金額
y = eval(input())#年收益率
m = eval(input())#經過的月份

print("%s \t  %s " % ('month','Amount'))

for i in range(1,m+1):
    total += total * y /1200#金額 = 存款* 年利率/1200 
    print("%3d \t %2f" %(i,total))#\t 為跳下一行
'''
#310 c迴圈公式計算
import math
n = eval(input())
sum = 0 
for i in range(2,n+1):
    sum += 1 /(math.sqrt(i-1) + math.sqrt(i))

print("%.4f"%(sum))    

##
import math

num = eval(input())
Sum = 0

for n in range(2, num + 1):
    Sum += 1 / (math.sqrt(n - 1) + math.sqrt(n))

print('%.4f' %Sum)