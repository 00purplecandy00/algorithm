import sys

##1
sys.stdin = open("text5_1.txt","r")
email = input()
list1 = []
i = 0
j = 0
k = 0
a = 0
for i in email:
    list1.append(i)
prohibit = ['C','A','M','B','R','I','D','G','E']
for j in email:
    if j in prohibit:
        a = list1.index(j)
        list1[a] = ""
    else:
        pass
for k in list1:
    print(k,end="")
print()

##2
sys.stdin = open("text5_2.txt","r")
T = int(input())
list1=[]
i = 0
j = 0
k = 0
p = 0
a = ""
b = ""
for i in range(T):
    a,b = map(str,input().split())
    for k in range(len(b)):
        for j in range(int(a)):
            list1.append(b[k])
    for p in list1:
        print(p,end="")
    print()
    list1 = []
    i = 0
    j = 0
    k = 0
    p = 0
    a = ""
    b = ""

##3
sys.stdin = open("text5_3.txt","r")
a = 0
word = input()
if len(word)%2==0:
    a = len(word)//2    
    if word[0:a:1] == word[len(word)-1:len(word)-a-1:-1]:
        print(1)
    else:
        print(0)
else:
    a = len(word)//2
    if word[0:a:1] == word[len(word)-1:len(word)-a-1:-1]:
        print(1)
    else:
        print(0)

##4
sys.stdin = open("text5_4.txt","r")
picture = input()
a = 0
b = 0
i = 0
j = 0
left_punch = 0
right_punch = 0
a = picture.index("(")
b = picture.index(")")

for i in range(a+1):
    if picture[i] == '@':
        left_punch += 1
for j in range(b,len(picture)):
    if picture[j] == '@':
        right_punch += 1
print(left_punch,right_punch)

##5
sys.stdin = open("text5_5.txt","r")
word = input()
list1 = ['c=','c-','d-','lj','nj','s=']
list2 = ['dz=']
list3 = ['z=']
i = 0
j = 0
count = len(word)
for i in range(len(word)):
    if word[i:i+2] in list1:
        count -= 1
    if word[i:i+3] in list2:
        count -= 1
    if word[i:i+2] in list3:
        count -= 1
print(count)

##6
sys.stdin = open("text5_6.txt","r")
a = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    if i in a:
        print(a.index(i), end= ' ')
    else:
        print(-1, end=' ')