elements = []
n = int(input("Enter the number of elements: "))
for i in range(0, n):
    num = int(input("Enter the value of element: "))
    elements.append(num)
elements.sort()
print(elements)  
