"""
Uitleg:

Het algoritme werkt in een aantal stappen om een willekeurige kaart
te genereren. 


1. De basis functie
'startGeneration' wordt aangeroepen met de variabele
variant; die aangeeft of er 20, 40 of 60 huizen moeten worden gegenereerd
en resolution; wat gebruikt is om de resolutie van de kaart groter te maken.
De kaart wordt groter gemaakt om ervoor te zorgen dat we minder ruimte 
verliezen doordat de vierkante hoeken nu minder vierkant worden (er kunnen
meer 'pixels' gebruikt worden om een ronding te creëren). We hebben de 
keuze gemaakt om dit te doen ipv rond hoeken omdat we vonden dat het 
niet een groot genoegen impact zal hebben op de score. Wel resulteert
dit in dat we onze beste uitkomst nooit de allerbeste kunnen noemen.

2. Water genereren
Water generatie is de eerste stap in het algoritme. Er is bekend dat
20 procent van het totale oppervlak bestaat uit water en dat het uit
maximaal 4 lichamen mag bestaan die een verhouding hebben van 1 tot 4.
Er word een willekeurige oppervlakte gekozen tussen 4 * resolutie en
het totale wateroppervlakte. Aan de hand van dit oppervlakte wordt 
gezocht naar de juiste lengte en breedte maten die erbij passen.
Om dichter bij een vierkant uit te komen wordt eerst de wortel
van de oppervlakte uitgerekend en vanaf daar gezocht naar hele 
getallen waarbij Oppervlakte MOD lengte = 0 
--> wanneer gevonden hebben we een breedte. En wordt de verhouding
gecontroleerd
--> wanneer niet gevonden wordt dit oppervlakte niet opgeslagen
en begint het opnieuw

Om te voldoen aan het maximale aantal waterlichamen wordt de laatste
oppervlakte mogelijk bepaald door de andere 3 lichamen die al gemaakt 
zijn, namelijk de oppervlakte die over is. Nu kan het zo zijn dat 
het oppervlakte dat over is niet kan worden voorzien van lengte
of breedte maat (bv als oppervlakte een priemgetal is). In dit
geval worden de laatste twee oppervlaktes gedropt en begint het
algoritme opnieuw. Op deze wijze zal er nooit een endless loop
onstaan en altijd voldoende water gegenereerd worden. Ten slotte
worden lengte en breedte willekeurig omgedraaid zodat er geen vlakke
onstaan die altijd dezelfde kant op wijzen.

De gevonden oppervlakten worden op willekeurige coordinaten geplaatst
zodat deze correct binnen de kaart vallen

3. Huizen
De huizen worden na het water gegenereerd. Ze krijgen ook een willekeurige
coordinaten. Waarbij het plaatsen alleen voltooid wordt wanneer het
voldoet aan de contraints dat verplichte vrije ruimte binnen de kaart
moet vallen en dat ze niet mogen overlappen. Ze worden van groot naar
klein op de kaart gezet. Beginnend bij Maisons dan bungalows en tenslotte
eengezinswoninngen.

Alle huizen en de wateroppervlakten kijgen eigen instanties van de 
'house' class. Deze worden toegevoegd aan een lijst zodat ze makkelijk
bereikbaar zijn voor andere functies.

"""
import alg_hillclimb
import random
import generic
import math
import os
import sys

# Get current location
dir_path = os.path.dirname(os.path.realpath(__file__))

# Add custom classes and functions
sys.path.insert(0, dir_path.split("\\")[-1] + "\Classes")
import class_house

sys.path.insert(0, dir_path.split("\\")[-1] + "\Results")
import read_write

def startGeneration(variant, resolution, loops):
		"""
		Variant is the number of houses that has
		to be placed, resolution changes the size
		of the map.	
		"""
		# Check for valid resolution
		if resolution % 2 != 0:
			print ("Resolution should be an even integer.")
			return 

		# Set high score:
		if variant == 20:
			high_score = 9932670

		# House distirbution:
		familyHome_count = 0.60 * variant
		bungalow_count = 0.25 * variant
		maison_count = 0.15 * variant

		for loops in range(loops):

			# Initialize Classlist
			placed_houses = []
			placed_water = []

			# Initialize values
			gr = generic.genMap(180 * resolution, 160 * resolution)

			# Set length and width based on resultion.
			fam_length = int(resolution * 8)
			fam_width = int(resolution * 8)
			fam_freespace = int(resolution * 2) 

			bung_length = int(resolution * 7.5)
			bung_width = int(resolution * 10)
			bung_freespace = int(resolution * 3) 

			mais_length = int(resolution * 10.5)
			mais_width = int(resolution * 11)
			mais_freespace = int(resolution * 6)

			# Water
			# Generate water parts
			water_parts = genWater(gr, resolution)

			# Place water parts in grid:
			for part in range(len(water_parts)):
				W = 0

				# Loop until correctly placed.
				while W != 1:

					# Define class instance
					Water = class_house.House(water_parts[part][1], water_parts[part][0], 
										   1, 0, 0, 4, "W", resolution)

					ngrid = genHome(gr, Water)

					# Check for success:
					if ngrid == False:
						print ("No succesfull placement Water")
					else:
						print ("Water {0} placed!".format(W))
						gr = list(ngrid)

						# Add water to list
						placed_houses.append(Water)
						
						W = 1


			# Maisons
			M = 0
			while M != maison_count:

				# Define class instance
				Maison = class_house.House(mais_length, mais_width, 
										   mais_freespace, 610000, 6, 1, "M", resolution)

				ngrid = genHome(gr, Maison)

				# Check if house succsfully placed:
				if ngrid == False:
					print ("No succesfull placement Maison")
				else:
					print ("Maison {0} placed!".format(M))
					gr = list(ngrid)

					# Add maison to list
					placed_houses.append(Maison)

					M += 1

			# Then bungalows
			B = 0
			while B != bungalow_count:

				# Define class instance
				Bungalow = class_house.House(bung_length, bung_width, 
										   bung_freespace, 399000, 4, 2, "B", resolution)

				ngrid = genHome(gr, Bungalow)

				# Check for succes:
				if ngrid == False:
					print ("No succesfull placement Bungalow")
				else:
					print ("Bungalow {0} placed!".format(B))
					gr = list(ngrid)

					# Add maison to list
					placed_houses.append(Bungalow)

					B += 1 

			# Then Family homes
			F = 0
			while F != familyHome_count:

				# Define class instance
				Familyhome = class_house.House(fam_length, fam_width, 
										   fam_freespace, 285000, 3, 3, "F", resolution)

				ngrid = genHome(gr, Familyhome)

				# Check for succes:
				if ngrid == False:
					print ("No succesfull placement Family Home")
				else:
					print ("Family home {0} placed!".format(F))
					gr = list(ngrid)

					# Add maison to list
					placed_houses.append(Familyhome)

					F += 1

			# Calculate score using Placed houses
			sc = generic.calculateScore(gr, placed_houses)
			name = ("Score: " + str(sc))

			# Only save to file when new record.
			fname = "Type{0} - {1}".format(variant, sc)

			if sc > high_score:
				read_write.write(fname, placed_houses)
				high_score = sc
				print ("New high score ({0}) in loop: {1}".format(sc, loops))
				print ("Writing to file..")

		return gr, placed_houses, sc

def genHome(grid, house):
	"""
	Input is a grid, length, width, freespace and id.
	It calls placeHouse function using random coordinates.
	"""
	house.random_x(grid)
	house.random_y(grid)
	return generic.placeHouse(grid, house)

def genWater(grid, resolution):
	"""
	Current problems:
	 - Priemgetallen zorgen voor extra loops 
	 	--> misschien eerst testen?
	 - Als eerste getal groot is heb je veel loops
	 - Functie is nog wat rommelig.

	 Takes as input a grid and outputs a list containing
	 tuples of max 4 water spaces using the following layout:
	 (width, length, ratio, size), where the water takes
	 20 percent of the total surface.

	"""

	grid_surface = len(grid) * len(grid[0])

	# Amount of surface for the water.
	allowed_surface = round(0.2 * grid_surface)

	# Collection of the created surfaces
	water_surfaces = []

	# Min size of one water piece.
	min_single_size = 4 * resolution

	run = 0

	# Loop until 4 and enough surface:
	while allowed_surface != 0:
		run += 1
		print (allowed_surface)
		w = 0
		l = 0

		# Only generate random if we have more then 1 option left.
		if len(water_surfaces) < 3 and min_single_size != allowed_surface and allowed_surface > 5:
			size = random.randint(min_single_size, allowed_surface)

		
		# Otherwise the size is the allowed surface
		else:
			size = allowed_surface

		
		# Shouldn't go below 0
		if allowed_surface - size >= 0:
		
			# Calculate width and length if possible.
			# Starting from the square root causes the part to 
			# be more square instead of a straight line.
			init = round(math.sqrt(size))
			for i in range(init, 1, -1):
				if size % i == 0 and 1 <= math.ceil((size / i) / i) <= 4:
					w = i
					l = size / w

					# Reinit allowed surface
					allowed_surface -= size

					# Randomly switch width and length
					coinflip = random.randint(1, 2)
					if coinflip == 1:

						# Adds a tuple wich contains (width, length, ratio, surface)
						water_surfaces.append((w, int(l), round(l / w, 2), size))
					else:
						water_surfaces.append((int(l), w, round(l / w, 2), size))
					break
					
		if run > 4:
			# Drop last try and remake the surface.
			print ("Drop")
			try:
				run = 2
				allowed_surface += water_surfaces[-1][3]
				water_surfaces = water_surfaces[:-1]
			except:
				print ("wat")

	return water_surfaces