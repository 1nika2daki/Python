# 4.	Показать первую цифру дробной части числа

number= 2341.94345945


number2=str(round(number,1))
list1=[]
for i in number2:
    list1.append(i)
print(list1[-1])
