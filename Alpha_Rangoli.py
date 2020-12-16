'''
You are given an integer, . Your task is to print an alphabet rangoli of size

. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------

The center of the rangoli has the first alphabet letter a,
and the boundary has the alphabet letter (in alphabetical order).

'''


# print_rangoli(N) function
def print_rangoli(size) :
    row = (size-1)*2 +1
    alpha_start = chr(97 + size)

    for r in range(0 ,row) :
        if r <= row//2 :
            for d in range(0 ,(size-1-r)*2) :
                print('-',sep='',end='')

            btw = r*2 +1
            incr_start = alpha_start

            for a in range(0 ,btw) :
                if a <= btw//2 :
                    if r == 0 :
                        incr_start = chr(ord(incr_start)-1)
                        prt = incr_start
                        print(prt,sep='',end='')
                    else :
                        incr_start = chr(ord(incr_start)-1)
                        prt = incr_start+'-'
                        print(prt,sep='',end='')
                else :
                    incr_start = chr(ord(incr_start)+1)
                    if a == r*2 :
                        prt = incr_start
                        print(prt,sep='',end='')
                    else :
                        prt = incr_start+'-'
                        print(prt,sep='',end='')

            for d in range(0 ,(size-1-r)*2) :
                print('-',sep='',end='')

        else :
            for d in range(0 ,(r-size+1)*2) :
                print('-',sep='',end='')

            btw = (row-r-1)*2 +1
            incr_start = alpha_start

            for a in range(0 ,btw) :
                if a <= btw//2 :
                    if r == row-1 :
                        incr_start = chr(ord(incr_start)-1)
                        prt = incr_start
                        print(prt,sep='',end='')
                    else :
                        incr_start = chr(ord(incr_start)-1)
                        prt = incr_start+'-'
                        print(prt,sep='',end='')
                else :
                    incr_start = chr(ord(incr_start)+1)
                    if a == btw-1 :
                        prt = incr_start
                        print(prt,sep='',end='')
                    else :
                        prt = incr_start+'-'
                        print(prt,sep='',end='')

            for d in range(0 ,(r-size+1)*2) :
                print('-',sep='',end='')

        print()
# function-ends



# main - function
size = int(input('Enter the size of Rangoli :'))
print_rangoli(size)
quit(0)


