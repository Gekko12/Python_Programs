#Program to read a file and shuffle the read words and write it into another file
#I'm assuming that :) , paragraphs are separated by empty lines 

import random

#reading a file
fhand = input('Enter file name (reading) :')
fopen = open(fhand) #default mode is read only

#writing into a file
fhand = input('Enter file name (writing) :')
fwrite = open(fhand,'w')    #writing into a file

for line in fopen :
    word_lst = line.split()
    
    if len(word_lst) < 1 : break #if a line is empty than we done with reading a paragraph
    
    #print(tmp_lst)
    random.shuffle(word_lst)   #stores the shuffled words in a list 
    #print(word_lst)

    for word in word_lst :
        fwrite.write(word+' ')
    
    fwrite.write('\n') #we're done with a line

fopen.close()
fwrite.close()

quit(0)