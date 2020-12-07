fir = 0
sec = 1
third = fir + sec

print("Enter a number where series goes upto :")
x = int(input())

print(fir , end = "  ")
print(sec , end = "  ") 
for i in range(x-2):
        print(third , end = "  ")  #end = " " is used to avoid newline as newline is feed to end
        fir = sec
        sec = third
        third = fir + sec

print("\nAbove is the Fibonnaci Series \n") 
