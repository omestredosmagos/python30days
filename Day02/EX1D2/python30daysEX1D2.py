# Basic operators
first_name = 'Nathan'
last_name = 'Alves'
fullname = first_name + " " + last_name
country = 'Brazil'
city = 'Pindamoiamgaba'
age = '28'
year = 1980
is_married = True
is_true = True
is_light_on = False
dictionary_values = {
    'First Name': first_name,
    'Last Name': last_name,
    'Fullname': fullname,
    'Country': country,
    'City': city,
    'Age': age,
    'Year': year,
    'Married?': is_married,
    'Light turned on?': is_light_on
}
# Math operators
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_two / num_one
remainder = num_two % num_one
exp = num_one**num_two
floor_division = num_one // num_two

print('#### Part 1 ####\n')
print("Variables and their values: ", dictionary_values)

print('\n#### Part 2 ####\n')
print('2.1 Checking the variables types:\n')
print(type(first_name))
print(type(last_name))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))

print('\n2.2 Checking the number of caracters of the first name using len: ', len(first_name))

print('\n2.3 The number of caracters of the First name is ', len(first_name), ' and the Last name is ', len(last_name))

print('\n2.4 Results of the math operators using ', num_one, ' as number one and ', num_two, ' as number two')
print('Total: ', total)
print('Difference', diff)
print('Mutiplication', product)
print('Division', division)
print('Modulus', remainder)
print('Floor Division', floor_division)

print('\n2.5 Calculating the circle properties\n')
# Circle Properties
circle_radius = 30
pi = 3.141592653589793
circle_area = pi * (circle_radius)**2
circle_circumference = (2*pi*circle_radius)

print('Giving the circle radius being = ', circle_radius, ', then the Area and Circumference respectively are', circle_area, ' and ', circle_circumference)

print('\n2.5.1 Calculating the circle area using an user input value\n')
circle_radius = input('Write the circle radius value: ')
circle_area = pi * (int(circle_radius))**2
circle_circumference = (2*pi*int(circle_radius))
print('Giving the circle radius being = ', circle_radius, ', then the Area and Circumference respectively are', circle_area, ' and ', circle_circumference)