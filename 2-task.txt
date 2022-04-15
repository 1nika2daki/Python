# 2.	Найти максимальное из пяти чисел


number_list =[]
n=1
while n !=6:
    enter_number= int (input (fplease enter {n} number = ))
    number_list.append(enter_number)
    n+=1



maxnumber=max(number_list)

print(f'the maximum number on yhis list is {maxnumber}')
