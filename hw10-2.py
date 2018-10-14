# 2 задача
 
filename1 = input('Введите название копируемого файла: ')
filename2 = input('Введите название нового файла: ')
file1 = open(filename1, 'r')
file2 = open(filename2, 'a')
file2.write(file1.read())
text = input('Какой текст хотите поместить в файл: ')
file2 = open(filename2, 'a')
file2.write(text)
file1.close()
file2.close()
print('Копирование успешно завершено')


# c with
filename1 = input('Введите название копируемого файла: ')
filename2 = input('Введите название нового файла: ')

with open (filename1, 'r') as f1, open(filename2, 'a') as f2:
	f2.write(f1.read())
	text = input('Какой текст хотите поместить в файл: ')
	f2.write(text)
    

print('Копирование успешно завершено')
