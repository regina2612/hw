import datetime

class Man:
	def __init__(self, name, year, month, day):
		self.name = name
		self.year = year
		self.month = month
		self.day = day

	def age(self):
		birthday = datetime.date(self.year, self.month, self.day)
		years = datetime.date.today().year - birthday.year
		return years

m = Man('Ivan', 2000, 12, 31)	
print('Ivan turned in 2018: ' + str(m.age()) + ' years old!')