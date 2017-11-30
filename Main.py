"""Teamname: Sandy & Co
Names and StudentID:
- Tom Dekker (11031735)
- Laura Geerars (11007699)
- Sander van Wickeren (11060999)

Beschrijving:
Het programma werkt als volgt:

"""

def main(variant, maps, visualization, algorithm):
	"""
	explain
	"""
	if algorithm == 1:

		# Second number is resolution and is by default 10.
		alg_random.startGeneration(variant, 10)

	#alg_random.startGeneration(20, 10)
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

	# Choose the algorithm
	# Random algorithm = 1
	# Hill climbing algorithm = 2
	# Simulated Annealing = 3
	algorithm = 1

	main(variant, maps, visualization, algorithm)