from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QCheckBox, QPushButton, QTextEdit, QScrollArea, QGroupBox, QGridLayout)
from PyQt6.QtCore import Qt
from species_data import CATEGORIAS_UI
from controller import ExpertController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = ExpertController()
        
        self.setWindowTitle("Sistema Experto Identificador de Animales")
        self.setMinimumSize(900, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f4f8;
            }
            QGroupBox {
                font-weight: bold;
                border: 1px solid #dcdcdc;
                border-radius: 5px;
                margin-top: 10px;
                background-color: #ffffff;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 5px;
                color: #2c3e50;
            }
            QLabel {
                font-size: 14px;
                color: #34495e;
            }
            QCheckBox {
                font-size: 13px;
                color: #2c3e50;
                padding: 3px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
            }
            QCheckBox:disabled {
                color: #a0a0a0;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QTextEdit {
                background-color: #ffffff;
                color: #2c3e50;
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                font-size: 14px;
                padding: 8px;
            }
        """)

        self.checkboxes_clase = {}
        self.checkboxes_dieta = {}
        self.checkboxes_caracteristicas = {}

        self._init_ui()
        self._update_ui_state()

    def _init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        
        # Panel Izquierdo: Formularios
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(10, 10, 10, 10)
        
        title_lbl = QLabel("<h3>Selecciona las características que conoces:</h3>")
        left_layout.addWidget(title_lbl)

        # Scroll para características
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")
        
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        
        # Grupo Clase
        group_clase = QGroupBox("Clase / Taxonomía Básica")
        layout_clase = QGridLayout()
        row, col = 0, 0
        for key, val in CATEGORIAS_UI["clase"].items():
            cb = QCheckBox(val)
            cb.setProperty("internal_key", key)
            cb.clicked.connect(self._on_checkbox_clicked)
            self.checkboxes_clase[key] = cb
            layout_clase.addWidget(cb, row, col)
            col += 1
            if col > 1:
                col = 0
                row += 1
        group_clase.setLayout(layout_clase)
        scroll_layout.addWidget(group_clase)

        # Grupo Dieta
        group_dieta = QGroupBox("Alimentación / Dieta")
        layout_dieta = QGridLayout()
        row, col = 0, 0
        for key, val in CATEGORIAS_UI["dieta"].items():
            cb = QCheckBox(val)
            cb.setProperty("internal_key", key)
            cb.clicked.connect(self._on_checkbox_clicked)
            self.checkboxes_dieta[key] = cb
            layout_dieta.addWidget(cb, row, col)
            col += 1
            if col > 1:
                col = 0
                row += 1
        group_dieta.setLayout(layout_dieta)
        scroll_layout.addWidget(group_dieta)

        # Grupo Características
        group_carac = QGroupBox("Hábitat y Morfología")
        layout_carac = QGridLayout()
        row, col = 0, 0
        for key, val in CATEGORIAS_UI["caracteristicas"].items():
            cb = QCheckBox(val)
            cb.setProperty("internal_key", key)
            cb.clicked.connect(self._on_checkbox_clicked)
            self.checkboxes_caracteristicas[key] = cb
            layout_carac.addWidget(cb, row, col)
            col += 1
            if col > 1:
                col = 0
                row += 1
        group_carac.setLayout(layout_carac)
        scroll_layout.addWidget(group_carac)

        scroll_layout.addStretch()
        scroll.setWidget(scroll_widget)
        
        left_layout.addWidget(scroll)

        # Botones de Acción
        btn_layout = QHBoxLayout()
        self.btn_identificar = QPushButton("Identificar Especie")
        self.btn_identificar.clicked.connect(self.identificar)
        
        self.btn_reset = QPushButton("Reiniciar")
        self.btn_reset.setStyleSheet("QPushButton { background-color: #e74c3c; } QPushButton:hover { background-color: #c0392b; }")
        self.btn_reset.clicked.connect(self.reset_form)
        
        btn_layout.addWidget(self.btn_reset)
        btn_layout.addWidget(self.btn_identificar)
        left_layout.addLayout(btn_layout)

        # Panel Derecho: Resultados y Log
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        result_title = QLabel("<h3>Log de Razonamiento (Motor Rete)</h3>")
        right_layout.addWidget(result_title)

        self.text_log = QTextEdit()
        self.text_log.setReadOnly(True)
        right_layout.addWidget(self.text_log)

        main_layout.addWidget(left_panel, 6)
        main_layout.addWidget(right_panel, 4)

    def _get_current_selections(self):
        sel_clase = [key for key, cb in self.checkboxes_clase.items() if cb.isChecked()]
        sel_dieta = [key for key, cb in self.checkboxes_dieta.items() if cb.isChecked()]
        sel_carac = [key for key, cb in self.checkboxes_caracteristicas.items() if cb.isChecked()]
        return sel_clase, sel_dieta, sel_carac

    def _on_checkbox_clicked(self):
        """Llamado cuando el usuario hace clic. Previene hacer clic en opciones excluyentes directas y reactiva UI."""
        # Se requiere que Clase y Dieta sean únicas si ya hay alguna seleccionada (por simplicidad, deseleccionamos otras del mismo grupo si es un radio button logico)
        sender = self.sender()
        if sender.isChecked():
            key = sender.property("internal_key")
            # Si es clase y marcó una, desmarcar las demas
            if key in CATEGORIAS_UI["clase"]:
                for cb in self.checkboxes_clase.values():
                    if cb != sender: cb.setChecked(False)
            if key in CATEGORIAS_UI["dieta"]:
                for cb in self.checkboxes_dieta.values():
                    if cb != sender: cb.setChecked(False)
        
        self._update_ui_state()

    def _update_ui_state(self):
        sel_clase, sel_dieta, sel_carac = self._get_current_selections()
        v_clase, v_dieta, v_carac = self.controller.on_selection_changed(sel_clase, sel_dieta, sel_carac)

        # Las válidas son las que pueden existir junto con lo ya seleccionado
        # Actualizamos enabled state si no están seleccionados
        for k, cb in self.checkboxes_clase.items():
            if not cb.isChecked():
                cb.setEnabled(k in v_clase)
                
        for k, cb in self.checkboxes_dieta.items():
            if not cb.isChecked():
                cb.setEnabled(k in v_dieta)
                
        for k, cb in self.checkboxes_caracteristicas.items():
            if not cb.isChecked():
                cb.setEnabled(k in v_carac)

    def reset_form(self):
        for cb_dict in [self.checkboxes_clase, self.checkboxes_dieta, self.checkboxes_caracteristicas]:
            for cb in cb_dict.values():
                cb.setChecked(False)
                cb.setEnabled(True)
        self.text_log.clear()
        self.controller.reset_state()
        self._update_ui_state()

    def identificar(self):
        sel_clase, sel_dieta, sel_carac = self._get_current_selections()
        
        self.text_log.append("--- INICIANDO INFERENCIA ---")
        especie, log = self.controller.identify_animal(sel_clase, sel_dieta, sel_carac)
        
        self.text_log.append(log)
        
        if especie:
            self.text_log.append(f"\n<b><font color='green' size='5'>>> Especie identificada: {especie} <<</font></b>")
            
        self.text_log.append("--- FIN ---")
        self.text_log.verticalScrollBar().setValue(self.text_log.verticalScrollBar().maximum())
