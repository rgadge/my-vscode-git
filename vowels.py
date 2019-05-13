# # vowels = ['a', 'e', 'i', 'o', 'u']
# # word = input("Provide a word to search for vowels: ")
# # found = []

# # for letter in word:
# #     if letter in vowels:
# #         if letter not in found:
# #             found.append(letter)

# # for vowel in found:
# #     print(vowel)



# vowels = set(list('aeiou'))
# word = input("Enter text to search for vowels and print numbers\n")
# found = {}

# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found[letter] = 1
#         found[letter] += 1
        
# print((found))


vowels = set('aeiou')
word = input("Enter text to search for vowels and print numbers\n")
found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
        
print((found))
