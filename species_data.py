SPECIES_DATA = [
    {
        "nombre": "Jaguar",
        "clase": "Mamífero",
        "dieta": "Carnívoro",
        "caracteristicas": ["piel_manchas_rosetas", "vive_en_selva", "felino_grande"]
    },
    {
        "nombre": "Oso de Anteojos",
        "clase": "Mamífero",
        "dieta": "Omnívoro",
        "caracteristicas": ["pelaje_negro", "manchas_blancas_rostro", "vive_en_andes"]
    },
    {
        "nombre": "Chigüiro",
        "clase": "Mamífero",
        "dieta": "Herbívoro",
        "caracteristicas": ["roedor_gigante", "semiacuatico", "vive_en_llanuras"]
    },
    {
        "nombre": "Jirafa",
        "clase": "Mamífero",
        "dieta": "Herbívoro",
        "caracteristicas": ["cuello_largo", "patas_largas", "vive_en_sabana_africana"]
    },
    {
        "nombre": "Cebra",
        "clase": "Mamífero",
        "dieta": "Herbívoro",
        "caracteristicas": ["rayas_blancas_negras", "equino", "vive_en_sabana_africana"]
    },
    {
        "nombre": "Elefante",
        "clase": "Mamífero",
        "dieta": "Herbívoro",
        "caracteristicas": ["trompa_larga", "orejas_grandes", "colmillos_marfil"]
    },
    {
        "nombre": "León",
        "clase": "Mamífero",
        "dieta": "Carnívoro",
        "caracteristicas": ["melena_machos", "felino_grande", "vive_en_sabana_africana"]
    },
    {
        "nombre": "Vaca",
        "clase": "Mamífero",
        "dieta": "Herbívoro",
        "caracteristicas": ["domestico", "produce_leche", "rumiante", "cuernos"]
    },
    {
        "nombre": "Perro",
        "clase": "Mamífero",
        "dieta": "Omnívoro",
        "caracteristicas": ["domestico", "ladra", "mascota"]
    },
    {
        "nombre": "Gato",
        "clase": "Mamífero",
        "dieta": "Carnívoro",
        "caracteristicas": ["domestico", "maulla", "mascota", "felino_pequeno"]
    },
    {
        "nombre": "Murciélago",
        "clase": "Mamífero",
        "dieta": "Insectívoro",
        "caracteristicas": ["vuela", "nocturno", "ecolocalizacion"]
    },
    {
        "nombre": "Cóndor",
        "clase": "Ave",
        "dieta": "Carroñero",
        "caracteristicas": ["enorme_envergadura", "collar_blanco", "vive_en_andes"]
    },
    {
        "nombre": "Águila Arpía",
        "clase": "Ave",
        "dieta": "Carnívoro",
        "caracteristicas": ["rapaz", "garras_enormes", "vive_en_selva"]
    },
    {
        "nombre": "Guacamaya",
        "clase": "Ave",
        "dieta": "Frugívoro",
        "caracteristicas": ["plumaje_colorido", "pico_fuerte", "vive_en_selva"]
    },
    {
        "nombre": "Pingüino",
        "clase": "Ave",
        "dieta": "Carnívoro",
        "caracteristicas": ["no_vuela", "vuela_bajo_agua", "vive_en_clima_frio"]
    },
    {
        "nombre": "Avestruz",
        "clase": "Ave",
        "dieta": "Omnívoro",
        "caracteristicas": ["corredora_veloz", "cuello_largo", "ave_gigante"]
    },
    {
        "nombre": "Gallina",
        "clase": "Ave",
        "dieta": "Omnívoro",
        "caracteristicas": ["domestico", "pone_huevos_consumo", "vuelo_corto"]
    },
    {
        "nombre": "Cocodrilo",
        "clase": "Reptil",
        "dieta": "Carnívoro",
        "caracteristicas": ["semiacuatico", "escamas_duras", "mandibula_poderosa"]
    },
    {
        "nombre": "Anaconda",
        "clase": "Reptil",
        "dieta": "Carnívoro",
        "caracteristicas": ["serpiente", "constrictora", "vive_en_amazonas"]
    },
    {
        "nombre": "Iguana",
        "clase": "Reptil",
        "dieta": "Herbívoro",
        "caracteristicas": ["cresta_dorsal", "trepadora", "cola_larga"]
    },
    {
        "nombre": "Tortuga Marina",
        "clase": "Reptil",
        "dieta": "Omnívoro",
        "caracteristicas": ["caparazon", "aletas", "vive_en_oceano"]
    },
    {
        "nombre": "Rana Dorada",
        "clase": "Anfibio",
        "dieta": "Insectívoro",
        "caracteristicas": ["piel_venenosa", "amarillo_brillante", "muy_pequena"]
    },
    {
        "nombre": "Sapo Común",
        "clase": "Anfibio",
        "dieta": "Insectívoro",
        "caracteristicas": ["piel_rugosa", "terrestre", "salta"]
    },
    {
        "nombre": "Pirarucú",
        "clase": "Pez",
        "dieta": "Carnívoro",
        "caracteristicas": ["agua_dulce", "escamas_gigantes", "respira_aire"]
    },
    {
        "nombre": "Tiburón Blanco",
        "clase": "Pez",
        "dieta": "Carnívoro",
        "caracteristicas": ["escualo", "dientes_aserrados", "depredador_marino"]
    }
]

# Diccionarios de mapeo para hacerlo amigable en la UI
CATEGORIAS_UI = {
    "clase": {
        "Mamífero": "Es Mamífero (tiene pelo/glándulas mamarias)",
        "Ave": "Es Ave (tiene plumas)",
        "Reptil": "Es Reptil (tiene escamas/sangre fría)",
        "Anfibio": "Es Anfibio (piel húmeda/metamorfosis)",
        "Pez": "Es Pez (tiene branquias/aletas)"
    },
    "dieta": {
        "Carnívoro": "Come carne (Carnívoro)",
        "Herbívoro": "Come plantas (Herbívoro)",
        "Omnívoro": "Come de todo (Omnívoro)",
        "Insectívoro": "Come insectos (Insectívoro)",
        "Carroñero": "Come animales muertos (Carroñero)",
        "Frugívoro": "Come frutas (Frugívoro)"
    },
    "caracteristicas": {
        "piel_manchas_rosetas": "Pelaje con manchas en roseta",
        "vive_en_selva": "Hábitat: Selvas húmedas o bosques",
        "felino_grande": "Es un felino de gran tamaño",
        "pelaje_negro": "Pelaje mayormente negro",
        "manchas_blancas_rostro": "Manchas o anillos claros en el rostro",
        "vive_en_andes": "Hábitat: Cordillera de los Andes",
        "roedor_gigante": "Es el roedor más grande",
        "semiacuatico": "Pasa mucho tiempo en el agua",
        "vive_en_llanuras": "Hábitat: Llanuras y sabanas sudamericanas",
        "cuello_largo": "Cuello extremadamente largo",
        "patas_largas": "Patas muy largas",
        "vive_en_sabana_africana": "Hábitat: Sabana Africana",
        "rayas_blancas_negras": "Pelaje con patrón de rayas blancas y negras",
        "equino": "Forma similar a un caballo",
        "trompa_larga": "Posee una trompa larga prensil",
        "orejas_grandes": "Orejas muy grandes",
        "colmillos_marfil": "Tiene colmillos largos (marfil)",
        "melena_machos": "Los machos tienen una gran melena",
        "domestico": "Animal doméstico/de granja",
        "produce_leche": "Utilizado comercialmente por su leche",
        "rumiante": "Sistema digestivo rumiante",
        "cuernos": "Posee cuernos",
        "ladra": "Emite ladridos",
        "mascota": "Popular como mascota principal de hogar",
        "maulla": "Emite maullidos",
        "felino_pequeno": "Es un felino de tamaño pequeño",
        "vuela": "Capacidad de volar activo",
        "nocturno": "Hábitos estrictamente nocturnos",
        "ecolocalizacion": "Utiliza ecolocalización para guiarse",
        "enorme_envergadura": "Alas con una enorme envergadura (más de 3m)",
        "collar_blanco": "Posee un collar de plumas blancas",
        "rapaz": "Ave rapaz con pico ganchudo",
        "garras_enormes": "Garras muy fuertes y desarrolladas",
        "plumaje_colorido": "Plumas de colores muy brillantes (rojo, azul, amarillo)",
        "pico_fuerte": "Pico muy robusto para romper semillas",
        "no_vuela": "Sus alas no le permiten volar por el aire",
        "vuela_bajo_agua": "Nada ágilmente (vuelo submarino)",
        "vive_en_clima_frio": "Hábitat: Climas helados o corrientes oceánicas frías",
        "corredora_veloz": "Capaz de correr a gran velocidad (ave)",
        "ave_gigante": "Es el ave más grande del mundo",
        "pone_huevos_consumo": "Sus huevos son muy consumidos por humanos",
        "vuelo_corto": "Solo puede realizar vuelos cortos o planear un poco",
        "escamas_duras": "Posee placas dorsales o escamas muy duras",
        "mandibula_poderosa": "Mandíbula alargada con mucha fuerza",
        "serpiente": "Reptil sin patas",
        "constrictora": "Mata a sus presas por estrangulamiento",
        "vive_en_amazonas": "Hábitat: Cuenca del río Amazonas",
        "cresta_dorsal": "Cresta de espinas en la espalda",
        "trepadora": "Excelente trepadora de árboles",
        "cola_larga": "Cola muy larga y usada como látigo",
        "caparazon": "Cuerpo cubierto por un gran caparazón",
        "aletas": "Patas adaptadas en forma de aletas",
        "vive_en_oceano": "Hábitat: Océanos y mares",
        "piel_venenosa": "Piel que secreta sustancias tóxicas",
        "amarillo_brillante": "Coloración aposemática amarilla",
        "muy_pequena": "De tamaño muy reducido (pocos centímetros)",
        "piel_rugosa": "Piel seca o llena de verrugas",
        "terrestre": "Pasa la mayor parte de etapa adulta en la tierra",
        "salta": "Se desplaza mayormente dando saltos",
        "agua_dulce": "Vive exclusivamente en agua dulce",
        "escamas_gigantes": "Posee escamas de gran tamaño e inusuales",
        "respira_aire": "Obligado a subir a la superficie para respirar aire",
        "escualo": "Forma típica de tiburón",
        "dientes_aserrados": "Varias hileras de dientes triangulares afilados",
        "depredador_marino": "Máximo depredador de los océanos"
    }
}
