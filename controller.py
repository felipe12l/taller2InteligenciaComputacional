from knowledge_base import AnimalExpertEngine, AnimalFact
from species_data import SPECIES_DATA

class ExpertController:
    def __init__(self):
        self.engine = AnimalExpertEngine()
        self.reset_state()

    def reset_state(self):
        """Reinicia la selección del usuario y la lista de especies posibles."""
        # Se almacenan las selecciones del usuario:
        # clases_sel: set, dieta_sel: set, caracteristicas_sel: set
        self.clase_sel = set()
        self.dieta_sel = set()
        self.caracteristicas_sel = set()

    def get_posibles_especies(self):
        """Retorna las especies que aún cumplen con todas las selecciones actuales."""
        posibles = []
        for sp in SPECIES_DATA:
            valido = True
            if self.clase_sel and sp["clase"] not in self.clase_sel:
                valido = False
            if self.dieta_sel and sp["dieta"] not in self.dieta_sel:
                valido = False
            
            # Verificar que la especie contenga TODAS las características seleccionadas
            if self.caracteristicas_sel:
                for c in self.caracteristicas_sel:
                    if c not in sp["caracteristicas"]:
                        valido = False
                        break
            if valido:
                posibles.append(sp)
        return posibles

    def on_selection_changed(self, clase_sel, dieta_sel, caracteristicas_sel):
        """
        Recibe el listado actual de checkboxes marcados.
        Retorna qué otros checkboxes deberían estar habilitados.
        """
        self.clase_sel = set(clase_sel)
        self.dieta_sel = set(dieta_sel)
        self.caracteristicas_sel = set(caracteristicas_sel)

        posibles = self.get_posibles_especies()
        
        clases_validas = set()
        dietas_validas = set()
        caracteristicas_validas = set()

        for sp in posibles:
            clases_validas.add(sp["clase"])
            dietas_validas.add(sp["dieta"])
            for c in sp["caracteristicas"]:
                caracteristicas_validas.add(c)

        return clases_validas, dietas_validas, caracteristicas_validas

    def identify_animal(self, clase_sel, dieta_sel, caracteristicas_sel):
        """Inicia el motor de inferencia con los datos recolectados y retorna los resultados."""
        self.engine.reset()
        self.engine.reasoning_log.clear()
        self.engine.identified_species = None

        # Preparar hechos a partir de la selección
        # Para hacer coincidir con rules, usaremos aserciones primitivas:
        
        # Mapeo de clase a sus hechos deducibles de nivel 1 (si queremos simular deducibilidad)
        # O podemos inyectar las aserciones directamente si selecciono "Clase X"
        for clase in clase_sel:
            self.engine.declare(AnimalFact(clase=clase))
            # Tambien inyectamos sus disparadores por si no marcó la clase explícitamente y queremos rastrearlo
            if clase == "Mamífero": self.engine.declare(AnimalFact(tiene_pelo=True))
            if clase == "Ave": self.engine.declare(AnimalFact(tiene_plumas=True))
            if clase == "Reptil": self.engine.declare(AnimalFact(tiene_escamas_reptil=True))
            if clase == "Anfibio": self.engine.declare(AnimalFact(tiene_piel_humeda=True))
            if clase == "Pez": self.engine.declare(AnimalFact(tiene_branquias=True))

        for dieta in dieta_sel:
            self.engine.declare(AnimalFact(dieta=dieta))
            if dieta == "Carnívoro": self.engine.declare(AnimalFact(come_carne=True))
            if dieta == "Herbívoro": self.engine.declare(AnimalFact(come_plantas=True))
            if dieta == "Omnívoro": self.engine.declare(AnimalFact(come_de_todo=True))
            if dieta == "Insectívoro": self.engine.declare(AnimalFact(come_insectos=True))
            if dieta == "Carroñero": self.engine.declare(AnimalFact(come_cadaveres=True))
            if dieta == "Frugívoro": self.engine.declare(AnimalFact(come_frutas=True))

        for carac in caracteristicas_sel:
            self.engine.declare(AnimalFact(caracteristica=carac))

        # Realizar el encadenamiento hacia adelante
        self.engine.run()

        # Determinar resultado
        especie = self.engine.identified_species
        log = "\n".join(self.engine.reasoning_log)

        if not especie:
            # Inferencia incompleta
            posibles = self.get_posibles_especies()
            if len(posibles) > 0:
                especies_nombres = ", ".join([p["nombre"] for p in posibles])
                log += f"\n\nInferencia Incompleta. Especiales posibles ({len(posibles)}):\n{especies_nombres}"
            else:
                log += "\n\nInferencia Fallida. Ningún animal de la base de conocimiento coincide."
        
        return especie, log
