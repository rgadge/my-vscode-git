# You are given a positive integer . Print a numerical triangle of height  like the one below:

# 1
# 22
# 333
# 4444
# 55555
# ......

# Can you do it using only arithmetic operations, a single for loop and print statement?
# Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.

#n = int(input())
#print(str(n)*n)
# for n in range(1,n):
#     print(str(n)*n)


# for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     # print(i*i)
#     n = i
#     while n>0:
#         print(i, end = "")
#         n -= 1
#     print("")


for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    # print(i*i)
    #print([0, 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i])
    print(int((10 ** i - 1) / 9) * i)
