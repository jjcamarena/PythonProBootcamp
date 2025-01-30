import random

tiros = '''
______                 _______                  _____
--'  ____)          ---'    ____)____           ---'   ___)______
    (_____)                     ______)                   ________)
 1  (_____)          2         _______)          3    _____________)
    (____)                   _______)                 (____)
-.__(___)           ---.___________)            ---.__(___)
'''

piedra = '''
    _______
---'   ____)
      (_____)
 1    (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'    ____)____
            ______)
 2         _______)
          _______)
---.___________)
'''

tijeras = '''
    _____
---'   ___)______
          ________)
 3    _____________)
      (____)
---.__(___)
'''

# print(tiros)
opcionJugador = int(input("\nSelecciona: \nPIEDRA = 1\nPAPEL = 2\nTIJERAS = 3\n---> "))

listaTiros = ["Piedra","Papel","Tijeras"]
print(f"Has seleccionado: {listaTiros[opcionJugador - 1]}")
if opcionJugador == 1:
    print(piedra)
elif opcionJugador == 2:
    print(papel)
else:
    print(tijeras)

listaCPU = [0, 1, 2]
randomCPU = listaTiros[random.choice(listaCPU)]
print("La computadora seleccionó: " + randomCPU)

# Convertir valor CPU a entero
opcionCPU = 0
if randomCPU == "Piedra":
    opcionCPU = 1
    print(piedra)
elif randomCPU == "Papel":
    opcionCPU = 2
    print(papel)
else:
    opcionCPU = 3
    print(tijeras)

if opcionJugador == opcionCPU:
    print("EMPATE !!")
elif opcionJugador == 1 and opcionCPU == 2:
    print("PERDISTE !!")
elif opcionJugador == 1 and opcionCPU == 3:
    print("GANASTE !!")
elif opcionJugador == 2 and opcionCPU == 1:
    print("GANASTE !!")
elif opcionJugador == 2 and opcionCPU == 3:
    print("PERDISTE !!")
elif opcionJugador == 3 and opcionCPU == 1:
    print("PERDISTE !!")
elif opcionJugador == 3 and opcionCPU == 2:
    print("GANASTE !!")

print("\nBye !!2")