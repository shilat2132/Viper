from viper import Viper

code = """
x=0
x = x + "6"
y = x
isTrue = true
if( x<=10) && isTrue{
print("some str")
}

"""
Viper(code).interperter()