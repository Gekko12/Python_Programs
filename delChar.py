"""
        Write a function delchar(s,c) that takes as input strings s and c, where c has length 1 (i.e., a single character), and returns
         the string obtained by deleting all occurrences of c in s. If c has length other than 1, the function should return s

        Here are some examples to show how your function should work.
    
        >>> delchar("banana","b")
        'anana'

        >>> delchar("banana","a")
        'bnn'

        >>> delchar("banana","n")
        'baaa'

        >>> delchar("banana","an")
        'banana'
"""

#delchar(string ,delCh )
def delchar(s ,c) :
        if len(c) != 1 :
                return s;
        st = ""
        for i in s :
                if i != c :
                        st = st + i
        
        return st
        
        
#main
s = input("Enter a string :")
c = input("Single char to delete :")

print(delchar(s ,c))

print()

        
                  
