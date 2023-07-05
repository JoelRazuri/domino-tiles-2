""" 
    Modificar el programa anterior para que pueda generar fichas de un juego que
    puede tener números de 0 a 𝑛.
"""

n = 8
contador = 0

for i in range(n+1):
    for j in range(contador,n+1):
        print(f"({i},{j})")
    contador+=1    