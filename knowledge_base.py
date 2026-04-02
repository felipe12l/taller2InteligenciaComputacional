from experta import *

class AnimalFact(Fact):
    """Información base sobre el animal"""
    pass

class AnimalExpertEngine(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.reasoning_log = []
        self.identified_species = None

    def log(self, text):
        self.reasoning_log.append(text)

    # Nivel 1: Clase
    @Rule(AnimalFact(tiene_pelo=True))
    def es_mamifero(self):
        self.declare(AnimalFact(clase="Mamífero"))
        self.log("Deducción: Es Mamífero (tiene pelo/glándulas mamarias).")

    @Rule(AnimalFact(tiene_plumas=True))
    def es_ave(self):
        self.declare(AnimalFact(clase="Ave"))
        self.log("Deducción: Es Ave (tiene plumas).")

    @Rule(AnimalFact(tiene_escamas_reptil=True))
    def es_reptil(self):
        self.declare(AnimalFact(clase="Reptil"))
        self.log("Deducción: Es Reptil.")

    @Rule(AnimalFact(tiene_piel_humeda=True))
    def es_anfibio(self):
        self.declare(AnimalFact(clase="Anfibio"))
        self.log("Deducción: Es Anfibio.")

    @Rule(AnimalFact(tiene_branquias=True))
    def es_pez(self):
        self.declare(AnimalFact(clase="Pez"))
        self.log("Deducción: Es Pez.")

    # Nivel 2: Dieta / Orden (algunos ejemplos)
    @Rule(AnimalFact(come_carne=True))
    def es_carnivoro(self):
        self.declare(AnimalFact(dieta="Carnívoro"))
        self.log("Deducción: Es Carnívoro (come carne).")

    @Rule(AnimalFact(come_plantas=True))
    def es_herbivoro(self):
        self.declare(AnimalFact(dieta="Herbívoro"))
        self.log("Deducción: Es Herbívoro (come plantas).")

    @Rule(AnimalFact(come_de_todo=True))
    def es_omnivoro(self):
        self.declare(AnimalFact(dieta="Omnívoro"))
        self.log("Deducción: Es Omnívoro (come de todo).")

    @Rule(AnimalFact(come_insectos=True))
    def es_insectivoro(self):
        self.declare(AnimalFact(dieta="Insectívoro"))
        self.log("Deducción: Es Insectívoro (come insectos).")

    @Rule(AnimalFact(come_cadaveres=True))
    def es_carronero(self):
        self.declare(AnimalFact(dieta="Carroñero"))
        self.log("Deducción: Es Carroñero (come animales muertos).")
        
    @Rule(AnimalFact(come_frutas=True))
    def es_frugivoro(self):
        self.declare(AnimalFact(dieta="Frugívoro"))
        self.log("Deducción: Es Frugívoro (come frutas).")

    # Nivel 3: Especies
    # Mamíferos
    @Rule(AnimalFact(clase="Mamífero"), AnimalFact(dieta="Carnívoro"),
          AnimalFact(caracteristica="piel_manchas_rosetas"), AnimalFact(caracteristica="vive_en_selva"), AnimalFact(caracteristica="felino_grande"))
    def jaguar(self):
        self.identified_species = "Jaguar"
        self.log("Especie Alcanzada: Jaguar")

    @Rule(AnimalFact(clase="Mamífero"), AnimalFact(dieta="Omnívoro"),
          AnimalFact(caracteristica="pelaje_negro"), AnimalFact(caracteristica="manchas_blancas_rostro"), AnimalFact(caracteristica="vive_en_andes"))
    def oso_anteojos(self):
        self.identified_species = "Oso de Anteojos"
        self.log("Especie Alcanzada: Oso de Anteojos")

    @Rule(AnimalFact(clase="Mamífero"), AnimalFact(dieta="Herbívoro"),
          AnimalFact(caracteristica="roedor_gigante"), AnimalFact(caracteristica="semiacuatico"), AnimalFact(caracteristica="vive_en_llanuras"))
    def chiguiro(self):
        self.identified_species = "Chigüiro"
        self.log("Especie Alcanzada: Chigüiro")

    @Rule(AnimalFact(clase="Mamífero"), AnimalFact(dieta="Herbívoro"),
          AnimalFact(caracteristica="cuello_largo"), AnimalFact(caracteristica="patas_largas"), AnimalFact(caracteristica="vive_en_sabana_africana"))
    def jirafa(self):
        self.identified_species = "Jirafa"
        self.log("Especie Alcanzada: Jirafa")

    @Rule(AnimalFact(clase="Mamífero"), AnimalFact(dieta="Herbívoro"),
          AnimalFact(caracteristica="rayas_blancas_negras"), AnimalFact(caracteristica="equino"), AnimalFact(caracteristica="vive_en_sabana_africana"))
    def cebra(self):
        self.identified_species = "Cebra"
        self.log("Especie Alcanzada: Cebra")

    @Rule(AnimalFact(clase="Mamífero"), AnimalFact(dieta="Herbívoro"),
          AnimalFact(caracteristica="trompa_larga"), AnimalFact(caracteristica="orejas_grandes"), AnimalFact(caracteristica="colmillos_marfil"))
    def elefante(self):
        self.identified_species = "Elefante"
        self.log("Especie Alcanzada: Elefante")

    @Rule(AnimalFact(clase="Mamífero"), AnimalFact(dieta="Carnívoro"),
          AnimalFact(caracteristica="melena_machos"), AnimalFact(caracteristica="felino_grande"), AnimalFact(caracteristica="vive_en_sabana_africana"))
    def leon(self):
        self.identified_species = "León"
        self.log("Especie Alcanzada: León")

    @Rule(AnimalFact(clase="Mamífero"), AnimalFact(dieta="Herbívoro"),
          AnimalFact(caracteristica="domestico"), AnimalFact(caracteristica="produce_leche"), AnimalFact(caracteristica="rumiante"), AnimalFact(caracteristica="cuernos"))
    def vaca(self):
        self.identified_species = "Vaca"
        self.log("Especie Alcanzada: Vaca")

    @Rule(AnimalFact(clase="Mamífero"), AnimalFact(dieta="Omnívoro"),
          AnimalFact(caracteristica="domestico"), AnimalFact(caracteristica="ladra"), AnimalFact(caracteristica="mascota"))
    def perro(self):
        self.identified_species = "Perro"
        self.log("Especie Alcanzada: Perro")

    @Rule(AnimalFact(clase="Mamífero"), AnimalFact(dieta="Carnívoro"),
          AnimalFact(caracteristica="domestico"), AnimalFact(caracteristica="maulla"), AnimalFact(caracteristica="mascota"), AnimalFact(caracteristica="felino_pequeno"))
    def gato(self):
        self.identified_species = "Gato"
        self.log("Especie Alcanzada: Gato")

    @Rule(AnimalFact(clase="Mamífero"), AnimalFact(dieta="Insectívoro"),
          AnimalFact(caracteristica="vuela"), AnimalFact(caracteristica="nocturno"), AnimalFact(caracteristica="ecolocalizacion"))
    def murcielago(self):
        self.identified_species = "Murciélago"
        self.log("Especie Alcanzada: Murciélago")

    # Aves
    @Rule(AnimalFact(clase="Ave"), AnimalFact(dieta="Carroñero"),
          AnimalFact(caracteristica="enorme_envergadura"), AnimalFact(caracteristica="collar_blanco"), AnimalFact(caracteristica="vive_en_andes"))
    def condor(self):
        self.identified_species = "Cóndor"
        self.log("Especie Alcanzada: Cóndor")

    @Rule(AnimalFact(clase="Ave"), AnimalFact(dieta="Carnívoro"),
          AnimalFact(caracteristica="rapaz"), AnimalFact(caracteristica="garras_enormes"), AnimalFact(caracteristica="vive_en_selva"))
    def aguila_arpia(self):
        self.identified_species = "Águila Arpía"
        self.log("Especie Alcanzada: Águila Arpía")

    @Rule(AnimalFact(clase="Ave"), AnimalFact(dieta="Frugívoro"),
          AnimalFact(caracteristica="plumaje_colorido"), AnimalFact(caracteristica="pico_fuerte"), AnimalFact(caracteristica="vive_en_selva"))
    def guacamaya(self):
        self.identified_species = "Guacamaya"
        self.log("Especie Alcanzada: Guacamaya")

    @Rule(AnimalFact(clase="Ave"), AnimalFact(dieta="Carnívoro"),
          AnimalFact(caracteristica="no_vuela"), AnimalFact(caracteristica="vuela_bajo_agua"), AnimalFact(caracteristica="vive_en_clima_frio"))
    def pinguino(self):
        self.identified_species = "Pingüino"
        self.log("Especie Alcanzada: Pingüino")

    @Rule(AnimalFact(clase="Ave"), AnimalFact(dieta="Omnívoro"),
          AnimalFact(caracteristica="corredora_veloz"), AnimalFact(caracteristica="cuello_largo"), AnimalFact(caracteristica="ave_gigante"))
    def avestruz(self):
        self.identified_species = "Avestruz"
        self.log("Especie Alcanzada: Avestruz")

    @Rule(AnimalFact(clase="Ave"), AnimalFact(dieta="Omnívoro"),
          AnimalFact(caracteristica="domestico"), AnimalFact(caracteristica="pone_huevos_consumo"), AnimalFact(caracteristica="vuelo_corto"))
    def gallina(self):
        self.identified_species = "Gallina"
        self.log("Especie Alcanzada: Gallina")

    # Reptiles
    @Rule(AnimalFact(clase="Reptil"), AnimalFact(dieta="Carnívoro"),
          AnimalFact(caracteristica="semiacuatico"), AnimalFact(caracteristica="escamas_duras"), AnimalFact(caracteristica="mandibula_poderosa"))
    def cocodrilo(self):
        self.identified_species = "Cocodrilo"
        self.log("Especie Alcanzada: Cocodrilo")

    @Rule(AnimalFact(clase="Reptil"), AnimalFact(dieta="Carnívoro"),
          AnimalFact(caracteristica="serpiente"), AnimalFact(caracteristica="constrictora"), AnimalFact(caracteristica="vive_en_amazonas"))
    def anaconda(self):
        self.identified_species = "Anaconda"
        self.log("Especie Alcanzada: Anaconda")

    @Rule(AnimalFact(clase="Reptil"), AnimalFact(dieta="Herbívoro"),
          AnimalFact(caracteristica="cresta_dorsal"), AnimalFact(caracteristica="trepadora"), AnimalFact(caracteristica="cola_larga"))
    def iguana(self):
        self.identified_species = "Iguana"
        self.log("Especie Alcanzada: Iguana")

    @Rule(AnimalFact(clase="Reptil"), AnimalFact(dieta="Omnívoro"),
          AnimalFact(caracteristica="caparazon"), AnimalFact(caracteristica="aletas"), AnimalFact(caracteristica="vive_en_oceano"))
    def tortuga_marina(self):
        self.identified_species = "Tortuga Marina"
        self.log("Especie Alcanzada: Tortuga Marina")

    # Anfibios
    @Rule(AnimalFact(clase="Anfibio"), AnimalFact(dieta="Insectívoro"),
          AnimalFact(caracteristica="piel_venenosa"), AnimalFact(caracteristica="amarillo_brillante"), AnimalFact(caracteristica="muy_pequena"))
    def rana_dorada(self):
        self.identified_species = "Rana Dorada"
        self.log("Especie Alcanzada: Rana Dorada")

    @Rule(AnimalFact(clase="Anfibio"), AnimalFact(dieta="Insectívoro"),
          AnimalFact(caracteristica="piel_rugosa"), AnimalFact(caracteristica="terrestre"), AnimalFact(caracteristica="salta"))
    def sapo_comun(self):
        self.identified_species = "Sapo Común"
        self.log("Especie Alcanzada: Sapo Común")

    # Peces
    @Rule(AnimalFact(clase="Pez"), AnimalFact(dieta="Carnívoro"),
          AnimalFact(caracteristica="agua_dulce"), AnimalFact(caracteristica="escamas_gigantes"), AnimalFact(caracteristica="respira_aire"))
    def pirarucu(self):
        self.identified_species = "Pirarucú"
        self.log("Especie Alcanzada: Pirarucú")

    @Rule(AnimalFact(clase="Pez"), AnimalFact(dieta="Carnívoro"),
          AnimalFact(caracteristica="escualo"), AnimalFact(caracteristica="dientes_aserrados"), AnimalFact(caracteristica="depredador_marino"))
    def tiburon_blanco(self):
        self.identified_species = "Tiburón Blanco"
        self.log("Especie Alcanzada: Tiburón Blanco")
