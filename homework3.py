##1
T = int(input())
list1 = list(map(int,input().split()))
print(min(list1),max(list1))

##2
T = int(input())
num = input()
sum1 = 0
for i in range(T):
    sum1 += int(num[i])
print(sum1)

##3
T = int(input())
list1 = []
for i in range(T):
    num = int(input())
    list1.append(num)
list1.sort()
for j in list1:
    print(j,end = " ")

##4
list1 = []
for i in range(9):
    a = int(input())
    list1.append(a)
max_num = max(list1)
max_index = list1.index(max_num)
print(max_num)
print(max_index+1)