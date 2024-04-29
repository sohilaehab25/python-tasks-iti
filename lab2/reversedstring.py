def String_Reverse(word):
    return word[::-1]

word = input("Enter your word: ")
if word.isalpha():
    print(f"The reversed word is: {String_Reverse(word)}")