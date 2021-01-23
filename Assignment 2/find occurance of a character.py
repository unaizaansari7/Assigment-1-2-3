str1 = input("Enter a string:")
ch1 = input("Choose a character from a sentence:")

for i in range(len(str1)):
    if(str1[i] == ch1):
        print(ch1, "is found at position" , i)
