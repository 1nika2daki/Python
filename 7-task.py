#7.Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x, y, z = 0, 0, 0

print ('x, y, z = 0, 0, 0_', not (x or y or z) == (not x and not y and  not z))

x, y, z = 0, 0, 1

print ('x, y, z = 0, 0, 1_', not (x or y or z) == (not x and not y and  not z))


x, y, z = 0, 1, 0

print ('x, y, z = 0, 1, 0_', not (x or y or z) == (not x and not y and  not z))

x, y, z = 1, 0, 1

print ('x, y, z = 1, 0, 1_', not (x or y or z) == (not x and not y and  not z))

x, y, z = 1, 1, 1

print ('x, y, z = 1, 1, 1_', not (x or y or z) == (not x and not y and  not z))

x, y, z = 1, 1, 0

print ('x, y, z = 1, 1, 0_', not (x or y or z) == (not x and not y and  not z))

x, y, z = 0, 1, 1

print ('x, y, z = 0, 1, 1_', not (x or y or z) == (not x and not y and  not z))

x, y, z = 1, 0, 1

print ('x, y, z = 1, 0, 1_', not (x or y or z) == (not x and not y and  not z))



