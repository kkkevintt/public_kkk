'''
# 601 索引職加總 .偶數
L = []
sum = 0 
for i in range(12):
    L.append(eval(input()))
    if i%2 == 0:
        sum += L[i]#是偶數的加到 sum 


for j in range(4):#0到3  4列
    print("%3d%3d%3d"%(L[j*3],L[j*3+1],L[j*3+2]))

print(sum)             

#602 撲克牌
sum = 0 
for i in range(5):
    s = input()
    if s == "J":
        sum += 11
    elif s == "Q":
        sum += 12
    elif s == "K":
        sum += 13
    elif s == "A":
        sum += 1 
    else:
        sum += int(s)        

print(sum)
#603 數字排序
L = []
for i in range(10):
    L.append(eval(input()))
L.sort()#小到大排序
print(L[9],L[8],L[7])    

#604    眾數應用            
L = []
count = [0] *10 #10個位子都是0 初始化
for i in range(10):
    n = eval(input())
    L.append(n)
    count[L.index(n)] += 1#放入在尋找有幾個相同 

print(L[count.index(max(count))]) 
print(max(count))

#605 成績計算
s = []
for i in range(10):
    s.append(eval(input()))
s.sort()#小到大排序
ans = sum (s) - s[0] - s[9]
print("%d\n%.2f"%(ans,ans/8))

#606  二微陣列
rows = eval(input())
cols = eval(input())


for r in range(rows):
    for c in range(cols):
        print("%4d" %(c-r),end= '')
    print()

#606-2 
rows = eval(input())
cols = eval(input())   

def compute(L):
    for r in range(rows):
        for c in range(cols):
            print("%4d"%L[r][c],end='')
        print()    

L = []
for r in range(rows):
    L.append([])
    for c in range(cols):
        L[r].append(c-r)
compute(L)

#607 成績計算
from tkinter.tix import MAX


rows = ["1st","2nd","3rd"]
score = [] #cols 
for i in range(3): 
    print("The %s student :" %rows[i])
    score.append([])#空
    for j in range(5):#五筆成績
        score[i].append(eval(input()))

for i in range(3):
    print("Student %d "%(i+1 ))
    print("#Sum %d" %(sum(score[i])))
    print("#Average %.2f "%(sum(score[i])/5))        
# 608 最大最小值索引
r1 = c1 = r2 = c2 = 0 #最大最小索引
MAX = -99999999
MIN = 99999999999
for i in range (3):
    for j in range(3):
        n = int(input())
        if n > MAX:
            MAX = n ;r1 = i ;c1 = j 
        if n < MIN:
            MIN = n ; r2 = i ;c2 = j

print("INdex of the largest number %d is :(%d , %d) "%(MAX,r1 ,c1 ))           

print("Index of the smallest number %d is :(%d ,%d )"%(MIN , r2,c2 ))
'''
# 609 矩陣相加

mat1 = [[],[]]#初始化二為串列
mat2 = [[],[]]
print("Enter matrix 1 :")
for i in range(2):
    for j in range(2):
        print("[%d, %d]: "%(i+ 1 , j +1 ),end ='')#不換行所以空字串
        mat1[i].append(eval(input()))

print("Enter matrix 2 :")
for i in range(2):
    for j in range(2):
        print("[%d, %d]: "%(i+ 1 , j +1 ),end ='')
        mat2[i].append(eval(input()))

print("Matrix 1 :")
for i in range(2):
    for j in range(2):
        print("%d "%mat1[i][j],end='')
    print()    

print("Matrix 2 :")
for i in range(2):
    for j in range(2):
        print("%d "%mat2[i][j],end='')
    print()

print("Sum of 2 matrices:")
for i in range(2):
    for j in range(2):
        print("%d "%(mat1[i][j]+mat2[i][j]),end='')
    print()
#610  溫度矩陣 一維作法
temp = []
for i in range(4):
    print("Week %d : %(i+ 1 ")
    for j in range(3):
        temp.append(eval(input("Day %d :"%(j+1 ))))

print("Average: %.2f "%(sum (temp)/12))   
print("Highest: ",max(temp))    
print("Lowest: ",min(temp)) 
#ˊ610 