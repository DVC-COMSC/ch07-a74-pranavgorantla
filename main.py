lst = []

n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) # adding the element
      


value = input("What value do you want to remove from the list?: ")

if value in lst:
   lst.remove(value)

print(lst)
