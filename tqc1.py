#101
'''#
a = eval(input("num1:"))
#eval = 字符串表达式，并返回表达式的值
b = float(input("num2:"))
c = input("num3:")
d = input("文字")
print('|%5d %5d|' %(a, b))
#寬為多少 則%多少 + 
print("/%5d %5d/"%(a,b))#向左靠齊
# 欄寬為7輸出浮點數到小數點後第二位。
print("/%7.2f %7.2f/"%(a,b))

%d = 整型 
%f = 小數 
%.(多少f) = 保留到多少位

print("/%10s %10s/"%(c,d))#題目要求10 蘭寬 空白尖閣


#104 計算園面積周長
import math 


r = eval(input("R?"))

radius = r

print("Radius = %d"%(radius))#半徑
print("Perimeter = %.2d"%(2 * 3.14159 *radius))#周長
print("Area = %d"%(radius * radius * math.pi))#面積

#105 矩行面積

h = eval(input("高:"))
w = eval(input("寬:"))

print("Perimeter = %.2f" %((h + w)* 2))
print("Area = %.2d" %(h * w))
'''
'''
#106  換算速度
x = eval(input("分:"))
y = eval(input("秒:"))
z = eval(input("幾公里:"))

print("Speed = %.1f"%((z /1.6) / ((y / 60 + x) / 60)))
print('Speed = %.1f' %((z / 1.6) / ((y / 60 + x) / 60)))

#107  河漢平均數
n1 = eval(input("1?"))
n2 = eval(input("2?"))
n3 = eval(input("3?"))
n4 = eval(input("4?"))
n5= eval(input("5?"))

sum = n1 + n2 + n3 + n4 + n5
ave = sum/5
print("Sum = %.1f"%(sum))
print("Average = %.1f"%(ave))
'''

#108 兩點座標與歐式距離
import math
x1 = eval(input())
x2 = eval(input())
y1 = eval(input())
y2 = eval(input())
print("(%d , %d)"%(x1,x2))
print("(%.2f , %d)"%(y1,y2))
print("({} , {})" .format(x1,x2))
print("Distance = %.4f"%math.sqrt(((x1 - x2)**2+(y1 - y2)**2)))

#109  正五邊形計算
import math
s = eval(input())
print("Area = %.4f"%((5 * s**2)/(4 * math.tan(math.pi / 5))))
 
#110 算多邊形面積
import math 
n = eval(input())
s = eval(input())
print("Area = %.4f"%((n * s ** 2)/(4 * math.tan(math.pi / n ))))
print("aaaaaaaa")