# for i in range(10):
#     for j in range(i, 10):
#         print(j, end="\t")
#     print()

arr = [1,2,3,4,5,6,7]

all_possible = []

for i in range(len(arr)):
    for j in range(i, len(arr)):
        # print(arr[i: j+1], end=" ")
        all_possible.append(arr[i:j+1])
    # print()

print(all_possible)









