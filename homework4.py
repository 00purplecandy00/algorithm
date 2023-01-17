import sys

##1
sys.stdin = open("text4_1.txt","r")
T1 = int(input())
list1 = []
for i in range(T1):
    T2 = int(input())
    list2 = list(map(int,input().split()))
    a = sum(list2)
    list1.append(a)
for j in list1:
    print(j)

##2
sys.stdin = open("text4_2.txt","r")
A,B,C,D = map(int,input().split())
first_num = str(A)+str(B)
second_num = str(C)+str(D)
result = int(first_num)+int(second_num)
print(result)

##3
sys.stdin = open("text4_3.txt","r")
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
c1,c2 = map(int,input().split())
d1,d2 = 0,0

if a1==b1:
    d1=c1
elif a1==c1:
    d1=b1
else:
    d1=a1

if a2==b2:
    d2=c2
elif a2==c2:
    d2=b2
else:
    d2=a2
    
print(d1,d2,sep=" ")

##4
sys.stdin = open("text4_4.txt","r")
list2=[]
while(1):
    b,c = map(int,input().split())
    if b == 0 and c == 0:
        for k in list2:
            print(k)
        break
    else:
        list2.append(b+c)

##5
sys.stdin = open("text4_5.txt","r")
original = input()
if len(original) == 1:
   original = "0"+original
num1 = original
i = 0
while(1):    
    num1_1 = int(num1[len(num1)-2])+int(num1[len(num1)-1])
    num1_2 = str(num1_1)
    num2 = num1[len(num1)-1]+num1_2[len(num1_2)-1]
    i += 1
    if original == num2:
        print(i)
        break
    else:
        num1 = num2
        str(num1)