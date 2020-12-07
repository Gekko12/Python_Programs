"""
        A positive integer m is a prime product if it can be written as p×q, where p and q are both primes. 
        
        Write a Python function primeproduct(m) that takes an integer m as input and returns True if m is a prime product and 
        False otherwise. (If m is not positive, your function should return False.)
        Eg.
        >>> primeproduct(6)
        True

        >>> primeproduct(188)
        False

        >>> primeproduct(202)
        True
"""

import math

# Seive of Erasthonesis Algorithm
def Seive(x) :     
        chk = list()
        
        chk.insert(0,False) # Index of 0 and 1 are false as we know that they're not prime numbers 
        chk.insert(1,False)
        
        for i in range(2,x+1) :
                chk.append(True)  # Assuming all to be prime at first
           
        upto = int(math.ceil(math.sqrt(x)))      
        for i in range(2 ,upto+1) :
                if chk[i] :
                        for j in range(i*i, x+1) :
                                if j % i == 0 :
                                        chk[j] = False
        return chk


#primeproduct()
def primeproduct(m) :
        lst = list()
        lst = Seive(m)
        for i in range(m):
                if lst[i] :
                        for j in range(i ,m) :
                                if lst[j] and i*j == m :
                                       # print("(", i, ",", j, ")")
                                        return True        
        return False


#main
inp = int(input("Enter a number :"))
print(primeproduct(inp))
                
