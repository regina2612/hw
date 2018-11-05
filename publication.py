class Publication:
	def __init__(self, name, date, pages, lidrary, type):
		self.name = name
		self.date = date
		self.pages = pages
		self.lidrary = lidrary
		self.type = type 

	def get_code_in_library(self):
		return f''

class Book(Publication):
	def __init__(self, name, date, pages, lidrary):
		Publication.__init__(self, name, date, pages, lidrary)
		self.type = book

class Magazine(Publication):
	def __init__(self, name, date, pages, lidrary):
		Publication.__init__(self, name, date, pages, lidrary)
		self.type = magazine

class Newspaper(Publication):
	def __init__(self, name, date, pages, lidrary):
		Publication.__init__(self, name, date, pages, lidrary)
		self.type = newspaper


 