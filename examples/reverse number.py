num=int(input('enter a number'));
rev=0;
if num>0:
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=trunc(num/10)
     print('reverse number is ' str(rev))
else:
    print('given number is not reversable')
