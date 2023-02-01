
from operator import itemgetter

lQueue = []

def prioSort(lPrioQueue):
    lPrioQueue = sorted(lPrioQueue, key=itemgetter("priority"), reverse=True)

    for i in range(0, len(lPrioQueue)):

        exec(lPrioQueue[i]["command"])


def addCmd(cmd,priority=5):
    if priority > 10:
        priority = 10
    if priority < 0:
        priority = 0

    newDict= {"command": str(cmd) , "priority": int(priority)}
    lQueue.append(newDict)


#testing examples
addCmd("print('hello')", 5)
addCmd("""
a = 3*5 
print(a)
""", 9)

addCmd("""
b = 3
while b:
    b = b-1
    print(b)
    """, 11)

addCmd("""
def fuc(n):
    a = 2
    for i in range(1, n+1):
        a = a*i
        return a
print(fuc(3))
    """, -2)

addCmd("print('checking')", 2)
    
prioSort(lQueue)