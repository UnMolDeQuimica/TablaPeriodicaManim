from manim import *
import pandas as pd

elementos = pd.read_csv("Elementos.csv")

class Elemento(VGroup):
    def __init__(self, numero=1, color = BLACK, relleno = (WHITE, BLUE), gradiente = 10, opacidad = 1, color_texto = BLACK,**kwargs):
        VGroup.__init__(self, **kwargs)
        self.numero = numero
        self.masa = str(elementos.iloc[[numero-1],[3]]).split()[2]
        self.simbolo = str(elementos.iloc[[numero-1],[2]]).split()[2]
        self.nombre = str(elementos.iloc[[numero-1],[1]]).split()[2]
        self.color = color
        self.opacidad = opacidad
        self.relleno = relleno
        self.color_texto = color_texto
        self.gradiente = gradiente
        marco = Rectangle(height = 2.8, width = 2, color=color,stroke_width = 0.2, fill_opacity = self.opacidad, fill_color = color_gradient(self.relleno, self.gradiente)).scale(0.8)
        
        self.add(marco)
        marca = Dot().next_to(marco, UP, buff = -0.3)
        if 10 <= numero < 100:
            marca.shift(0.15*RIGHT)
        if numero >= 100:
            marca.shift(0.3*RIGHT)
        self.add(marca)
        self.add(Text(self.simbolo, color = self.color_texto).scale(1.1).move_to(marco.get_center()))
        nom = Text(self.nombre, color = self.color_texto).scale(0.2).next_to(marco, DOWN, buff = -0.4)
        ratio = marco.get_width()/(1.25*nom.get_width())
        self.add(nom.scale(ratio))


        while nom.get_height() > 0.3:
            nom.scale(0.9)

        #self.add(Text(numero).scale(1).next_to(marca, LEFT, buff = 2))
        self.add(Tex(self.numero, color = self.color_texto).scale(0.65).next_to(marca, LEFT, buff = 0.5))
        self.remove(marca)

colores_base = ("#","#","#",WHITE,WHITE)
azulito1 = "#8fd3fe"
azulito2 = "#c7e9fe"
rojito1 ="#fe7474"
rojito2 ="#fe9d9d"
naranjita1 ="#ffb8a2"
naranjita2 ="#ffcdbd"
grisito1 = "#b0b0b0"
grisito2 = "#d7d7d7" 
purpurita1 = "#be92be"
purpurita2 = "#dbc2db"
rosita1 = "#ffc0cb"
rosita2 = "#ffdae0"
verdosito1 ="#a1dcd3"
verdosito2 = "#ECF8F6"
tierrita1 = "#e2d1c5"
tierrita2 = "#f3ece7"
cielito1 = "#b9b9e3"
cielito2 = "#f0f0f9"
pistachito1 = "#c1cfab"
pistachito2 = "#f1f4ec"
pollito1 = "#ffff99"
pollito2 = "#ffffcc"
color_hidrogeno = (azulito1,azulito2,WHITE)
colores_alcalinos = (rojito1, rojito2,WHITE)
colores_alcalinoterreos = (naranjita1,naranjita2,WHITE)
colores_bloque_d = (grisito1,grisito2,WHITE)
colores_lantanidos = (purpurita1,purpurita2,WHITE)
colores_actinidos = (rosita1,rosita2,WHITE)
colores_semimetales = (verdosito1, verdosito2,WHITE)
colores_semimetales_arriba = (tierrita1,tierrita2,WHITE)
colores_no_metales = (cielito1,cielito2,WHITE)
colores_halogenos = (pistachito1,pistachito2,WHITE)
colores_gases_nobles = (pollito1,pollito2 ,WHITE)


