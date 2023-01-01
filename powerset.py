def powerset(set1):
  list_sub = list(set1)
  subsets = []
  for i in range(2**len(list_sub)):
    subset = []
    for k in range(len(list_sub)):
      if i & 1<<k:
        subset.append(list_sub[k])
    subsets.append(subset)
  return subsets
user = input("input list ex-[1,2,3,4,5]: ")
user = user[1:-1]
user =(int(i) for i in user.split(","))
subsets = powerset((user))
print(subsets)
