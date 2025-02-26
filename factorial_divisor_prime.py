# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

# def is_prime(n):
#     c=0
#     for i in range(1,n+1):
#         if n%i==0:
#             c+=1
#         if c>2:
#             return False
#     if c==2:
#         return True

# def is_prime(n):
#     for i in range(2,n//2+1):
#         if n%i==0:
#             return False
#     return True
import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
    
# print(is_prime(3))
arr=[]
for i in range(1,100+1):
    if is_prime(i):
        arr.append(i)
    # print(i, is_prime(i))
print(arr)
N=11

def cal():
    fact=1
    i=2
    print(fact,N)
    while N>=fact+1:
        fact*=i
        print(fact)
        if fact==N-1 or fact==N+1:
            print("factorial prime", N)
            return
        i+=1
    print(fact,N,"jj")
    print("NOt factorial prime hh", N)
    return 
if is_prime(N):
    cal()
else: 
    print("NOt factorial prime vv", N)

    
            
