import datetime as dt

today_1 = dt.date.today()
today_3 = dt.date.today()+dt.timedelta(days=3)
print('Today: ' +str(today_1))
print('Today plus 3: ' +str(today_3))

colors = ['blue', 'black', 'red', 'orange']
for color in colors:
    print(color)

dict_colors ={0:'blue', 1:'black', 2:'red', 3:'orange'}
for key, value in dict_colors.items():
    print('El valor correspondiente a '+str(key)+' es: '+str(value))

x1, x2, x3, x4 = colors
print('Color 1: '+x1)
print('color 2: '+x2)
print('color 3: '+x3)
print('color 4: '+x4)
