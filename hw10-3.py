# 3 зададча 

foto1 = input('Введите название копируемого файла: ')
foto2 = input('Введите название нового файла: ')
f1 = open(foto1, 'rb')
f2 = open(foto2, 'ab')
f2.write(f1.read())
f1.close()
f2.close()
print('Копирование завершено')

# c with

foto1 = input('Введите название копируемого файла: ')
foto2 = input('Введите название нового файла: ')

with open(foto1, 'rb') as f1, open(foto2, 'ab') as f2:
	f2.write(f1.read())
print('Копирование завершено')