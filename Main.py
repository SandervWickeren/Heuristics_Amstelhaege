"""Teamname: Sandy & Co
Names and StudentID:
- Tom Dekker (11031735)
- Laura Geerars (11007699)
- Sander van Wickeren (11060999)

Description:
"""

def main(variant, maps, visualization):
	"""
	explain
	"""


	def TestClasses():
		Maison = class_house.house(10.5, 11, 6, 610000, 6, 3, "M")
		print (Maison.length)	
				


	def Testcalcscore():
		grid = [[0, 0, 0, 0, 0, 0, 0, 0],
			    [0, 0, 0, 0, 0, 0, 0, 0],
			    [0, 0, 1, 0, 0, 0, 0, 0],
			    [0, 0, 0, 0, 0, 0, 0, 0],
			    [0, 0, 0, 0, 0, 0, 0, 0],
			    [0, 0, 0, 5, 5, 5, 5, 5],
			    [0, 0, 0, 5, 1, 1, 1, 5],
			    [0, 0, 0, 5, 1, 1, 1, 5],
			    [0, 0, 0, 5, 5, 5, 5, 5]]

		y = 6
		x = 4
		w = 3
		l = 2
		f = 0

		test = True
		d = 0
		while test:
			f += 1
			d += 1
			test = generic.allowedFreespace(grid, y, x, w, l, f, [0, 5, 4, 6, 7, 8, 9])

		print (f)


	def calcScore(grid):

		# Temp test grid
		tmp = [[5, 5, 5, 5, 0, 0, 0, 0],
			   [5, 1, 1, 5, 0, 0, 0, 0],
			   [5, 1, 1, 5, 0, 0, 0, 0],
			   [5, 5, 5, 5, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 5, 5, 5, 5, 5],
			   [0, 0, 0, 5, 2, 2, 2, 5],
			   [0, 0, 0, 5, 2, 2, 2, 5],
			   [0, 0, 0, 5, 5, 5, 5, 5]]

		tmp2 = [[5, 5, 5, 5, 0, 0, 0, 0],
			    [5, 1, 1, 5, 0, 0, 0, 0],
			    [5, 1, 1, 5, 0, 0, 0, 0],
			    [5, 5, 5, 5, 0, 0, 0, 0],
			    [0, 0, 0, 0, 0, 0, 0, 0],
			    [0, 0, 0, 0, 0, 0, 0, 0],
			    [0, 0, 0, 0, 0, 0, 0, 0],
			    [0, 0, 0, 0, 0, 0, 0, 0],
			    [0, 0, 0, 0, 0, 0, 0, 0]]

		tmp3 = [[0, 0, 0, 0, 0, 0, 0, 0],
			    [0, 0, 0, 0, 0, 0, 0, 0],
			    [0, 0, 5, 5, 5, 5, 0, 0],
			    [0, 0, 5, 1, 1, 5, 0, 0],
			    [0, 0, 5, 1, 1, 5, 0, 0],
			    [0, 0, 5, 5, 5, 5, 0, 0],
			    [0, 0, 0, 0, 0, 0, 0, 0],
			    [0, 0, 0, 0, 0, 0, 0, 0],
			    [0, 0, 0, 0, 0, 0, 0, 0]]

		# (0,0), (0,3), (3,3), (3, 0)
		# (5, 3), (5, 7), (8, 7), (8, 3)

		# classes:
		House1 = class_house.house(2, 2, 1, 610000, 6, 2, "Test")
		House2 = class_house.house(2, 3, 1, 399000, 4, 3, "Test")
		House1.setX(1)
		House1.setY(1)
		House2.setX(4)
		House2.setY(6)

		placed_houses = [House1, House2]

		total_price = 0

		# For every class
		for x in placed_houses:

			allowed = [0, 5, 4]

			check = True
			distance = 0
			while check:
				distance += 1
				check = generic.allowedFreespace(tmp, x, x.freespace + distance, allowed)
				

			# Calculate house price
			sell_price = x.price * (1 + (x.priceimprovement / 100) * (distance - x.freespace))
			total_price += sell_price
			print ("Gevonden afstand {0} met een prijs van {1}".format(distance, sell_price))

		print (total_price)
		return 0


	alg_random.startGeneration(20, 10)
	#gr = genMap(160, 180)
	#print (placeWater(gr))
	#calcScore("ja");
	#Testcalcscore()
	#TestClasses()
	

if __name__ == "__main__":
	import random
	import copy
	import math
	import sys
	import os

	# Get current location
	dir_path = os.path.dirname(os.path.realpath(__file__))

	# Add custom classes and functions
	sys.path.insert(0, dir_path + "/Functions")
	sys.path.insert(0, dir_path + "/Classes")

	import generic
	import alg_random
	import class_house


	# Choose the variant between 20/40/60
	variant = 20

	# Choose the amount of maps it should generate.
	maps = 1

	# Choose if you want a visualization (1 = yes, 0 = no)
	# If you generate multiple maps it 'll only show the 
	# best one after the final map is generated.
	visualization = 1

	main(variant, maps, visualization)