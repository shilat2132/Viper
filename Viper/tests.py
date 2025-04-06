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
"""
Viper(code1).interperter()

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
x=6
if x{
print("yes")
}
"""
# Viper(code4).interperter()

code5 = """
a = [1, -5, "hello", "world"]
a.append("!")
str = ""
for i in a{
print(i)
str = str.CONCAT(" ")
str = str.CONCAT(i)
}
"""
# Viper(code5).interperter()


code6 ="""
x = 10
y = 5
sum = x + y
if sum > 10 {
    print("Sum is greater than 10")
} else {
    print("Sum is 10 or less")
}

for i in range(3) {
    print("Iteration:", i)
}
"""
# Viper(code6).interperter()

code7 = """
arr = [1, 2, 3]
sum = 0
for num in arr {
    sum = sum + num
}
print("Sum of array:", sum)

text = "HELLO"
if text.isUpper() {
    print("Text is uppercase")
} else {
    print("Text is not uppercase")
}
"""
# Viper(code7).interperter() 





code8 = """
text = true
if text {
    print("This condition is boolean")
}
x=5
if x!=5{
x=9
}
else
{
print("this is the else block and it works")
}

arr = ["tuples"]
len = arr.length()
tup = ("are", "fun")
for t in tup{
arr.append(t)
}
areIndex = arr.index("are")
if arr.index("array") == -1{
print("can't find array word in arr")
}

arr.set(areIndex, "are not")
element = arr.get(areIndex)
print(arr)
arr.remove(0)
arr.addItem(0, "arrays")
print("No! ", arr)

"""

# Viper(code8).interperter()

code10 = """
tup = (9, 1, 3)
tup_to_add = (21, 17, 6)
tup2 = tup.combine(tup_to_add)
print(tup2)

index_of_3 = tup2.index(3)
print(index_of_3)
item4 = tup2.getItem(4)
sorted = tup2.sorted()
len = tup2.length()
"""
# Viper(code10).interperter()



code11 = """
lo = "all lower"
up = "ALL UPPER"
if lo.isLower(){
print(lo, "is all lower")
}
if up.isUpper(){
print(up, "is all upper")
}

text = "The bigdata data scientict was analyzing datas"
new_text = text.REPLACE("data", "structure")
print(new_text)
"""
# Viper(code11).interperter()

code12 = """
x = 20/5
y=x%3
f = false
t = !f

if !f{
print(f)
}
"""
# Viper(code12).interperter()

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


# would raise an error for trying to add a number and a string
err9 = """
x=0
x = x + "6"
y = x
isTrue = true
if( x<=10) && isTrue{
print("some str")
}

"""
# Viper(err9).interperter()

# would throw an error for using an inappropriate method on an array.
err10 = """
arr = [1, 2, 3]
arr.REPLACE(1, "one")  
"""
# Viper(err10).interperter()

# would raise an error because a number is not iterable
err11 = """
a= 4
for i in a{
print(i)
} 
"""
# Viper(err11).interperter()