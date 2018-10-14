# 1 задача 

file = open('kyrgyzstan.txt', 'w')
text = input('Какой текст хотите поместить в файл: ')
file.write(text)
file.close()

print('Текст сохранен!')

file = open('kyrgyzstan.txt', 'r')
print('В данном тексте ' + str(len(file.read())) + ' символов!')
file.close()



# c with
text = input('Какой текст хотите поместить в файл: ')

with open('kyrgyzstan.txt', 'w') as f:
    f.write(text)
file = ('kyrgyzstan.txt')
with open(file, 'r') as f:
    print(len(f.read()))
