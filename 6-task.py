#6.Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

monday    = Понедельник
tusday    = Вторник
wednesday = Среда
thursday    = Четверг
friday    = Пятница
saturday  = Суббота
sunday    = Воскресенье
week_day  =  рабочий день
weekend   =  выходной

input_number =int(input(пожалуста введите число От 1 До 7 -))
while input_number < 0 or input_number > 7:

    print (вы вышли за рамкиб пожалуста введите число От 1 До 7 )
    input_number =int(input(пожалуста введите число От 1 До 7 -))

if input_number ==1 :
    print(monday + week_day)

elif input_number == 2 :
    print (tusday + week_day)

elif input_number == 3 :
    print (wednesday + week_day)

elif input_number == 4 :
    print (thursday + week_day)

elif input_number == 5 :
    print (friday + week_day)

elif input_number == 6 :
    print (saturday + weekend)

elif input_number == 7 :
    print (sunday + weekend)
