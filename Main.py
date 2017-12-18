"""Teamname: Sandy & Co
Names and StudentID:
- Tom Dekker (11031735)
- Laura Geerars (11007699)
- Sander van Wickeren (11060999)

Description:

The main file, containing all options to run the program. 
by changing 


"""

def main(variant, algorithm, filename, loops, visualization):
	"""
	All algorithms save automatically the best scores.
	"""

	# Random algorithm
	if algorithm == 1:

		# Second number is resolution and is by default 10.
		new_grid, houses, score = alg_random.startGeneration(variant, 10, loops)	


	# Hill climbing
	elif algorithm == 2:

		if filename == "":
			grid, houses, score = alg_random.startGeneration(variant, 10, loops)
			new_grid, score = alg_hillclimb.start_hillclimb(grid, houses, loops)

		# Use the filename
		else:
			houses = read_write.read(filename)

			# Check if succesfull:
			if houses != False:

				# Retrieve score and make grid
				score = filename.split(" ")[-1]
				grid = generic.transformtoGrid(houses, 10)

				# Call hill climb
				new_grid, score = alg_hillclimb.start_hillclimb(grid, houses, loops)

	# Simulated Annealing using directions
	elif algorithm == 3:
		
		if filename == "":
			grid, houses, score = alg_random.startGeneration(variant, 10, loops)
			new_grid, score = alg_simannealing.start_simannealing(grid, houses)

		# Use filename
		else:
			houses = read_write.read(filename)

			# Check for succes
			if houses != False:

				# Retrieve score and make grid
				score = filename.split(" ")[-1]
				grid = generic.transformtoGrid(houses, 10)

				# Call hill climb
				new_grid, score = alg_simannealing.start_simannealing(grid, houses)

    # Show a plot of a file
	elif algorithm == 4:
		houses = read_write.read(filename)

		if houses != False:

				# Retrieve score and make grid
				score = filename.split(".0")[0]
				grid = generic.transformtoGrid(houses, 10)

				title = "Score: {0}".format(score)

				generic.visualizeGrid(grid, title)

	# Simulated Annealing using switching
	elif algorithm == 5:
		
		if filename == "":
			grid, houses, score = alg_random.startGeneration(variant, 10, loops)
			new_grid, score = alg_simannealing_switch.start_simannealing(grid, houses)

		# Use filename
		else:
			houses = read_write.read(filename)

			# Check for succes
			if houses != False:

				# Retrieve score and make grid
				score = filename.split(" ")[-1]
				grid = generic.transformtoGrid(houses, 10)

				# Call hill climb
				new_grid, score = alg_simannealing_switch.start_simannealing(grid, houses)

	# Only show visualization if asked for.
	if visualization == 1:
		print ("Generating map..")
		generic.visualizeGrid(new_grid, score)


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
	sys.path.insert(0, dir_path + "/Results")

	import generic
	import alg_simannealing
	import alg_simannealing_switch
	import alg_random
	import alg_hillclimb
	import class_house
	import read_write


	# Choose the variant between 20/40/60
	variant = 20

	# Choose the algorithm / Function
	# Random algorithm = 1
	# Hill climbing algorithm = 2
	# Simulated Annealing (Directions) = 3
	# Open File and create visualization = 4
	# Simulated Annealing v2 (Switch) = 5
	algorithm = 5

	# The filename can be used for 2, 3 and 4:
	# 2, 3, 5: Applies hill climbing on the grid from the 
	# given file.
	# 4: Shows a visualization from grid
	# Leaving it empty causes it to use
	# a random valid grid.
	filename = ""

	# Select the amount of loops you want to execute.
	# Used by algorithm 1 and 2.
	loops = 1

	# Choose if you want a visualization (1 = yes, 0 = no)
	# If you generate multiple maps it 'll only show the 
	# last one.
	visualization = 1

	# Start program
	main(variant, algorithm, filename, loops, visualization) 