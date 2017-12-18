"""
Uitleg:

Dit algoritme werkt als een variant op onze hill climb. Er wordt
in eerst instantie een random huis gepakt. Vervolgens wordt
er een willekeurige kant gepakt en het huis een aantal stappen
die kant op geplaatst. De score wordt berekend en bij een verbetering
of gelijke score wordt de kaart gehouden. Wanneer er een verslechtering
optreedt wordt er aan de hand van een temperatuursfunctie gekeken
of deze verslechtering moet worden aangenomen of niet.
"""


def start_simannealing(grid, placed_houses):
	"""
	Takes as input a grid and a list
	containing instances of the house class.
	It outputs a new grid and list produced
	by the algorithm.

	"""
	import random
	import generic
	import sys
	import os
	import platform
	import math

    # Get current os
	os_name = platform.system()

	if os_name == "Windows":
		sp = "\\"
		i = -1
	elif os_name == "Darwin":
		sp = "/"
		i = -1

	# Get current location
	dir_path = os.path.dirname(os.path.realpath(__file__))

	sys.path.insert(0, dir_path.split(sp)[i] + "\Results")
	import read_write

	# Check if grid is given
	if grid == False:
		# Generate the grid
		grid = generic.transformtoGrid(placed_houses, 10)

	# Choose to amount of steps it should take for
	# every loop 1 = 0.1 meter
	step = 5

	# Initial temperature
	temperature = 100000000

	# Cooling rate
	# 0.003
	cooling_rate = 0.1
   
    # Hierbij ook
	minimal_temperature = 1
	start_temperature = temperature
	count = 0


    # Get start score
	score = generic.calculateScore(grid, placed_houses)
	best_score = score
	best_layout = list(placed_houses)
	print ("Old score: {0}".format(score))

   
	# Loop
	loop = 0
	while temperature > minimal_temperature:
		print ("-- Round {0} --".format(loop + 1))

		# Choose a random house
		house_index = random.randint(0, len(placed_houses) - 1)
		h = placed_houses[house_index]

		# Choose a random side
		side = random.randint(0, 4)

		if h.h_type != "W":

			# Counts the amount of times the same score is produced
			same_score_count = 0

			# Save old coordinates
			old_x = h.x
			old_y = h.y

			# Save old grid when possible
			if grid != False:
				old_grid = list(grid)

			# Check which side it has to move to:
			if side == 0:
				# Reduce y to move to the north.
				h.reduce_y(step)

			elif side == 1:
				# Increase x to move to the east
				h.increase_x(step)

			elif side == 2:
				# Increase y to move to the south
				h.increase_y(step)

			elif side == 3:
				# Decrease x to move to the west
				h.reduce_x(step)

			# Regenerate the grid
			grid = generic.transformtoGrid(placed_houses, 10)
			
			# Console feedback
			if grid == False:
				print ("Returned False")
				h.x = old_x
				h.y = old_y

			# Check if valid positioned
			if grid != False:

				# Get the new score
				new_score = generic.calculateScore(grid, placed_houses)

				# Score feedback print
				if new_score != score:
					print ("Loop {0}: O: {1} -- N: {2} -- D: {3}".format(loop,
						score, new_score, new_score - score))

				if new_score == score:
					same_score_count += 1
				else:

					# Check if accepted
					prob = acceptance_probability(score, new_score, temperature)
					chance = random.uniform(0, 1)
					print ("Prob: {0}, R: {1}".format(prob, chance))
					if prob > chance:

						print ("Current: {0} ::: New: {1}".format(score, new_score))

						# Keep current map
						score = new_score

						# Check if new best
						if score > best_score:
							best_score = score
							best_layout = list(placed_houses)

			loop += 1
			
			temperature = temperature * (1 - cooling_rate)
			print ("current temp: {0}".format(temperature))
			print ("---")

	# Save result
	variant = 20
	fname = "Type{0}SA - {1}".format(variant, score)
	read_write.write(fname, placed_houses)
	print ("Writing to file..")

	# Done
	print ("done")
	print("found score: {0}".format(best_score))
	return generic.transformtoGrid(best_layout, 10), best_score


def acceptance_probability(old_score, new_score, temperature):
	"""
	Takes in the old score, the new score and temperature.
	It return as output a value between 0-1 which represents
	the chance of acceptance.
	"""
	import math

	# If solution is better accept it
	if new_score > old_score:
		return 1

	# If solution is worse calculate acceptance probability
	# Find a good function that returns a value between 0-1
	# increase and decrease is from minimal 8550 --> (36600+)
	print ("Difference: {0}".format(new_score - old_score))
	return math.exp(((new_score - old_score) / temperature))

print ("alg_simannealing imported")