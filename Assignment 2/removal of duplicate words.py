s = "Apple is my favourite fruit and spanish is my favourite vegetable"
l = s.split() 
k = [] 
for i in l: 
  
     
    if (s.count(i)>1 and (i not in k)or s.count(i)==1): 
        k.append(i) 
print(' '.join(k)) 
