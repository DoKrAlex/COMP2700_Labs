#Problem 1
def gcd(x,y): # It receive x and y values
        if(x==0 and y==0): # If both parameters are 0
            return # return none`
    
        if(y==0): # If second parameter is 0
            return x # return x
        else:
            return gcd(y,x%y) # recursive calling function
x = int(input("Enter x: ")) # Accept x value
y = int(input("Enter y: ")) # Accept y value
print("GCD of",x,"and",y,"is",gcd(x,y)) # calling where it pass x and y values and receive the return value and print the result
    

#Problem 2
def mod_inv(x,y):
    r0,r1 = x,y
    s0,s1 = 1,0
    t0,t1 = 0,1
    
    # Calculating the Bezout coefficients
    while r1 != 0:
        q = r0 // r1
        r0,r1 = r1,r0 % r1
        s0,s1 = s1, s0 - q*s1
        t0,t1 = t1, t0 - q*t1

    # s0 and t0 are the Bezout coefficients
    # ro holds the gcd of x and y
    # if r0 is not 1 we return None
    if r0 != 1:
        return None
    #Calculating the inverse
    inverse = (s0%y + y) % y;
    #returning the inverse
    return inverse

# Testing the above function
print("Mod inverse of 3 , 11 =",mod_inv(3,11))
print("Mod inverse of 4 , 12 =",mod_inv(4,12))

#Problem 3
def mod_exp(x,y,n):
    p = 1 
    s = x 
    r = y 

    while (r>0):
        if(r%2==1):
            p = p*(s%n)
        s = s*(s%n)
        r = r//2 
    
    return p
    
#Problem 4
import math

def generateRSAkey(p,q):
    n = p * q
    phin = (p - 1) * (q - 1) # this is phi of n
    #now e need to calculate e
    e = 2
    while(e<phin):
        if(math.gcd(e,phin)==1):
            break
    e+=1

    #let k be a random integer
    k = randint(1,100)
    d = 1 + k * phin
    return [[n,e],d]

#sample test
print(generateRSAkey(13,17))

#Problem 5
import random 
from fractions import gcd 
def generate_public(phi): 
   #selecting the e such that 1 < e <phi and gcd(e,phi)= 1 
    e = random.randrange(1,phi) 
    coprime =gcd(phi,e) 
    while (coprime >1): 
        e = random.randrange(1,phi) 
        coprime =gcd(phi,e)  
    return e;

 
def generate_private(Pub_key,phi): 
    for i in range(l,phi): 
       if((Pub_key * i)% phi == 1): 
           return i 
    return 


def encryption(M,e,n):
     #encrypted text 
    ET = pow(M,e) % n 
    return ET

def decryption(C,d,n): 
    #plain text
    PT = (pow(C,d)) % n 
    return PT 


p = int(input("Enter P = ")) 
q = int(input("Enter Q = ")) 
M = int(input("Enter plain text M = ")) 


n = p*q 
phi = (p-1)*(q-1) 
Pub_key = generate_public(phi) 
Pri_key = generate_private(Pub_key,phi) 
print ("Public key = "+str(Pub_key) )
print ("Private key = "+str(Pri_key) )

Cipher_text = encryption(M,Pub_key,n) 
print ("Cipher_text = "+str(Cipher_text) )

Plain_text = decryption(Cipher_text,Pri_key,n) 
print ("Decipher_text = "+str(Plain_text) )

#Problem 6
print("yay :)")
