#4章
'''
#401 輸入10數字找最小值
list = []
for i in range(10):
    list.append(eval(input()))

print(min(list))    
##
minn = eval(input())
for i in range(0,9):
    n1 = eval(input())
    if minn > n1:
        minn = n1 
print(minn)        
        
#ˋ402
list = []
n = eval(input())
while n != 9999:
    list.append(n)
    n = eval(input())
    

print(min(list))    

#403
a = eval(input())
b = eval(input())
sum = 0 
list =[]

for i in range (a,b+1):
    if i % 4 == 0 or i % 9 == 0:
        sum += 1 
        list.append(i)
        print("%-4d" %i ,end='')#靠左對其 寬為四


        if sum %10 == 0:#一列輸出10 個數字
            print('')#跳行
print("\n%d\n%d"%(sum, sum(list)))  #\n 換行      


#404 反轉
a = eval(input())
print(a[::-1])

#405 級別判斷
g = eval(input)
while g != -9999:
    if g >= 90 and g <= 100:
        print('A')
    elif  g >= 80 and g <= 89:
        print('B')        
    elif  g >= 70 and g <= 79:
        print('C')
    else:
        print("E")    

#406   BMI 計算
import turtle


cm = eval(input())
while cm != -9999:
    weight = w = eval(input())
    BMI = w / (cm / 100 ) ** 2
    print("BMI :%.2f"%(BMI))

    if BMI <  18.5:
        print("State: under weight")
    elif BMI >= 18.5 and BMI < 25:
        print("State: normal ")
    elif BMI >= 25 and BMI< 30 :
        print("State: over weight")
    elif BMI >= 30  :
        print("State: you are so fat ")

    else:
        print("賣粿亂拉") 
    cm = eval(input())    
    
#tqc 407 
while(True):
    y = eval(input("?"))
    if y == -9999:
        break 
    elif (y%4 == 0 and y %100!= 0) or y %400 == 0:
        #四年且非百 或是400
        print("%d is a leap year "%y)
    else:
        print("%d is not a leap year "%y)        

#tqc 408 機偶數判斷 輸入10 庶幾偶數判斷'
even = 0 
for i in range (10):
    if eval(input())%2 == 0:
        even += 1 

print("Evan number:%d"%(even))
print("odd numbers :%d"%(10 - even))         
'''
#tqc 409 
nami = chopper = null = 0 #開始都為 0 
for i in range(5):#輸入五個值
    n = eval(input())
    if n == 1 :
        nami += 1 
    if n == 2 :
        chopper += 1 
    else:
        null += 1 

    print("Total votes of NO.1:nami =  %d " %nami)
    print("Total votes of NO.2:chopper =  %d " %chopper)
    print("Total null votes  =  %d " %null)#null空的
if nami > chopper :
    print("=> No.1 nami won the election. ")
elif nami == chopper :
    print("=> no one won the election. ")    
else :
    print("=> No.2 chopper won the election. ")    

#tqc 410  等腰三角形
n = eval(input())
for i in range(n):#為7 時 range = 0到6
    for j in range(n-i-1):#空白
        print(" ",end='')
    for k in range(2*i+1):
        print("*",end='')
    print("")        #每一個i 做換行動作
