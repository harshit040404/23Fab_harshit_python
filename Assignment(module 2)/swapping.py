
x = 5
y = 10
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

# create a temporary variable and swap the values

x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)
