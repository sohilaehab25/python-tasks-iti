def longestalphabitcal(s):
    longest_string = ""
    current_letter = ""
    
    for i in range(len(s)):
        if i == 0 or s[i] >= s[i - 1]:
            current_letter += s[i]
        else:
            if len(current_letter) >len(longest_string):
                longest_string = current_letter
            current_letter =s[i]

    if len(current_letter)> len(longest_string):
        longest_string = current_letter
    
    return longest_string

print("longestmstring is:", longestalphabitcal("sohilaehababcd")) 
