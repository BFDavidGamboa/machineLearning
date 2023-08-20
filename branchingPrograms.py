booleanExpression = False

if booleanExpression:
    print(booleanExpression)
else:
    print(booleanExpression)

a = 6

if a%2 == 0:
    print('Even')
else:
    print('Odd')

print('Done with conditional')

if a%2 == 0:
    if a%3 ==0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and and not by 3')
elif a%3 == 0:
    print('Divisible by 3 and not by 2')


x = 5
y = 3
z = 7

result = 0

if x%2 != 0 and y%2 != 0 and z%2 != 0:
    if  x>y>z:
        print(x, ' is the largest number')
    if y>x>z:
        print(y, ' is the largest number')
    if z>y>x:
        print(z, ' is the largest number')
elif x%2 == 0 and y%2 == 0 and z%2 == 0:
    print('All numbers are Even')







