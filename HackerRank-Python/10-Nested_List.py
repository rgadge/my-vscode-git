# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# list1 = []
# list2 = []

# iteration = int(input())

# for n in range(iteration):
#     list1.append(input())
#     list2.append(input())

# print(list1, ":", list2)

name = []
score = []


for _ in range(int(input())):
    name.append(input())
    score.append(float(input()))

print(name)
print(score)

# student = zip(name, score)
# list(student)

student = [(name[i],score[i]) for i in range(0,len(name))]
print(student)