import random

print('Игра угадай число!')
ran = int(input('Введите число от 1 до 20: '))
random.randint(1, 20)
9

i = 0 
while i < 4:
	print(input('Введите число от 1 до 20: '))
	i += 1 
	if ran < 1 and ran < 8:
	    res = 'Слишком мало!'
	elif ran == 9:
		res = 'Вы выйграли!'
	else:
		ran > 10 and ran < 20
		res = 'Слишком много'

print(res)