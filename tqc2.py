#201 判斷是否為偶數
from tkinter import X

'''
n = eval(input("輸入一數?"))
if n % 2 == 0:
    print("%d is an even number"%(n))
else:
    print("%d is not an even number"%(n))


#202 3和5 倍數
x = eval(input("請輸入一數?"))
if x % 5 == 0:
    if x % 3 == 0:
        print("%d is a multiple of 3 and 5"%(x))
    else:
        print("%d is a multiple of 5"%(x))
elif n % 3 == 0:
    print("%d is a multiple of 3"%(x)) 

else:
    print("都不是拉")
'''
'''
#203 闺年 4 100! 400  
n = eval(input("please enter the years:"))
if n % 4 == 0 and n%100 != 0 or n % 400 == 0:
    print("%d is a leep year , "%(n))
else:
    print('%d is not a neep  years'%(n))    

'''
'''
#205 字元判斷
#英文字母 alphabet   數字 number  其他字元 symbol
n = input()
if n >= 'a' and n <= 'z' or n >= 'A' and n <= 'Z':
    print("%s is an alphabet"%(n))
elif n >= '0' and n <= '9':
    print("%s is a number"%(n))
else:
    print("%s is a symbol"%(n))       #%s 字符串 

#207 折扣
n = eval(input("?"))
if n >= 38000:
    print(n*0.7)
if n >= 28000:
    print(n * 0.8)    
if n >= 18000:
    print(n * 0.9)
if n >= 8000:
    print(n * 9.5)         
else:
    print(n)    

#208 十進位換算
n = eval(input("0到15"))
if n <= 9:
    print(n) 
elif n == 10:
    print('A')    
elif n == 11:
    print("B")
'''

#209 距離判斷
import math 
x = eval(input("?"))
y = eval(input("?"))
distance = math.sqrt((x - 5) ** 2 +(y-6) ** 2)
if distance <= 15:
    print("inside")
else:
    print("outside")    

#210 成立三角形判斷
n1 = eval(input("1?"))
n2 = eval(input("2?"))
n3 = eval(input("3?"))
if n1 + n2 > n3 and n1 + n3 > 2 and n2 +n3 >n1:
    print(n1+n2+n2)
else:
    print("invalid")    