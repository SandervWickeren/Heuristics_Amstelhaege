"""Teamname: Sandy & Co
Names and StudentID:
-
-
- Sander van Wickeren (11060999)

Description:
~"""

def main():
	"""
	explain
	"""
	def GenHouse(surface, fill_color, border_color, rect, border=1):
		surface.fill(border_color, rect)
		surface.fill(fill_color, rect.inflate(-border*2, -border*2))

	def Draw100():
		for i in range(20):
			y = random.randint(0, 180 * TileSize)
			x = random.randint(0, 160 * TileSize)

			GenHouse(gameDisplay, red, black, pygame.Rect(x, y, 32, 32), 8)

	# Define colors.
	white = (255,255,255)
	black = (0,0,0)
	red = (255, 0, 0)

	# Size of the tiles in pixels.
	TileSize = 4

	# Setting up resolutions.
	gameDisplay = pygame.display.set_mode((180 * TileSize,160 * TileSize))
	pygame.display.set_caption('Amstelhaege')

	gameRun = True
	a = True

	gameDisplay.fill(white)
	if a == True: 
		Draw100()
	pygame.display.update()
	a = False

	while gameRun:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameRun = False





if __name__ == "__main__":
	import pygame
	import random
	main()