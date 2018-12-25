# # Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# # list1 = []
# # list2 = []

# # iteration = int(input())

# # for n in range(iteration):
# #     list1.append(input())
# #     list2.append(input())

# # print(list1, ":", list2)

# name = []
# score = []

# ## Storing multiple input values into a lists, name and score
# for _ in range(int(input())):
#     name.append(input())
#     score.append(float(input()))

# # student = [(name[i],score[i]) for i in range(0,len(name))]

# # Storing maximum score into a variable for calculation
# max_score = max(score)

# # # Exploring Tupples for this purpose
# # student_tuple = tuple(zip(name,score))
# # print(student_tuple)

# # for i in student_tuple:
# #     if i[1] == max_score:
# #         print(i[0], "has highest score!")
# #         max_no = i[1]

# # Trying the same as done above but this time using list
# student_list = list(zip(name,score))
# print(student_list)

# for i in student_list:
#     if i[1] == max_score:
#         print(i[0], "has highest score!")

# # Remove t=value where the max score exits and then we calculate the 2nds highest
# student_list_2 = student_list
# for n in student_list_2:
#     if n[1] == max_score:
#         student_list_2.remove(n)

# print(student_list_2[1])
# #student_list.pop(1)

# print(student_list_2)


# max_score_2 = []
# for x in student_list_2:
#     max_score_2.append(x[1])
# max_2 = max(max_score_2)
# for r in max_score_2:
#     if r[1] = max_2:
#         [print(student_list_2[0], "has the seconda highest score!")


# Doing it the Dictionary way
name = []
score = []

## Storing multiple input values into a lists, name and score
for _ in range(int(input())):
    name.append(input())
    score.append(float(input()))
# Connverting Lists name and score into a dictionary
name_score = dict(zip(name,score))
#print(type(name_score))
#print(name_score)

def find_max_score(my_dict):
    """This function will take a dictionary as in input and Looping throgh all the items in the Dictionary and 
    loop though all the items to find keys which have highest value"""
    for key,value in my_dict.items():
        if value == max(my_dict.values()):
            return key

# finding highest score 
max_score = find_max_score(name_score)
print(max_score, "has the highest score!")

# finding the second highest by deleting max score key pair from the dicttionary and creating a fresh dictionary for calculations
del name_score[max_score]
        #name_score.pop[key]
#print(name_score)

second_max_score = find_max_score(name_score)
print(second_max_score, "has the second highest score!!")

 