"""
def cab_charge(X,Y):
    if X<Y:
        return"FIRST"
    elif X>Y:
        return"SECOND"
    else:
        return"ANY"
X,Y=30,65
print(cab_charge(X,Y))
X,Y=42,42
print(cab_charge(X,Y))
X,Y=90,50
print(cab_charge(X,Y))
"""

T=int(input())  #input of test case

for i in range(T): #jitne test case hai utne var loop chalana
    (X,Y)= map(int,input().split(' '))
    if X<Y:
        print("FIRST")
    elif X>Y:
        print("SECOND")
    else:
        print("ANY")