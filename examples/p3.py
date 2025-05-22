operator=input("Enter an operator + - *");
num1=float(input("Enter the 1st number"));
num2=float(input("Enter the second number"));


if operator=='+':
   result=num1+num2;

elif operator=='-':
   result=num1-num2;

elif operator=='*':
   result=num1*num2;

else: 
   result="Operation Not Found";

print(" Result is ", result);
