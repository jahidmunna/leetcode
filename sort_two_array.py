
count = 0 
def sorted_list(list1, list2):
    global count
    count +=1 
    print("count: ", count)
    print(f"l1: {list1}")
    print(f"l2: {list2}")
    print("-"*50)
    
    if not list1:
        print("list1 is empty")
        return list2
    
    if not list2:
        print("list2 is empty")
        return list1
    
    
    if list1[0]<=list2[0]:
        print("HERE")
        return [list1[0]] + sorted_list(list1[1:], list2)
             
    if list2[0]<=list1[0]:
        print("HERE2")
        return [list2[0]] + sorted_list(list1, list2[1:])



list1 = [1,3,4]
list2 = [2,5,6]

result = sorted_list(list1, list2)
print(result)
