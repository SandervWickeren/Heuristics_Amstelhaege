class house:

	# Class variable
	num_of_houses = 0
	resolution = 1

	# Constructor of the class
	def __init__(self, length, width, freespace, price, priceimprovement):
		self.length = length
		self.width = width
		self.freespace = freespace
		self.price = price
		self.priceimprovement = priceimprovement

		# Adds house to class variable
		house.num_of_houses += 1

	# Class instance function applies (and uses) only values from
	# an instance of the class. 
	def surface(self):
		return width * length

	# Class method function applies to all instances of a class.
	@classmethod
	def set_resolution(cls, resolution):
		cls.resolution = resolution






