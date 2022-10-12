from elemento import *

elementos = pd.read_csv("Elementos.csv")

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



H = Elemento(numero =1,  relleno = color_hidrogeno)
Li = Elemento(numero =3, relleno = colores_alcalinos).next_to(H,DOWN, buff = 0)
Na = Elemento(numero =11, relleno = colores_alcalinos).next_to(Li,DOWN, buff = 0)
K = Elemento(numero =19, relleno = colores_alcalinos).next_to(Na,DOWN, buff = 0)
Rb = Elemento(numero =37, relleno = colores_alcalinos).next_to(K,DOWN, buff = 0)
Cs = Elemento(numero =55, relleno = colores_alcalinos).next_to(Rb,DOWN, buff = 0)
Fr = Elemento(numero =87, relleno = colores_alcalinos).next_to(Cs,DOWN, buff = 0)
grupo_1 = VGroup(H,Li,Na,K,Rb,Cs,Fr)
    
    #Grupo 2
Be = Elemento(numero =4, relleno = colores_alcalinoterreos).next_to(Li,RIGHT, buff = 0)
Mg = Elemento(numero =12, relleno = colores_alcalinoterreos).next_to(Be,DOWN, buff = 0)
Ca = Elemento(numero =20, relleno = colores_alcalinoterreos).next_to(Mg,DOWN, buff = 0)
Sr = Elemento(numero =38, relleno = colores_alcalinoterreos).next_to(Ca,DOWN, buff = 0)
Ba = Elemento(numero =56, relleno = colores_alcalinoterreos).next_to(Sr,DOWN, buff = 0)
Ra = Elemento(numero =88, relleno = colores_alcalinoterreos).next_to(Ba,DOWN, buff = 0)
grupo_2 = VGroup(Be,Mg,Ca,Sr,Ba,Ra)
    #Grupo 3
Sc = Elemento(numero =21, relleno = colores_bloque_d).next_to(Ca,RIGHT, buff = 0)
Y = Elemento(numero =39, relleno = colores_bloque_d).next_to(Sc,DOWN, buff = 0)
La = Elemento(numero =57, relleno = colores_lantanidos).next_to(Y,DOWN, buff = 0)
Ac = Elemento(numero =89, relleno = colores_actinidos).next_to(La,DOWN, buff = 0)
grupo_3 = VGroup(Sc, Y, La, Ac)
    
    #Grupo 4
Ti = Elemento(numero =22, relleno = colores_bloque_d).next_to(Sc,RIGHT, buff = 0)
Zr = Elemento(numero =40, relleno = colores_bloque_d).next_to(Ti,DOWN, buff = 0)
Hf = Elemento(numero =72, relleno = colores_bloque_d).next_to(Zr,DOWN, buff = 0)
Rf = Elemento(numero =104, relleno = colores_bloque_d).next_to(Hf,DOWN, buff = 0)
grupo_4 = VGroup(Ti,Zr,Hf,Rf)
    
    #Grupo 5
V = Elemento(numero =23, relleno = colores_bloque_d).next_to(Ti,RIGHT, buff = 0)
Nb = Elemento(numero =41, relleno = colores_bloque_d).next_to(V,DOWN, buff = 0)
Ta = Elemento(numero =73, relleno = colores_bloque_d).next_to(Nb,DOWN, buff = 0)
Db = Elemento(numero =105, relleno = colores_bloque_d).next_to(Ta,DOWN, buff = 0)
grupo_5 = VGroup(V, Nb, Ta, Db)
    
    #Grupo 6
Cr = Elemento(numero =24, relleno = colores_bloque_d).next_to(V,RIGHT, buff = 0)
Mo = Elemento(numero =42, relleno = colores_bloque_d).next_to(Cr,DOWN, buff = 0)
W = Elemento(numero =74, relleno = colores_bloque_d).next_to(Mo,DOWN, buff = 0)
Sg = Elemento(numero =106, relleno = colores_bloque_d).next_to(W,DOWN, buff = 0)
grupo_6 = VGroup(Cr,Mo,W,Sg)
    
    #Grupo 7
Mn = Elemento(numero =25, relleno = colores_bloque_d).next_to(Cr,RIGHT, buff = 0)
Tc = Elemento(numero =43, relleno = colores_bloque_d).next_to(Mn,DOWN, buff = 0)
Re = Elemento(numero =75, relleno = colores_bloque_d).next_to(Tc,DOWN, buff = 0)
Bh = Elemento(numero =107, relleno = colores_bloque_d).next_to(Re,DOWN, buff = 0)
grupo_7 = VGroup(Mn, Tc, Re, Bh)
    #Grupo 8
Fe = Elemento(numero =26, relleno = colores_bloque_d).next_to(Mn,RIGHT, buff = 0)
Ru = Elemento(numero =44, relleno = colores_bloque_d).next_to(Fe,DOWN, buff = 0)
Os = Elemento(numero =76, relleno = colores_bloque_d).next_to(Ru,DOWN, buff = 0)
Hs = Elemento(numero =108, relleno = colores_bloque_d).next_to(Os,DOWN, buff = 0)
grupo_8 = VGroup(Fe,Ru,Os,Hs)
    #Grupo 9
Co = Elemento(numero =27, relleno = colores_bloque_d).next_to(Fe,RIGHT, buff = 0)
Rh = Elemento(numero =45, relleno = colores_bloque_d).next_to(Co,DOWN, buff = 0)
Ir = Elemento(numero =77, relleno = colores_bloque_d).next_to(Rh,DOWN, buff = 0)
Mt = Elemento(numero =109, relleno = colores_bloque_d).next_to(Ir,DOWN, buff = 0)
grupo_9 = VGroup(Co,Rh,Ir,Mt)
    
    #Grupo 10
Ni = Elemento(numero =28, relleno = colores_bloque_d).next_to(Co,RIGHT, buff = 0)
Pd = Elemento(numero =46, relleno = colores_bloque_d).next_to(Ni,DOWN, buff = 0)
Pt = Elemento(numero =78, relleno = colores_bloque_d).next_to(Pd,DOWN, buff = 0)
Ds = Elemento(numero =110, relleno = colores_bloque_d).next_to(Pt,DOWN, buff = 0)
grupo_10 = VGroup(Ni, Pd, Pt, Ds)
    
    #Grupo 11
Cu = Elemento(numero =29, relleno = colores_bloque_d).next_to(Ni,RIGHT, buff = 0)
Ag = Elemento(numero =47, relleno = colores_bloque_d).next_to(Cu,DOWN, buff = 0)
Au = Elemento(numero =79, relleno = colores_bloque_d).next_to(Ag,DOWN, buff = 0)
Rg = Elemento(numero =111, relleno = colores_bloque_d).next_to(Au,DOWN, buff = 0)
grupo_11= VGroup(Cu, Ag, Au, Rg)
    
    #Grupo 12
Zn = Elemento(numero =30, relleno = colores_bloque_d).next_to(Cu,RIGHT, buff = 0)
Cd = Elemento(numero =48, relleno = colores_bloque_d).next_to(Zn,DOWN, buff = 0)
Hg = Elemento(numero =80, relleno = colores_bloque_d).next_to(Cd,DOWN, buff = 0)
Cn = Elemento(numero =112, relleno = colores_bloque_d).next_to(Hg,DOWN, buff = 0)
grupo_12= VGroup(Zn, Cd, Hg, Cn)
    
    #Grupo 13
    
Ga = Elemento(numero =31, relleno = colores_semimetales).next_to(Zn,RIGHT, buff = 0) # Inverted in order to put next to Zn
Al = Elemento(numero =13, relleno = colores_semimetales).next_to(Ga,UP, buff = 0)
B = Elemento(numero =5, relleno = colores_semimetales_arriba).next_to(Al,UP, buff = 0)
In = Elemento(numero =49, relleno = colores_semimetales).next_to(Ga,DOWN, buff = 0)
Tl = Elemento(numero =81, relleno = colores_semimetales).next_to(In,DOWN, buff = 0)
Nh = Elemento(numero =113, relleno = colores_semimetales).next_to(Tl,DOWN, buff = 0)
grupo_13 = VGroup(B,Al,Ga,In,Tl,Nh) # Reordered, as it should be
    #Grupo 14
C = Elemento(numero =6, relleno = colores_no_metales).next_to(B,RIGHT, buff = 0)
Si = Elemento(numero =14, relleno = colores_semimetales_arriba).next_to(C,DOWN, buff = 0)
Ge = Elemento(numero =32, relleno = colores_semimetales_arriba).next_to(Si,DOWN, buff = 0)
Sn = Elemento(numero =50, relleno = colores_semimetales).next_to(Ge,DOWN, buff = 0)
Pb = Elemento(numero =82, relleno = colores_semimetales).next_to(Sn,DOWN, buff = 0)
Fl = Elemento(numero =114, relleno = colores_semimetales).next_to(Pb,DOWN, buff = 0)
grupo_14 = VGroup(C,Si,Ge,Sn,Pb,Fl)
    #Grupo 15
N = Elemento(numero =7, relleno = colores_no_metales).next_to(C,RIGHT, buff = 0)
P = Elemento(numero =15, relleno = colores_no_metales).next_to(N,DOWN, buff = 0)
As = Elemento(numero =33, relleno = colores_semimetales_arriba).next_to(P,DOWN, buff = 0)
Sb = Elemento(numero =51, relleno = colores_semimetales_arriba).next_to(As,DOWN, buff = 0)
Bi = Elemento(numero =83, relleno = colores_semimetales).next_to(Sb,DOWN, buff = 0)
Mc = Elemento(numero =115, relleno = colores_semimetales).next_to(Bi,DOWN, buff = 0)
grupo_15 = VGroup(N,P,As,Sb,Bi,Mc)
    #Grupo 16      
O = Elemento(numero =8, relleno = colores_no_metales).next_to(N,RIGHT, buff = 0)
S = Elemento(numero =16, relleno = colores_no_metales).next_to(O,DOWN, buff = 0)
Se = Elemento(numero =34, relleno = colores_no_metales).next_to(S,DOWN, buff = 0)
Te = Elemento(numero =52, relleno = colores_semimetales_arriba).next_to(Se,DOWN, buff = 0)
Po = Elemento(numero =84, relleno = colores_semimetales_arriba).next_to(Te,DOWN, buff = 0)
Lv = Elemento(numero =116, relleno = colores_semimetales).next_to(Po,DOWN, buff = 0)
grupo_16 = VGroup(O,S,Se,Te,Po,Lv)
    #Grupo 17
F = Elemento(numero =9, relleno = colores_halogenos).next_to(O,RIGHT, buff = 0)
Cl = Elemento(numero =17, relleno = colores_halogenos).next_to(F,DOWN, buff = 0)
Br = Elemento(numero =35, relleno = colores_halogenos).next_to(Cl,DOWN, buff = 0)
I = Elemento(numero =53, relleno = colores_halogenos).next_to(Br,DOWN, buff = 0)
At = Elemento(numero =85, relleno = colores_halogenos).next_to(I,DOWN, buff = 0)
Ts = Elemento(numero =117, relleno = colores_halogenos).next_to(At,DOWN, buff = 0)
grupo_17 = VGroup(F,Cl,Br,I,At,Ts)
    #Grupo 18
Ne = Elemento(numero =10, relleno = colores_gases_nobles).next_to(F,RIGHT, buff = 0) # Inverted again
He = Elemento(numero =2, relleno = colores_gases_nobles).next_to(Ne,UP, buff = 0)
Ar = Elemento(numero =18, relleno = colores_gases_nobles).next_to(Ne,DOWN, buff = 0)
Kr = Elemento(numero =36, relleno = colores_gases_nobles).next_to(Ar,DOWN, buff = 0)
Xe = Elemento(numero =54, relleno = colores_gases_nobles).next_to(Kr,DOWN, buff = 0)
Rn = Elemento(numero =86, relleno = colores_gases_nobles).next_to(Xe,DOWN, buff = 0)
Og = Elemento(numero =118, relleno = colores_gases_nobles).next_to(Rn,DOWN, buff = 0)
grupo_18 = VGroup(He,Ne,Ar,Kr,Xe,Rn,Og)
    #Lantánidos
Lan = Elemento(numero =57, relleno = colores_lantanidos).next_to(Ac,DOWN, buff = 1.5)
Ce = Elemento(numero =58, relleno = colores_lantanidos).next_to(Lan,RIGHT, buff = 0)
Pr = Elemento(numero =59, relleno = colores_lantanidos).next_to(Ce,RIGHT, buff = 0)
Nd = Elemento(numero =60, relleno = colores_lantanidos).next_to(Pr,RIGHT, buff = 0)
Pm = Elemento(numero =61, relleno = colores_lantanidos).next_to(Nd,RIGHT, buff = 0)
Sm = Elemento(numero =62, relleno = colores_lantanidos).next_to(Pm,RIGHT, buff = 0)
Eu = Elemento(numero =63, relleno = colores_lantanidos).next_to(Sm,RIGHT, buff = 0)
Gd = Elemento(numero =64, relleno = colores_lantanidos).next_to(Eu,RIGHT, buff = 0)
Tb = Elemento(numero =65, relleno = colores_lantanidos).next_to(Gd,RIGHT, buff = 0)
Dy = Elemento(numero =66, relleno = colores_lantanidos).next_to(Tb,RIGHT, buff = 0)
Ho = Elemento(numero =67, relleno = colores_lantanidos).next_to(Dy,RIGHT, buff = 0)
Er = Elemento(numero =68, relleno = colores_lantanidos).next_to(Ho,RIGHT, buff = 0)
Tm = Elemento(numero =69, relleno = colores_lantanidos).next_to(Er,RIGHT, buff = 0)
Yb = Elemento(numero =70, relleno = colores_lantanidos).next_to(Tm,RIGHT, buff = 0)
Lu = Elemento(numero =71, relleno = colores_lantanidos).next_to(Yb,RIGHT, buff = 0)
lantanidos = VGroup(Lan,Ce,Pr,Nd,Pm,Sm,Eu,Gd,Tb,Dy,Ho,Er,Tm,Yb,Lu)
    #Actinidos
Act = Elemento(numero =89, relleno = colores_actinidos).next_to(Lan,DOWN, buff = 0)
Th = Elemento(numero =90, relleno = colores_actinidos).next_to(Act,RIGHT, buff = 0)
Pa = Elemento(numero =91, relleno = colores_actinidos).next_to(Th,RIGHT, buff = 0)
U = Elemento(numero =92, relleno = colores_actinidos).next_to(Pa,RIGHT, buff = 0)
Np = Elemento(numero =93, relleno = colores_actinidos).next_to(U,RIGHT, buff = 0)
Pu = Elemento(numero =94, relleno = colores_actinidos).next_to(Np,RIGHT, buff = 0)
Am = Elemento(numero =95, relleno = colores_actinidos).next_to(Pu,RIGHT, buff = 0)
Cm = Elemento(numero =96, relleno = colores_actinidos).next_to(Am,RIGHT, buff = 0)
Bk = Elemento(numero =97, relleno = colores_actinidos).next_to(Cm,RIGHT, buff = 0)
Cf = Elemento(numero =98, relleno = colores_actinidos).next_to(Bk,RIGHT, buff = 0)
Es = Elemento(numero =99, relleno = colores_actinidos).next_to(Cf,RIGHT, buff = 0)
Fm = Elemento(numero =100, relleno = colores_actinidos).next_to(Es,RIGHT, buff = 0)
Md = Elemento(numero =101, relleno = colores_actinidos).next_to(Fm,RIGHT, buff = 0)
No = Elemento(numero =102, relleno = colores_actinidos).next_to(Md,RIGHT, buff = 0)
Lr = Elemento(numero =103, relleno = colores_actinidos).next_to(No,RIGHT, buff = 0)
actinidos = VGroup(Act,Th,Pa,U,Np,Pu,Am,Cm,Bk,Cf,Es,Fm,Md,No,Lr)
    #bloques
bloque_s = VGroup(grupo_1, grupo_2)
bloque_p = VGroup(grupo_13,grupo_14,grupo_15,grupo_16,grupo_17,grupo_18)
bloque_d = VGroup(grupo_3,grupo_4,grupo_5,grupo_6,grupo_7,grupo_8,grupo_9,grupo_10,grupo_11,grupo_12 )
bloque_f = VGroup(lantanidos,actinidos)

Tabla_Periodica = VGroup(bloque_s, bloque_d, bloque_p, bloque_f)
Tabla_Periodica.scale(0.325)
Tabla_Periodica.move_to([0,0,0])


Elemento_Del_Video = Elemento(numero = 77, relleno = (RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK,WHITE, )).scale(0.5).next_to(Tabla_Periodica, UP, buff = -1.7)

class prueba(Scene):
    def construct(self):
        self.add(ImageMobject("fondo.png"))
        self.wait(0.2)
        self.play(Write(Tabla_Periodica), run_time = 3)
        self.wait()
        self.play(Transform(Ir.copy(), Elemento_Del_Video))
        self.wait()

        #self.add(Tabla_Periodica)

