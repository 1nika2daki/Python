#11.	Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.
import random


a=int(input(enter number , length on the list : ))
b=[]
x=1
while x<=a:
    
    k=random.randrange(a)
    b.append(k)
    x+=1
print(b)

