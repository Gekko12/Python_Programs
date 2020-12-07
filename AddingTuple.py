# Program to demonstrate how to add elements in tuple as tuple are immutable

n = int(input ("Enter the number of elements : "))
lst = list(map (int ,input("Enter elements in a single line :").split())) [ : n]

tup = tuple( lst )
print(lst)

