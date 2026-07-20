def sort_lst(lst):
  for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
      return lst
numbers=[1,9,4,5,2]
print(sort_lst(numbers))