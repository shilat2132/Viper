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
# Viper(code1).interperter()


code2 = """
x = sqrt(9)+3
y = max(x, 17)
"""
Viper(code2).interperter()
