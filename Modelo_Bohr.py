import math
from manim import*
import numpy as np
import random as rd
from elemento import*
import pandas as pd
elementos = pd.read_csv("Elementos.csv")

class Nucleo(VGroup):
    def __init__(self, n_protones, n_neutrones, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.n_protones = n_protones
        self.n_neutrones = n_neutrones
        protones = []
        neutrones = []

        for p in range(n_protones):
            protones.append("p")
        for n in range(n_neutrones):
            neutrones.append("n")
        nuclidos = neutrones+protones
        rd.shuffle(nuclidos)
        nucelo = VGroup()
        n_masico = n_protones+n_neutrones
        distancia = 120
        for nuclido in nuclidos:
            alfa = rd.uniform(0,2*PI)
            if nuclido == "n":
                nucelo.add(Dot(stroke_width = 2,color = GRAY, fill_opacity=0.8).shift(np.array([math.cos(alfa)*0.0005*rd.randint(0,int(math.sqrt(n_masico)))*distancia,math.sin(alfa)*0.0005*rd.randint(0,int(math.sqrt(n_masico)))*distancia,0])).scale(1.5))
            else:
                nucelo.add(Dot(stroke_width = 2,color = RED, fill_opacity=0.8).shift(np.array([math.cos(alfa)*0.0005*rd.randint(0,int(math.sqrt(n_masico)))*distancia,math.sin(alfa)*0.0005*rd.randint(0,int(math.sqrt(n_masico)))*distancia,0])).scale(1.5))   
        self.add(nucelo)

        
        

        

class Electrones(VGroup):
    def __init__(self, n_electrones, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.n_electrones = n_electrones
        capa = 1
        n_1 = VGroup()
        n_2 = VGroup()
        n_3 = VGroup()
        n_4 = VGroup()
        n_5 = VGroup()
        n_6 = VGroup()
        capas=[n_1,n_2,n_3,n_4,n_5, n_6]
        def distribuir_electrones(n_electrones):
            angulos = 360/n_electrones
            self.add(Circle(color = BLUE_A, radius = capa, stroke_width = 1.5))
            for electrones in range(n_electrones):
                capas[capa-1].add(Dot(color = BLUE).move_to(capa*np.array([math.cos(math.radians(angulos*electrones)),math.sin(math.radians(angulos*electrones)), 0])))
        if n_electrones <= 2:
            distribuir_electrones(n_electrones)
            self.add(n_1)
        elif n_electrones-2 <= 8:
            distribuir_electrones(2)
            n_electrones = n_electrones-2
            self.add(n_1)
            capa = 2
            distribuir_electrones(n_electrones)
            self.add(n_2)
        elif n_electrones - 10 <= 18:
            distribuir_electrones(2)
            capa = 2
            distribuir_electrones(8)
            capa = 3
            n_electrones = n_electrones - 10
            distribuir_electrones(n_electrones)
            self.add(n_1)
            self.add(n_2)
            self.add(n_3)
        elif n_electrones - 28 <= 32:
            distribuir_electrones(2)
            capa = 2
            distribuir_electrones(8)
            capa = 3
            distribuir_electrones(18)
            capa = 4
            n_electrones = n_electrones - 28
            distribuir_electrones(n_electrones)
            self.add(n_1)
            self.add(n_2)
            self.add(n_3)
            self.add(n_4)
        elif n_electrones - 60 <= 50:
            distribuir_electrones(2)
            capa = 2
            distribuir_electrones(8)
            capa = 3
            distribuir_electrones(18)
            capa = 4
            distribuir_electrones(32)
            capa = 5
            n_electrones = n_electrones - 60
            distribuir_electrones(n_electrones)
            self.add(n_1)
            self.add(n_2)
            self.add(n_3)
            self.add(n_4)
            self.add(n_5)
        else:
            distribuir_electrones(2)
            capa = 2
            distribuir_electrones(8)
            capa = 3
            distribuir_electrones(18)
            capa = 4
            distribuir_electrones(32)
            capa = 5
            distribuir_electrones(50)
            capa = 6
            n_electrones = n_electrones - 110
            distribuir_electrones(n_electrones)
            self.add(n_1)
            self.add(n_2)
            self.add(n_3)
            self.add(n_4)
            self.add(n_5)
            self.add(n_6)

class Atomo(VGroup):
    def __init__(self, n_protones, n_neutrones, n_electrones, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.n_protones = n_protones
        self.n_neutrones = n_neutrones
        self.n_electrones = n_electrones
        self.add(Nucleo(n_protones, n_neutrones).scale(0.5+1/n_protones))
        self.add(Electrones(n_electrones))


alcalinos = [3,11,19,37,55,87]
alcalinoterreos = [4,12,20,38,56,88]
transicion = [21,22,23,24,25,26,27,28,29,30,39,40,41,42,43,44,45,46,47,48,72,73,74,75,76,77,78,79,80,104,105,106,107,108,109,110,111,112]
lantanidos = [57,58,59,60,61,62,63,64,65,66,67,68,69,70,71]
actinidos = [89,90,91,92,93,94,95,96,97,98,99,100,101,102,103]
halogenos = [9,17,35,53,85,117]
gases_nobles = [2,10,18,36,54,86,118]
no_metales = [6,7,8,15,16,34]
semimetales_arriba = [5,14,32,33,51,52,84]
semimetales = [13,31,49,50,81,82,83,113,114,115,116]

class atomo(Scene):
    def construct(self):
        nucleo = Nucleo(118,118)
        n_e = 118
        electrones = Electrones(n_e)
        tamaño_nucleo = 1
        tamaño_electrones = 1
        for i in range(118):
            tamaño_nucleo = tamaño_nucleo *0.988
            tamaño_electrones = tamaño_electrones * 0.995
        self.add(nucleo.scale(tamaño_nucleo).shift(3*RIGHT))
        self.add(electrones.scale(tamaño_electrones).shift(3*RIGHT))
        self.add(Elemento(numero = 1, relleno = color_hidrogeno).shift(4*LEFT).scale(2.5))
        self.wait()

class testeo(Scene):
    def construct(self):
        numero = 1
        def rotasiong(electrones, n_e):
            if n_e <= 2:
                self.play(Rotate(electrones[1]),rate_func = linear, run_time = 2)
            elif n_e <= 10:
                self.play(Rotate(electrones[1], about_point = electrones[0].get_center()), Rotate(electrones[3], PI, about_point = electrones.get_center()), rate_func = linear, run_time = 2)
            elif n_e <= 28:
                self.play(Rotate(electrones[3], about_point = electrones[0].get_center()), Rotate(electrones[4], PI, about_point = electrones.get_center()), Rotate(electrones[5], PI/2, about_point = electrones.get_center()), rate_func = linear, run_time = 2)
            elif n_e <= 60:
                self.play(Rotate(electrones[4], about_point = electrones[0].get_center()), Rotate(electrones[5], PI, about_point = electrones.get_center()), Rotate(electrones[6], PI/2, about_point = electrones.get_center()), Rotate(electrones[7], PI/4, about_point = electrones.get_center()), rate_func = linear, run_time = 2)
            elif n_e <= 110:
                self.play(Rotate(electrones[5], about_point = electrones[0].get_center()), Rotate(electrones[6], PI, about_point = electrones.get_center()), Rotate(electrones[7], PI/2, about_point = electrones.get_center()), Rotate(electrones[8], PI/4, about_point = electrones.get_center()), Rotate(electrones[9], PI/6, about_point = electrones.get_center()), rate_func = linear, run_time = 2)
            else:
                self.play(Rotate(electrones[6], about_point = electrones[0].get_center()), Rotate(electrones[7], PI, about_point = electrones.get_center()), Rotate(electrones[8], PI/2, about_point = electrones.get_center()), Rotate(electrones[9], PI/4, about_point = electrones.get_center()), Rotate(electrones[10], PI/6, about_point = electrones.get_center()), Rotate(electrones[11], PI/8, about_point = electrones.get_center()), rate_func = linear, run_time = 2)
        tamaño_nucleo = 1
        tamaño_electrones = 1
            
        for i in range(118):
        
            if numero == 1:
                relleno = color_hidrogeno
            if numero in alcalinos:
                relleno = colores_alcalinos
            if numero in alcalinoterreos:
                relleno = colores_alcalinoterreos
            if numero in transicion:    
                relleno =colores_bloque_d 
            if numero in  lantanidos:    
                relleno =colores_lantanidos 
            if numero in  actinidos:    
                relleno =colores_actinidos 
            if numero in  semimetales:    
                relleno =colores_semimetales
            if numero in  semimetales_arriba:    
                relleno =colores_semimetales_arriba 
            if numero in  no_metales:    
                relleno =colores_no_metales 
            if numero in  halogenos:    
                relleno =colores_halogenos 
            if numero in  gases_nobles:    
                relleno =colores_gases_nobles 
            elemento = Elemento(numero = numero, relleno = relleno).shift(4*LEFT).scale(2.5)
            atomo = Nucleo(
                int(float(str(elementos.iloc[[numero-1],[5]]).split()[2])),
                int(float(str(elementos.iloc[[numero-1],[4]]).split()[2]))).shift(3*RIGHT)
            nube = Electrones(int(float(str(elementos.iloc[[numero-1],[6]]).split()[2]))).shift(3*RIGHT)
            tamaño_nucleo = tamaño_nucleo *0.988
            tamaño_electrones = tamaño_electrones * 0.995

            self.add(elemento)
            self.add(atomo.scale(tamaño_nucleo))
            self.add(nube.scale(tamaño_electrones))
            rotasiong(nube,int(float(str(elementos.iloc[[numero-1],[6]]).split()[2])))
            self.clear()
            numero +=1

