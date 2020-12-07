'''
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
'''

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try :
        fh = open(fname)
        lc = 0
        total = 0.0
        
        for line in fh:
            if not line.startswith("X-DSPAM-Confidence:") : continue
            lc += 1
            z = line.find('0')
            new_line = line[z:z+7].strip()
            total += float(new_line)
            
        res = float(total / lc)
        print("Average spam confidence:",res,"\n")
        
except :
        print("File not found \n")
        quit()

