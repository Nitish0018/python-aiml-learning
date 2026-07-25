list1 = list(map(int, input("enter a list of numbers separated b spaces:").split()))
list2 = list(map(int,input("enter another list of number separated by spaces:").split()))
merged_list = list1 + list2
print("merged list:",merged_list)
sorted_list = sorted(merged_list)
print("sorted list:",sorted_list)
