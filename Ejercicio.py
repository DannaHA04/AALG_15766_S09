lab=[[1,1,1,1,0,1,1,1,1],
   [1,0,0,1,0,1,0,0,0],
   [1,1,0,1,1,1,1,0,1],
   [0,1,0,1,0,0,1,0,1],
   [1,1,1,1,1,1,1,1,1],
   [1,0,1,0,0,0,1,0,1],
   [1,1,1,1,0,1,1,0,1],
   [1,0,0,1,0,1,0,0,1],
   [1,1,1,1,0,1,1,1,1]]



res=[[0]*9 for _ in range(9)]


def imprime(mat):
  for fila in mat:
    for c in fila:
      print(f"{c},", end="")
    print()
  print()



def valida(fil, col):
  if 0 <= fil < len(lab) and 0 <= col < len(lab[0]):
    if lab[fil][col] == 1 and res[fil][col] == 0:
      return True
  return False



def laberinto(fil, col, salida_fila, salida_col):
  if (fil, col) == (salida_fila, salida_col):
    res[fil][col] = 1
    imprime(res)
    return True

  
  if valida(fil, col):
    res[fil][col] = 1
    imprime(res)



    # Direcciones: abajo, derecha, izquierda, arriba

    if laberinto(fil+1, col, salida_fila, salida_col):
      return True
    if laberinto(fil, col+1, salida_fila, salida_col):
      return True
    if laberinto(fil, col-1, salida_fila, salida_col):
      return True
    if laberinto(fil-1, col, salida_fila, salida_col):
      return True

    res[fil][col] = 0 # backtrack
  return False



# Posición inicial: (0, 0)

# Posición final (salida): (2, 0)

if laberinto(0, 0, 2, 0):

  print("¡Camino encontrado!")

else:

  print("No hay salida.")