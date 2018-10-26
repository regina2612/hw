class Phone:
	def __init__(self, brend, model, price):
		self.brend = brend
		self.model = model
		self.price = price

	def  get_phone_info(self):
		return f'Телефон {self.model} {self.price}'

if __name__ == '__main__':
	apple = Phone('Apple', 'iphone xs', 75000)
	apple_1 = input('Введите модель телефона: ')
	print(apple.get_phone_info())