string = input("enter your string")
voules = ['a', 'e', 'i', 'o', 'u']
result = ""
for i in range(len(string)):
    if string[i] not in voules:
        result = result + string[i]
print("\nyour string after removing the voules",result )        