# Read an integer N.
# Without using any string methods, try to print the following:
# 123...N
# Note that "" represents the values in between.

n = int(input())
# number = 1
# num_list = []
# while number <= n:
#     num_list.append(number)
#     print(number)
#     number += 1
    

# print(num_list)

for item in range(1,n+1):
    print(item, end = "")
print("")