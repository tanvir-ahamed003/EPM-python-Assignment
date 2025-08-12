#EPM assignment
#ID-232-141-003
#ID-232-141-012

import math
print('Enter the type of crystal Structure (BCC or FCC) ')
Structure1= input("Structure Type: ")
Structure= Structure1.strip().upper()

if Structure in ["BCC","FCC"]:
    density = float(input("Enter The Density of Material (Kg/m^3): "))
    atomic_mass = float(input("Enter The Atomic mass(kg/mol): "))
    avogadro = 6.023e23

    if Structure=="BCC":
        n = 2
    elif Structure=="FCC":
        n = 4
    #Lattice Parameter
    a = ((n * atomic_mass) / (density * avogadro)) **(1/3)
    # Atomic radius
    if Structure == "BCC":
        R = (math.sqrt(3) * a) / 4
    elif Structure == "FCC":
        R = (math.sqrt(2) * a) / 4

    # Atomic concentration
    Atm_concentration = (density / atomic_mass) * avogadro / 1e-6

    print(f"Lattice Parameter = {a:.5e} metre")
    print(f"Atomic Radius = {R:.5e} metre")
    print(f"Atomic Concentration = {Atm_concentration:.5e} atom/cm^3")

else:
    print("Invalid")
    exit()







