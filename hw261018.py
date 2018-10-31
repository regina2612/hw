# 1 задача 
def func ():
	res = 'Кыргызская Республика!'
	res1 = 'KP'
	res2 = 'Rudy on Rails'
	res3 = 'POR'
	res4 = 'For your interest'
	res5 = 'FYI'
	return res1, res3, res5

print(func())

# 2 задача 
class Sudscrider():
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def __repr__(self):
		return self.firstname + self.lastname

person = Sudscrider('Ivan', 'Ivanov')
print(person)

# 5 задача

class Cow():
	def make_sound(self):
		print('Myyy')

c = Cow()
c.make_sound()

# 6 задача

class Cat:
	def make_sound(self):
		print('May')

m = Cat()
m.make_sound()

# 7 задача

class Dog(object):
	def make_sound(self):
		print('Avav')

d = Dog()
d.make_sound()

def sum(a,b):
	return a+b
sum(3,4)