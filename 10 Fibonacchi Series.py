    # Program to find Fibonacchi series upto given numbers

a = 0
b = 1

x = int(input(" Enter the Number = "))

for i in range ( 1 , x+1 ) :
    c = a + b
    a = b
    b = c

print ( " Fibonacchui number series upto no ", x , " is = " ,c)
