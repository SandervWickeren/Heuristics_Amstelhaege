# Heuristics_Amstelhaege
Project van het vak Heuristieken aan de UvA, de Amstelhaege case. Er moet een wijk (van 160 bij 180 meter) worden ingedeeld met woningen. Er zijn drie varianten mogelijk qua indeling: de 20 huizen, 40 huizen en 60 huizen variant. Het aantal woningen in de wijk bestaat hierbij voor iedere variant voor 60% uit eengezinswoningen, 25% uit bungalows en 15% uit maisons.  Ieder soort huis heeft een andere verplichte vrijstand en een standaard waarde wat het oplevert. Iedere meter extra vrijstand kan zorgen voor een prijsverbetering. Doel van het project is het zo optimaal mogelijk indelen van de wijk, waarbij het meeste geld kan worden opgeleverd.

### Vereisten
De volgende installaties moeten uitgevoerd worden om de code correct te kunnen runnen. 
Hierbij is het het makkelijkst om Anaconda te gebruiken.
- [Installeer Anaconda](https://conda.io/docs/user-guide/install/index.html)
- [Installeer Python 3.6](https://www.python.org/downloads/release/python-360/)
- [Installeer matplotlib 2.1](https://matplotlib.org/2.1.0/users/installing.html)

### Runnen van de algoritmen
Om de verschillende algoritmen te runnen, kan dit met behulp van de Main.py file. In deze file kan er precies worden gekozen welk algoritme er gerund moet worden, welke variant, een eerder grid waarop een Hill Climber algoritme of Simmulated Annealing algoritme op toegepast kan worden, het aantal loops die uitgevoerd moeten worden en of er een visualisatie moet komen of niet.

Eerst kan er een variant uitgekozen worden. Dit kunnen 20, 40 of 60 huizen zijn.
'''py

	# Choose the variant between 20/40/60
	variant = 60
'''

Vervolgens kan er een algoritme uitgekozen worden. Ieder algoritme heeft een nummer toegekend gekregen die ingevuld kan worden.
'''py

	# Choose the algorithm / Function
	# Random algorithm = 1
	# Hill climbing algorithm = 2
	# Simulated Annealing (Directions) = 3
	# Open File and create visualization = 4
	# Simulated Annealing v2 (Switch) = 5
	algorithm = 3
'''

Ook kan er een visualisatie worden gegenereerd uit de Results map door hier de bestandsnaam in te vullen. Om een Hill Climber
of Simulated Annealing algoritme te runnen, moet dit op basis van een eerdere file die in de Results map staat. 
'''

	# The filename can be used for 2, 3 and 4:
	# 2, 3, 5: Applies hill climbing on the grid from the 
	# given file.
	# 4: Shows a visualization from grid
	# Leaving it empty causes it to use
	# a random valid grid.
	filename = "Type20HC - 27142740.0"

'''

Vervolgens kan het aantal loops worden geselecteerd. Bij het random algoritme gaat het om het aantal kaarten dat wordt gegenereerd, genereer bijvoorbeeld 1000 kaarten (dus 1000 loops), als er een betere score uitkomt dan al eerder is opgeslagen in de map Results, zal hij deze opslaan. 
Bij het Hill Climber algoritme gaat het om het aantal keer dat alle zijdes worden gecheckt voor alle huizen, bij een al eerder gegenereerde kaart. Als er uiteindelijk een betere score uitkomt dan al eerder is opgeslagen in de map Results, zal hij deze opslaan.


'''

	# Select the amount of loops you want to execute.
	# Used by algorithm 1 and 2.
	loops = 4
'''	


### Contributors:
- Tom Dekker (11031735)
- Laura Geerars (11007699)
- Sander van Wickeren (11060999)



### Indeling GitHub:
#### Mappen
_Classes_: In deze map staan de classes die zijn opgesteld. Hierin staat nu de class House die gemaakt is om de verschillende soorten huizen (waarbij ook water een instantie is van de class House) uiteindelijk makkelijker te kunnen genereren.

_Functions_: In deze map staan de verschillende functies die zijn opgesteld. Hierin staan nu de files voor het algemene gedeelte (generic.py) van de functies dus die voor verschillende files de basis is. Ook staat de file voor het eerste algoritme, het random algoritme, in deze map (alg_random.py). Hieraan is de file voor het tweede algoritme, het Hill Climbing algoritme, toegevoegd (alg_hillclimb.py). Hieraan moet het derde algoritme nog worden toegevoegd. 

_Info_: In deze map staan informatieve files, dus een algemene file met een aantal git commands en de file voor het bijhouden van de argumentatie voor de IDEA punten. Deze is als het goed is tijdelijk.

_Timing_: In deze map staan een aantal files voor het kunnen berekenen van de snelheid ...

_Toestandsruimte_: In deze map staat tot nu toe een file voor het kunnen berekenen van de toestandsruimte. Deze zal tijdelijk zijn, maar voor nu is het fijn om die apart te hebben staan.

_docs_: In deze map komt alle documentatie/literatuur te staan die van belang is bij de case. 

_Results_: In deze map wordt alle nuttige/toepasbare informatie opgeslagen. In deze map staat de file read_write.py, die functies bevat voor het lezen en creëren van de visualisaties, wanneer deze een betere versie is dan die er bestaan, worden deze resultaten opgeslagen in de map Results. Een voorbeeld van een filename is "Type20HC - 11165430.0", dus variant 20, algoritme Hill Climber, met de verbeterde score van 11165430.0. 

Om de visualisatie van de algoritmes te kunnen runnen, kan dit door middel van het runnen van Main.py. In deze file kan de variant worden aangepast, dus de 20-, 40- of 60-huizen variant, het algoritme, deze hebben ieder een nummer gekregen. Deze toelichting staat ook in de comments boven het aanroepen van het algoritme. Ook kan in deze file de filename en het aantal loops worden aangepast. 


