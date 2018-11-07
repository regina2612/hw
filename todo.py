class Todo:
	todo_items = []

	def add_todo(self, item):
		self.todo_items.append(item)

	def list_items(self):
		for element in self.todo_items:
			print(element)

	def find(self, arg):
		for element in self.todo_items:
			if (element.name.find(arg) != -1):
				print([str(self.todo_items.index(element)) + ' ' + str(element.name)])


class TodoItem:
	is_done = False

	def __init__(self, name):
		self.name = str(name)

	def check(self):
		is_done = True

	def uncheck(self):
		is_done = False

	def __str__(self):
		return str(self.name) + ' status: ' + str(self.is_done)

	


ti1 = TodoItem('Item')
ti2 = TodoItem('Item2')
ti2.check()
td = Todo()
td.add_todo(ti1)
td.add_todo(ti2)
td.list_items()
td.find('m2')