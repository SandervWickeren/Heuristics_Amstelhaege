"""
Contains functions that are used to read and write created maps.
These maps 'll be saved in a different folder called results.


Using structure
Type(0) - (score).pickle

for example:
Type20 - 9034500.pickle
"""
import pickle
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

print(dir_path.split("\\")[-2] + "\Functions")

# Add custom functions
sys.path.insert(0, dir_path.split("\\")[-2] + "\Functions")
import generic


def read(filename):

	
	# Get current location
	dir_path = os.path.dirname(os.path.realpath(__file__))

	# Open new file
	with open(dir_path + "\\" + filename + ".pickle", "rb") as load_file:
		houses = pickle.load(load_file)
		return houses
	
	return False

def write(filename, houses):

	# Get current location
	dir_path = os.path.dirname(os.path.realpath(__file__))

	# Open new file
	with open(dir_path + "\\" + filename + ".pickle", "wb") as new_file:

		print (dir_path + filename)

		# Dump the information into the file
		pickle.dump(houses, new_file)

		# Close the file after writing
		new_file.close()

	return

def read_and_visualize(filename):
	houses = read(filename)

	if houses != False:

		# Generate grid
		grid = generic.transformtoGrid(houses, 10)

		# Retrieve the score from filename

		# Return the visualization
		return generic.visualizeGrid(grid, "test")

	return False



