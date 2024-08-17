from viper import Viper

code1 = """
x=0
x = (x+3)^2
isTrue = true
if (x<=10) && isTrue{
print("some str")
}
y = 0

while y<=5{
print(2)
y=y+1
}
y = x
for i in range(4){
    y = y+2
print(y)

}



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
# Viper(code1).interperter()


code2 = """
x = sqrt(9)+3
y = max(x, 17)
if (x>5) || (x==17){
x= 1
}else{
x=5
}
x=3
while x>0{
print(x)
x=x-1
}
"""
# Viper(code2).interperter()

code3 = """
for k in range(2, 8){
print(k)
}
x=1
a = [2, "str", "hello", "world", x]
for k in a{
print(k)
}
"""
# Viper(code3).interperter()


code4 = """
if x{
print("yes")
}
"""
# Viper(code4).interperter()

code5 = """
a = [1, 5, "hello", "world"]
a.append("!")
str = ""
for i in a{
print(i)
str = str.CONCAT(" ")
str = str.CONCAT(i)
}
"""
# Viper(code5).interperter()

# PROGRAMS THAT THROW ERRORS
# SYNTAX ERRORS
# would throw an error for the extra }
err1 = """
x=1
if x{
x=3
}}
"""

# Viper(err1).interperter()
# would throw an error for the extra )

err2 = """
x= 1
y =( y+1)*3)
"""

# Viper(err2).interperter()

# would raise an error because min function was called with no ()
err3 = """
x= min
"""

# Viper(err3).interperter()

# throws an error for missing a body
err4 = """
x=1
if x<1
"""

# Viper(err4).interperter()

# would raise an error because min function suppose to take 2 args
err5 = """
x=1
min(x, 5, 6)
"""

# Viper(err5).interperter()


# would raise an error because y doesn't exist
err6 = """
x=y

"""

# Viper(err6).interperter()

# would raise an error because while should be followed by a logical expression or just a variable
err7 = """
x=8
while x+3{
x=1
}
"""

# Viper(err7).interperter()

# would raise an error because starting index of range function should be smaller than ending index
err8 = """
for i in range(5, 3){
x=1
}
"""

# Viper(err8).interperter()

err9 = """
x=0
x = x + "6"
y = x
isTrue = true
if( x<=10) && isTrue{
print("some str")
}

"""
Viper(err9).interperter()

