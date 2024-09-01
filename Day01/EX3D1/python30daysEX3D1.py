print('#### Part 1 ####\n')

print('Number Integer: ', 6)
print('Number Float: ', 3.14)
print('Number Complex: ', 1+1j)
print('String: ', 'Duda é linda')
print('Boolean: ', True)
print('List: ', ['pão', 'queijo', 'presunto', 'café'])
print('Tuple: ', ('python', 'java', 'c', 'javascript'))
print('Set: ', {15, 1, 50, 6})
print('Dictionary: ', {'nome': 'duarda', 'idade': 24, 'qualidade': 'inteligente'})

print('\n#### Part 2 ####\n')

dataPoints1 = (2,3)
dataPoints2 = (10,8)
euclidianDistance = (((dataPoints1[0] - dataPoints2[0])**2)+((dataPoints1[1] - dataPoints2[1])**2))**(1/2)

print('Euclidian Distance for the data points: ', dataPoints1, ' and ', dataPoints2, ' is = ', euclidianDistance)