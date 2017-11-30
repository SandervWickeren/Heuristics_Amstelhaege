print ("Succesfully imported class_house")

class house:

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
		house.num_of_houses += 1

	# Class instance function applies (and uses) only values from
	# an instance of the class. 
	def surface(self):
		return width * length

	def setX(self, newX):
		self.x = newX

	def setY(self, newY):
		self.y = newY

	def setMultiplier(self, newM):
		self.multiplier = newM

	def reduceY(self, reduces):
		if self.y - reduces - self.freespace >= 0:
			self.y = self.y - reduces

	def increaseY(self, increases):
		self.y = self.y + increases

	def reduceX(self, reduces):
		if self.x - reduces - self.freespace >= 0:
			self.x = self.x - reduces

	def increaseX(self, increases):
		self.x = self.x + increases

	def calcPrice(self):
		if self.multiplier > 0:
			return self.price
		else:
			return self.price * (1 + (self.priceimprovement * self.multiplier) / 100)

	# Class method function applies to all instances of a class.
	@classmethod
	def set_resolution(cls, resolution):
		cls.resolution = resolution






