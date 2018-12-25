# name = []
# score = []

# ## Storing multiple input values into a lists, name and score
# for _ in range(int(input())):
#     name.append(input())
#     score.append(float(input()))
# # Connverting Lists name and score into a dictionary
# name_score = dict(zip(name,score))

# def find_lowest_score(my_dict):
#     """This function will take a dictionary as in input and Looping throgh all the items in the Dictionary and 
#     loop though all the items to find keys which have highest value"""
#     for key,value in my_dict.items():
#         if value == min(my_dict.values()):
#             return key

# # finding highest score 
# lowest_score = find_lowest_score(name_score)
# print(lowest_score)

# # finding the second highest by deleting max score key pair from the dicttionary and creating a fresh dictionary for calculations
# del name_score[lowest_score]

# second_lowest_score = find_lowest_score(name_score)
# print(second_lowest_score)


marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))