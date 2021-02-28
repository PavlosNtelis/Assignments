import random

def fibo(x):
    i=1
    j=1
    for k in range(x - 2):
        tmp = i
        i = i + j
        j = tmp
    return i

print("Enter your number:")
x = int(input())
n = fibo(x)
print("The No.", x,"term is", n)
i = 0
while i < 20:
    a = random.randint(1 , n)
    if (a**n) % n != a % n:
        print ("It is not a prime number")
        break
    i += 1
    
if i == 20 :
    print("It is a prime number")
