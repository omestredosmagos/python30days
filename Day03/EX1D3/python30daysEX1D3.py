# Exercises from 1 to 11
age = 28
height = 1.83
complex_number = 1+2j

# Calculating the triagle area

base = input('Insert the triangle\'s base value: ')
height = input('Insert the triangle\'s height: ')
triangle_area = 0.5*float(base)*float(height)
print('\nThe area of the triangle is ', triangle_area)


# Calculating the triagle perimeter

side1 = input('\nInsert the first side of the triangle: ')
side2 = input('Insert the second side of the triangle: ')
side3 = input('Insert the third side of the triangle: ')
perimeter = side1+side2+side3
print('\nThe perimeter of the triangle is ', perimeter)


# Calculating the Retangle's Area and Perimeter

lenght = int(input('\nInsert the retangle\'s lenght: '))
width = int(input('\nInsert the retangle\'s width: '))
area_retangle = lenght*width
perimeter_retangle = 2*(lenght+width)
print('\nThe retangle\'s area is ', area_retangle, ' and the perimeter is ', perimeter_retangle)


# Calculating the Circle's Area and Circumference

radius_circle = int(input('\nInsert the Circle\'s radius: '))
pi = 3.14
area_circle = 2*(radius_circle)**2
circumference = 2*pi*radius_circle
print('\nThe Circle\'s area is ', area_circle, ' and the circumference is ', circumference)


# Calculating the Slope (m=y2-y1/x2-x1) and Euclidean distance for the (2,2) and (6,10)

dataPoints1 = (2,2)
dataPoints2 = (6,10)
slope = (dataPoints1[1]-dataPoints2[1])/(dataPoints1[0]-dataPoints2[0])
euclidianDistance = (((dataPoints1[0] - dataPoints2[0])**2)+((dataPoints1[1] - dataPoints2[1])**2))**(1/2)
print('\n Giving the two data points (2,2) and (6,10), the slope and euclidian distance respectively are, ', slope, ' and ', euclidianDistance)


# Calculating the value of y=x^2+6x+9

x = int(input('\nTo calculate the y=x^2+6x+9 expression, insert the value for the \'x\': '))
y = (x**2)+(6*x)+9
print('\nThe value for the y is ', y)

