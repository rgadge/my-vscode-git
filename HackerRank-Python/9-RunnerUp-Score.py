# # Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# # You are given scores. Store them in a list and find the score of the runner-up.

# # Sample Input
# # 5
# # 2 3 6 6 5

# # Sample Output
# # 5

# n = int(input())
# #nos = [int(input().split())]
# nos = list(map(int, input().split()))

# #nos = map(int, input()).split()

# #print(nos)
# #print(type(nos))
# #print(max(nos))
# nos.remove(max(nos))
# #print(nos)
# print(max(nos))
# for item in nos:
#     if item == max(nos):
#         nos.remove(item)
#     else:
#         continue

# print(max(nos))


n = int(input())
nos = list(map(int,input().strip().split()))[:n]
i = max(nos)
while max(nos) == i:
    nos.remove(max(nos))
print(max(nos))