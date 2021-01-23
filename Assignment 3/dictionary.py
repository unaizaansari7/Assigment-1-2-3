list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]

print("Original list1 is" + str(list1))
print("Original list2 is" + str(list2))

res = dict(zip(list1, list2))

print("Resultant dictionary is:" + str(res))
