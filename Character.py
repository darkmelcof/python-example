class Character:
	"""docstring for Personnage
	- name
	- sex
	- power"""

	number = 0
	def __init__(self):
		Character.number += 1
		self.name = "Alberto"
		self.sex = "male"
		self.power = "fire"
	def show(self):
		print("My character is a {} and we used to call him {}".format(self.sex,self.name));
		print("The number of character is : {} ".format(Character.number))
		
