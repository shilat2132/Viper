from viper import Viper

# code = """
# x=0
# x = x + "6"
# y = x
# isTrue = true
# if( x<=10) && isTrue{
# print("some str")
# }

# """
# Viper(code).interperter()

# code1 = """
# x = 10
# y = 5
# sum = x + y
# if sum > 10 {
#     print("Sum is greater than 10")
# } else {
#     print("Sum is 10 or less")
# }

# for i in range(3) {
#     print("Iteration:", i)
# }
# """
# Viper(code1).interperter()

# code2 = """
# arr = [1, 2, 3]
# sum = 0
# for num in arr {
#     sum = sum + num
# }
# print("Sum of array:", sum)

# text = "Hello"
# if text.isUpper() {
#     print("Text is uppercase")
# } else {
#     print("Text is not uppercase")
# }
# """
# Viper(code2).interperter() 


# code3 = """                     
# x = 10
# y = "5"
# result = x + y  
# if result > 10 {
#     print("This will not print due to error")
# }
# """
# #A program with a typo that tries 
# #to append a number to a string, 
# # causing a runtime error.
# Viper(code3).interperter()

# code4 = """
# text = "Hello"
# if x + 5 {
#     print("This condition is not boolean")
# }

# arr = [1, 2, 3]
# arr.replace(1, "one")  
# """
# #A program with a syntax error and a type error: using a 
# #non-Boolean condition and using an inappropriate method 
# #on an array.
# Viper(code4).interperter()

# code5 = """
# text = true
# if text {
#     print("This condition is not boolean")
# }

# arr = [1, 2, 3]
# arr.replace(1, "one")  
# """
# #A program with a syntax error and a type error: using a 
# #non-Boolean condition and using an inappropriate method 
# #on an array.
# Viper(code4).interperter()

code5 = """
str1 = "Hello"
str2 = "World"
greeting = str1.CONCAT(" ")
greeting = greeting.CONCAT(str2)
print(greeting)

arr = [10, 20, 30]
arr.append(40)
print(arr)

arr.addItem(2, 25)
print(arr)

tup = (1, 2, 3)
tup_to_add = (4, 5, 6)
tup2 = tup.combine(tup_to_add)
print(tup2)

index_of_3 = tup2.index(3)
print(index_of_3)
"""

Viper(code5).interperter()


