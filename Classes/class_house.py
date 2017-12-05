print ("Succesfully imported class_house")
import random

class House:

	# Class variable
	num_of_houses = 0
	resolution = 1

	# Constructor of the class
	def __init__(self, length, width, freespace, price, priceimprovement, ID, h_type, resolution):
		self.length = length
		self.width = width
		self.freespace = freespace
		self.price = price
		self.priceimprovement = priceimprovement
		self.resolution = resolution

		# Used for visualization
		self.id = ID

		# Used to dermine the house type (Maison, bungalow etc.)
		self.h_type = h_type
		
		# Other variables
		self.x = 0
		self.y = 0
		self.multiplier = 0

		# Adds house to class variable
		House.num_of_houses += 1

	# Class instance function applies (and uses) only values from
	# an instance of the class. 
	def surface(self):
		return width * length

	def set_x(self, newX):
		self.x = newX

	def set_y(self, newY):
		self.y = newY

	def set_multiplier(self, newM):
		self.multiplier = newM

	def random_y(self, grid):
		self.y = random.randint(self.freespace, len(grid) - self.freespace - self.length)

	def random_x(self, grid):
		self.x = random.randint(self.freespace, len(grid[0]) - self.freespace - self.width)

	def reduce_y(self, reduces):
		if self.y - reduces - self.freespace >= 0:
			self.y = self.y - reduces

	def increase_y(self, increases):
		self.y = self.y + increases

	def reduce_x(self, reduces):
		if self.x - reduces - self.freespace >= 0:
			self.x = self.x - reduces

	def increase_x(self, increases):
		self.x = self.x + increases

	def calc_price(self):
		if self.multiplier > 0:
			return self.price
		else:
			return self.price * (1 + (self.priceimprovement * self.multiplier) / 100)

	# Class method function applies to all instances of a class.
	@classmethod
	def set_resolution(cls, resolution):
		cls.resolution = resolution






