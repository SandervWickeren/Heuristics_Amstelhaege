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

		# Temp dict with coordinates
		tmpdict = {"M":[(1,1)], "B": [(6, 4)]}

		total_price = 0

		# For every housetype
		for housetypes in tmpdict.keys():
			print (housetypes)


			# For every coordinate:
			for coordinates in tmpdict[housetypes]:
				

				#
				if housetypes == "M":
					width = 2
					length = 2
					freespace = 1
					price = 610000
					percentage = 6
				else:
					width = 3
					length = 2
					freespace = 1
					price = 399000
					percentage = 4 

				allowed = [0, 5, 4]

				check = True
				distance = 0
				while check:
					distance += 1
					check = generic.allowedFreespace(tmp, coordinates[0], coordinates[1], width, length, freespace + distance, allowed)
					

				# Calculate house price
				sell_price = price * (1 + (percentage / 100) * (distance - freespace))
				total_price += sell_price
				print ("Gevonden afstand {0} met een prijs van {1}".format(distance, sell_price))
		print (total_price)
		return 0


	alg_random.startGeneration(20, 10)
	#gr = genMap(160, 180)
	#print (placeWater(gr))
	#calcScore("ja");
	#Testcalcscore()
	

if __name__ == "__main__":
	import random
	import copy
	import math
	import sys
	import os

	# Get current location
	dir_path = os.path.dirname(os.path.realpath(__file__))

	# Add custom classes and functions
	sys.path.insert(0, dir_path + "\Functions")
	sys.path.insert(0, dir_path + "\Classes")

	import generic
	import alg_random


	# Choose the variant between 20/40/60
	variant = 20

	# Choose the amount of maps it should generate.
	maps = 1

	# Choose if you want a visualization (1 = yes, 0 = no)
	# If you generate multiple maps it 'll only show the 
	# best one after the final map is generated.
	visualization = 1

	main(variant, maps, visualization)