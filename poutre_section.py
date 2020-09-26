# Initialisation des variables
F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm

# poutre carrée
a = 15  # en mm

# poutre ronde
d = 5  # en mm

# poutre creuse
D = 15  # en mm
d = 5  # en mm

# Calcul de la section optimale
#programme doit faire tout les calculus et demonter lequel a une section optimale 

Irectangulaire = float(b * (h**3)) / (12)
delta_maxrectangulaire = float(F * L**3 )/ (3 * (E*10**3) * Irectangulaire) 


Icarre = float(a**4/12)
delta_maxcarre = float(F * L**3 )/ (3 * (E*10**3) * Icarre) 

#The math.pi constant normally returns to value of : 3.141592653589793.
Ironde = float(3.141592653589793*d**4/64)
delta_maxronde = float(F * L**3 )/ (3 * (E*10**3) * Ironde) 


Icreuse  = float(3.141592653589793*(D**4 - d**4)/ 64)
delta_maxcreuse = float(F * L**3 )/ (3 * (E*10**3) * Icreuse) 

delta_max = [delta_maxrectangulaire, delta_maxcarre, delta_maxronde, delta_maxcreuse]

section = ['rectangulaire', 'carré', 'ronde', 'creuse']

if min(delta_max) == delta_maxrectangulaire:
  print('Le type de section minimisant la deformation maximale est',section[0] ,'avec une déformation de' , round(min(delta_max), 2), 'mm')
elif min(delta_max) == delta_maxcarre:
  print('Le type de section minimisant la deformation maximale est' ,section [1],'avec une déformation de', round(min(delta_max), 2), 'mm')
elif min(delta_max) == delta_maxronde:
  print('Le type de section minimisant la deformation maximale est ',section[2] ,'avec une déformation de', round(min(delta_max), 2), 'mm')
elif min(delta_max) == delta_maxcreuse:
  print('Le type de section minimisant la deformation maximale est' , section[3] , 'avec une déformation de', round(min(delta_max), 2), 'mm')