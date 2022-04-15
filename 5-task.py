#5.	Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30


enter_number = int(input('enter number =  '))


if enter_number % 5 ==0 and enter_number % 10 ==0:
    print('кратно 5  и  10 ')
    
    
elif enter_number % 15 ==0 and enter_number % 30 !=0:
    print('кратно  15 но не 30')
    

