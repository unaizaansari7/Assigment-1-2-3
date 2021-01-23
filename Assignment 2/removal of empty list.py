list_1 = [7, 12, [], 10, 77, [], 99, [], 11, [], 56]

print("the original list is: " + str(list_1))

res = [element for element in list_1 if element != []]

print ("list after empty list removal : " + str(res))
