import sys

##1
sys.stdin = open("text6_1.txt","r")
score = int(input())
if score < 60:
    print('F')
elif score < 70:
    print('D')
elif score < 80:
    print('C')
elif score < 90:
    print('B')
else:
    print('A')

##2
sys.stdin = open("text6_2.txt","r")
i = 0
j = 0
T=int(input())
for i in range(T):
    S = list(input().split())
    for j in S:
        print(j[::-1],end = " ")
    print()

##3
sys.stdin = open("text6_3.txt","r")
S = input()
for i in range(0,len(S),10):
    print(S[i:i+10])

##4
sys.stdin = open("text6_4.txt","r")
numbers = list(map(int,input().split()))
i = 0
j = 1
k = 0
temp = 0
while(1):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
            temp = 0
            for j in numbers:
                print(j,end=" ")
            print()
    if numbers == sorted(numbers):
        break


