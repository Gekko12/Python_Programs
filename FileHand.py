# Program for File Handling

file = open("File.txt")  # By default open() use read method ie. file = open("File.txt" ,"r")

count = 0
for line in file :
        print(line ,end="")  # end="" as in file ,line already end with newline character
        count += 1

print("\nNumber of lines = ",count)
file.close()

file = open("File.txt") # As file pointer is already reached to EOF in above for loop that's why re-initialization      
full_file = file.read() # Read full file as a single string
print("\nNumbers of characters = ",len(full_file)) 

print("\nPrint(File[ : 15] = ",full_file[ : 15])
file.close()

quit(0)