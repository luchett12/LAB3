def mayor(num1,num2,num3):
    if(num1 > num2 and num1 > num3):
        return num1
    if(num2 > num1 and num2 > num3):
        return num2
    if(num3 > num2 and num3 > num2):
        return num3

print("Hola crack ingresa el 1: ")
num1 = int(input())
print("Hola crack ingresa el 2: ")
num2 = int(input())
print("Hola crack ingresa el 3: ")
num3 = int(input())

print(f"El mayor es:  {mayor(num1,num2,num3)}")