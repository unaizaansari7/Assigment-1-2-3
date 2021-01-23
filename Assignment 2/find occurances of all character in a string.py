

str1 = "Astrology"
  

all_char = {} 
  
for i in str1: 
    if i in all_char: 
        all_char[i] += 1
    else: 
        all_char[i] = 1
  
  
print ("Count of all characters in Astrology is :\n "
                                        +  str(all_char))

a = str1.find("o")
print(a)

a = str1.find("o" , a+1)
print(a)




