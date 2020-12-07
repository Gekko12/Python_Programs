# Seive of Eratosthenes algo having complexity of O(n*log(log(n))) used to find prime num in a given range
 
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
        return chk #returns a boolean list of given range

'''
#main        
m = int(input("Enter the range upto which prime numbers will print :"))

lst = list()
lst = Seive(m)

for i in range(m+1):
        if lst[i] :
                print(i ,end=" ")

print()
'''

