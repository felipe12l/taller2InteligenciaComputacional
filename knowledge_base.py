from py_rete.common import Has, Rule, WME
from py_rete.network import Network


class AnimalFact(dict):
    """Representación simple de hechos con API compatible con el controlador."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class AnimalExpertEngine:
    def __init__(self):
        self.reasoning_log = []
        self.identified_species = None
        self.reset()

    def reset(self):
        self.network = Network()
        self.reasoning_log = []
        self.identified_species = None
        self._facts = set()
        self._productions = []
        self._fired_signatures = set()
        self._build_productions()

    def log(self, text):
        self.reasoning_log.append(text)

    def declare(self, fact):
        for attribute, value in fact.items():
            self._assert_fact("animal", attribute, value)

    def run(self):
        made_inference = True
        while made_inference:
            made_inference = False
            for production in self._productions:
                pnode = production["pnode"]
                for token in pnode.items:
                    signature = (
                        production["name"],
                        tuple((w.identifier, w.attribute, w.value) for w in token.wmes),
                    )
                    if signature in self._fired_signatures:
                        continue

                    self._fired_signatures.add(signature)

                    if production.get("log"):
                        self.log(production["log"])

                    inferred = production.get("infer", [])
                    for identifier, attribute, value in inferred:
                        added = self._assert_fact(identifier, attribute, value)
                        if added:
                            made_inference = True

                    species = production.get("species")
                    if species and self.identified_species is None:
                        self.identified_species = species

    def _assert_fact(self, identifier, attribute, value):
        value = self._rete_value(value)
        key = (identifier, attribute, value)
        if key in self._facts:
            return False
        self._facts.add(key)
        self.network.add_wme(WME(identifier, attribute, value))
        return True

    def _add_rule(self, name, conditions, infer=None, log=None, species=None):
        lhs = Rule(
            *[
                Has(identifier, attribute, self._rete_value(value))
                for identifier, attribute, value in conditions
            ]
        )
        pnode = self.network.add_production(lhs, name=name)
        self._productions.append(
            {
                "name": name,
                "pnode": pnode,
                "infer": infer or [],
                "log": log,
                "species": species,
            }
        )

    @staticmethod
    def _rete_value(value):
        return str(value)

    def _build_productions(self):
        self._add_rule(
            "es_mamifero",
            [("animal", "tiene_pelo", True)],
            infer=[("animal", "clase", "Mamífero")],
            log="Deducción: Es Mamífero (tiene pelo/glándulas mamarias).",
        )
        self._add_rule(
            "es_ave",
            [("animal", "tiene_plumas", True)],
            infer=[("animal", "clase", "Ave")],
            log="Deducción: Es Ave (tiene plumas).",
        )
        self._add_rule(
            "es_reptil",
            [("animal", "tiene_escamas_reptil", True)],
            infer=[("animal", "clase", "Reptil")],
            log="Deducción: Es Reptil.",
        )
        self._add_rule(
            "es_anfibio",
            [("animal", "tiene_piel_humeda", True)],
            infer=[("animal", "clase", "Anfibio")],
            log="Deducción: Es Anfibio.",
        )
        self._add_rule(
            "es_pez",
            [("animal", "tiene_branquias", True)],
            infer=[("animal", "clase", "Pez")],
            log="Deducción: Es Pez.",
        )
        self._add_rule(
            "es_carnivoro",
            [("animal", "come_carne", True)],
            infer=[("animal", "dieta", "Carnívoro")],
            log="Deducción: Es Carnívoro (come carne).",
        )
        self._add_rule(
            "es_herbivoro",
            [("animal", "come_plantas", True)],
            infer=[("animal", "dieta", "Herbívoro")],
            log="Deducción: Es Herbívoro (come plantas).",
        )
        self._add_rule(
            "es_omnivoro",
            [("animal", "come_de_todo", True)],
            infer=[("animal", "dieta", "Omnívoro")],
            log="Deducción: Es Omnívoro (come de todo).",
        )
        self._add_rule(
            "es_insectivoro",
            [("animal", "come_insectos", True)],
            infer=[("animal", "dieta", "Insectívoro")],
            log="Deducción: Es Insectívoro (come insectos).",
        )
        self._add_rule(
            "es_carronero",
            [("animal", "come_cadaveres", True)],
            infer=[("animal", "dieta", "Carroñero")],
            log="Deducción: Es Carroñero (come animales muertos).",
        )
        self._add_rule(
            "es_frugivoro",
            [("animal", "come_frutas", True)],
            infer=[("animal", "dieta", "Frugívoro")],
            log="Deducción: Es Frugívoro (come frutas).",
        )

        self._add_species_rule("jaguar", "Jaguar", "Mamífero", "Carnívoro", ["piel_manchas_rosetas", "vive_en_selva", "felino_grande"])
        self._add_species_rule("oso_anteojos", "Oso de Anteojos", "Mamífero", "Omnívoro", ["pelaje_negro", "manchas_blancas_rostro", "vive_en_andes"])
        self._add_species_rule("chiguiro", "Chigüiro", "Mamífero", "Herbívoro", ["roedor_gigante", "semiacuatico", "vive_en_llanuras"])
        self._add_species_rule("jirafa", "Jirafa", "Mamífero", "Herbívoro", ["cuello_largo", "patas_largas", "vive_en_sabana_africana"])
        self._add_species_rule("cebra", "Cebra", "Mamífero", "Herbívoro", ["rayas_blancas_negras", "equino", "vive_en_sabana_africana"])
        self._add_species_rule("elefante", "Elefante", "Mamífero", "Herbívoro", ["trompa_larga", "orejas_grandes", "colmillos_marfil"])
        self._add_species_rule("leon", "León", "Mamífero", "Carnívoro", ["melena_machos", "felino_grande", "vive_en_sabana_africana"])
        self._add_species_rule("vaca", "Vaca", "Mamífero", "Herbívoro", ["domestico", "produce_leche", "rumiante", "cuernos"])
        self._add_species_rule("perro", "Perro", "Mamífero", "Omnívoro", ["domestico", "ladra", "mascota"])
        self._add_species_rule("gato", "Gato", "Mamífero", "Carnívoro", ["domestico", "maulla", "mascota", "felino_pequeno"])
        self._add_species_rule("murcielago", "Murciélago", "Mamífero", "Insectívoro", ["vuela", "nocturno", "ecolocalizacion"])
        self._add_species_rule("condor", "Cóndor", "Ave", "Carroñero", ["enorme_envergadura", "collar_blanco", "vive_en_andes"])
        self._add_species_rule("aguila_arpia", "Águila Arpía", "Ave", "Carnívoro", ["rapaz", "garras_enormes", "vive_en_selva"])
        self._add_species_rule("guacamaya", "Guacamaya", "Ave", "Frugívoro", ["plumaje_colorido", "pico_fuerte", "vive_en_selva"])
        self._add_species_rule("pinguino", "Pingüino", "Ave", "Carnívoro", ["no_vuela", "vuela_bajo_agua", "vive_en_clima_frio"])
        self._add_species_rule("avestruz", "Avestruz", "Ave", "Omnívoro", ["corredora_veloz", "cuello_largo", "ave_gigante"])
        self._add_species_rule("gallina", "Gallina", "Ave", "Omnívoro", ["domestico", "pone_huevos_consumo", "vuelo_corto"])
        self._add_species_rule("cocodrilo", "Cocodrilo", "Reptil", "Carnívoro", ["semiacuatico", "escamas_duras", "mandibula_poderosa"])
        self._add_species_rule("anaconda", "Anaconda", "Reptil", "Carnívoro", ["serpiente", "constrictora", "vive_en_amazonas"])
        self._add_species_rule("iguana", "Iguana", "Reptil", "Herbívoro", ["cresta_dorsal", "trepadora", "cola_larga"])
        self._add_species_rule("tortuga_marina", "Tortuga Marina", "Reptil", "Omnívoro", ["caparazon", "aletas", "vive_en_oceano"])
        self._add_species_rule("rana_dorada", "Rana Dorada", "Anfibio", "Insectívoro", ["piel_venenosa", "amarillo_brillante", "muy_pequena"])
        self._add_species_rule("sapo_comun", "Sapo Común", "Anfibio", "Insectívoro", ["piel_rugosa", "terrestre", "salta"])
        self._add_species_rule("pirarucu", "Pirarucú", "Pez", "Carnívoro", ["agua_dulce", "escamas_gigantes", "respira_aire"])
        self._add_species_rule("tiburon_blanco", "Tiburón Blanco", "Pez", "Carnívoro", ["escualo", "dientes_aserrados", "depredador_marino"])

    def _add_species_rule(self, rule_name, species_name, clase, dieta, caracteristicas):
        conditions = [
            ("animal", "clase", clase),
            ("animal", "dieta", dieta),
            *[("animal", "caracteristica", c) for c in caracteristicas],
        ]
        self._add_rule(
            rule_name,
            conditions,
            log=f"Especie Alcanzada: {species_name}",
            species=species_name,
        )
