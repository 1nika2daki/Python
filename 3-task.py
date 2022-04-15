# 3.	Вывести на экран числа от -N до N

start_range= int (input ( 'enter sattr point please =  '))
#end_range = int (input ( 'please enter endpoint =  '))


rangenumb=range(-start_range, start_range+1)

for i in rangenumb:
    print(i)

