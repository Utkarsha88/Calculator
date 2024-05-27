import math
str="Calculator"
print(str.center(80))
user=input("Enter the expression you want to calculate: ")
operand1="0"
index=0
operator="+"
for i in range(len(user)+1):
    
    
    if(user[i]=="+" or user[i]=="-" or user[i]=="*" or user[i]=="/" ):
        operator=user[i]
        index=i+1
        break

    elif(user[i]!="+" and user[i]!="-" and user[i]!="*" and user[i]!="/"):
       operand1 =operand1+ user[i]
       
    
    # elif(user[i]==" "):
    #     continue

operand2="0"
for i in range(index, len(user)):
    if(user[i]=="+" or user[i]=="-" or user[i]=="*" or user[i]=="/" ):
        print("Warning! Please donot repeat your operaator next time")
    else:
        operand2= operand2+ user[i]



match operator:
    case "+":
        print("Calculated Result: ")
        print(float(operand1)+float(operand2))
    
    case "-":
        print("Calculated Result: ")
        print(float(operand1)-float(operand2))
    
    case "*":
        print("Calculated Result: ")
        print(float(operand1)*float(operand2))
    
    case "/":
        print("Calculated Result: ")
        print(float(operand1)/float(operand2))
    
    case _:
        print("wrong input")
