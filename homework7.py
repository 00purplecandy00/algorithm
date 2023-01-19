import sys
##1
sys.stdin = open("text7_1.txt","r")
list1 = []
list2 = []
count = 0
for i in range(7):
    a = int(input())
    list1.append(a)
for j in list1:
    if j%2 == 1:
        list2.append(j)

if len(list2) == 0:
    print(-1)
else:
    print(sum(list2))
    print(min(list2))

##2
sys.stdin = open("text7_2.txt","r")
list1=[]
S = list(input().split(","))
for i in S:
    list1.append(int(i))
print(sum(list1))

##3
sys.stdin = open("text7_3.txt","r")
my_dic = {
    "A+": "4.3", "A0": "4.0", "A-": "3.7",
    "B+": "3.3", "B0": "3.0", "B-": "2.7",
    "C+": "2.3", "C0": "2.0", "C-": "1.7",
    "D+": "1.3", "D0": "1.0", "D-": "0.7",
    "F": "0.0"
}
S = input()
print(my_dic[S])

##4
sys.stdin = open("text7_4.txt","r")
i = 0
j = 0
time = 0
list1 = []
S = input()
my_dic = {
    "A":3,
    "B":3,
    "C":3,
    "D":4,
    "E":4,
    "F":4,
    "G":5,
    "H":5,
    "I":5,
    "J":6,
    "K":6,
    "L":6,
    "M":7,
    "N":7,
    "O":7,
    "P":8,
    "Q":8,
    "R":8,
    "S":8,
    "T":9,
    "U":9,
    "V":9,
    "W":10,
    "X":10,
    "Y":10,
    "Z":10
}
for i in range(len(S)):
    list1.append(my_dic[S[i]])
for j in list1:
    time += j
print(time)

##5
sys.stdin = open("text7_5.txt","r")
A = int(input())
B = int(input())
C = int(input())

S = A*B*C
list1 = []
S = str(S)
i = 0
j = 0
k = 0
dic = {}
for i in range(len(S)):
    list1.append(S[i])
for j in list1:
    if j not in dic:
        dic[j] = 1
    else:
        dic[j] += 1
for k in range(10):
    if str(k) not in dic:
        print(0)
    else:
        print(dic[str(k)])

##6
sys.stdin = open("text7_6.txt","r")
T = int(input())
count = 0
dic = {}
list1 = []


for i in range(T):
    S = input()
    if S[0:len(S)-6:1] not in dic:
        if S[-5:] == "enter":
            dic[S[0:len(S)-6:1]]  = 1
        elif S[-5:] == "leave":
            dic[S[0:len(S)-6:1]]  = 0
    else:
        if S[-5:] == "enter":
            dic[S[0:len(S)-6:1]]  += 1
        elif S[-5:] == "leave":
            dic[S[0:len(S)-6:1]]  -= 1
for j in dic:
    if dic[j] == 1:
        list1.append(j)
print(*sorted(list1, reverse= True))

