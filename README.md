# Heuristics_Amstelhaege
Project van het vak Heuristieken aan de UvA, de Amstelhaege case. Doel van het project is het zo optimaal mogelijk indelen van het gebied waarbij het meeste geld kan worden opgeleverd.

# Contributors:
- Tom Dekker (11031735)
- Laura Geerars (11007699)
- Sander van Wickeren (11060999)

# Indeling GitHub:
### Mappen
_Classes_: In deze map staan de classes die zijn opgesteld. Hierin staat nu de class House die gemaakt is om de verschillende soorten huizen (waarbij ook water een instantie is van de class House) uiteindelijk makkelijker te kunnen genereren.

_Functions_: In deze map staan de verschillende functies die zijn opgesteld. Hierin staan nu de files voor het algemene gedeelte (generic.py) van de functies dus die voor verschillende files de basis is. Ook staat de file voor het eerste algoritme, het random algoritme, in deze map (alg_random.py). Hieraan is de file voor het tweede algoritme, het Hill Climbing algoritme, toegevoegd (alg_hillclimb.py). Hieraan moet het derde algoritme nog worden toegevoegd. 

_Info_: In deze map staan informatieve files, dus een algemene file met een aantal git commands en de file voor het bijhouden van de argumentatie voor de IDEA punten. Deze is als het goed is tijdelijk.

_Timing_: In deze map staan een aantal files voor het kunnen berekenen van de snelheid ...

_Toestandsruimte_: In deze map staat tot nu toe een file voor het kunnen berekenen van de toestandsruimte. Deze zal tijdelijk zijn, maar voor nu is het fijn om die apart te hebben staan.

_docs_: In deze map komt alle documentatie/literatuur te staan die van belang is bij de case. 

_Results_: In deze map wordt alle nuttige/toepasbare informatie opgeslagen. In deze map staat de file read_write.py, die functies bevat voor het lezen en creëren van de visualisaties, wanneer deze een betere versie is dan die er bestaan, worden deze resultaten opgeslagen in de map Results. Een voorbeeld van een filename is "Type20HC - 11165430.0", dus variant 20, algoritme Hill Climber, met de verbeterde score van 11165430.0. 

Om de visualisatie van de algoritmes te kunnen runnen, kan dit door middel van het runnen van Main.py. In deze file kan de variant worden aangepast, dus de 20-, 40- of 60-huizen variant, het algoritme, deze hebben ieder een nummer gekregen. Deze toelichting staat ook in de comments boven het aanroepen van het algoritme. Ook kan in deze file de filename en het aantal loops worden aangepast. 

# Progressie:
Week 1:
- Eerste pogingen met pygame, random generatie van huizen.

Week 2:
- Er wordt gebruik gemaakt van de matplotlib package voor de visualisatie van het gebied.
- Basisfuncties werkende zoals; het genereren van huizen, map generatie,random nummer generatie.
- Transformatie naar python 3.
- Het aanroepen van een functie met varianten (20/40/60) als input.
- Eerste presentatie uitgevoerd.
- Resolutie grid aangepast x10.

Week 3:
- Werken aan score functie.
- Eerste algoritme werkende: random generatie van huizen en water.
- Literatuur/ideeën voor tweede en derde algoritme: Hill Climbing & Simulated Annealing

Week 4:
- Score functie werkende.
- Tweede presentatie uitgevoerd.
- Scorefunctie gekoppeld aan gegenereerde kaart.
- Alles omgezet naar classes.
- Functies en algoritmes eigen bestanden met functies.

Week 5:
- Tweede algoritme werkende: Hill Climbing.
- Upper / Lower bound zijn opgesteld.
- Experiment uitgevoerd: heeft het zin om water ook te verplaatsen bij Hill Climbing algoritme?
- Experiment uitgevoerd: heeft het zin om meerdere iteraties uit te voeren bij 

Week 6:
- Opslaan van alleen nuttige/toepasbare informatie.

# Planning:
Week 6:
- Derde algoritme: Simulated Annealing

Week 7:
- Experiment: Optimaliseren van algoritme 1: het vaststellen van de plekken van de maisons, water en andere huizen random generalisatie.
- Experiment: vergelijken algoritme 1 met algoritme 2.
- Experiment: vergelijken algoritme 2 met algoritme 3.
- Experiment: vergelijken drie algoritmen.
- Experiment: optimaliseren algoritme 2.
- Experiment: optimaliseren algoritme 3.


