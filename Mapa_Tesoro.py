
FILENAME="mapa.txt"

#E:2 numeros enteros
#S: una matriz
def generar_matriz(filas, columnas):
    if isinstance (filas, int) and isinstance (columnas, int):
        with open(FILENAME, 'w')as archivo:
            line= columnas * '.'
            for _ in range(filas):
                archivo.write(line + '\n')
        
    else:
        return "Los datos ingresados son invalidos"


def character_tesoro(row, col):
    with open (FILENAME, 'r+') as archivo:        
        row_length = len(archivo.readline())
        archivo.seek(0)
        
        posicion = row * row_length + col +row #row*tamannioFilas + columna
        
        archivo.seek(posicion) 
        archivo.write("T")

#E: cordenadas en lista
#S: none
def obstaculos(coord):
    with open(FILENAME, 'r+') as archivo:
        row_lenght = len(archivo.readline()) #largo de las filas
        archivo.seek(0)

        for i in range(len(coord)-1):
            row1=coord[i][0] -1
            col1= coord[i][1] -1
            row2=coord[i+1][0] -1
            col2= coord[i+1][1] -1

            if row1 == row2: #Parte horizontal
                for c in range(min(col1, col2), max(col1, col2)+1):
                    offset = row1 * row_lenght + c + row1
                    archivo.seek(offset)
                    archivo.write('#')

            elif col1 == col2: #parte vertical
                for r in range(min(row1, row2), max(row1, row2)+1):
                    offset = r * row_lenght + col1 + r
                    archivo.seek(offset)
                    archivo.write('#')
            else:
                print("Error en las coordenadas")

def ver_mapa():
    archivo = open(FILENAME, 'r')
    contenido= archivo.read()
    print(contenido)


def generador_mapa():
    while True:
        print("""
        1.Crear Mapa
        2. Colocar Tesoro
        3. Colocar Obstaculos
        4. Ver mapa
        5. Salir
        """)
        opcion= int(input("Opcion a elegir: "))

        if opcion == 1:
            size_row = int(input("Ingrese la cantidad de filas de la matriz: "))
            size_col = int(input("Ingrese la cantidad de columnas de la matriz: "))

            generar_matriz(size_row, size_col)
            
        
        elif opcion == 2:
            print("Indique en que fila y columna desea colocar el tesoro")
            print("Segun este rango")
            print(f"Fila : {size_row}")
            print(f"Columna : {size_col}")
            
            fila = int(input("Fila: "))-1
            columna = int(input("Columna: "))-1

            character_tesoro(fila, columna)
            
        
        elif opcion == 3:
            print(f"Rango fila: {size_row}\nRango columna: {size_col}")
            print("Ejemplo Formato: '[(4,3),(6,3),(6,7)])' --> Haria una L")
            while True:
                try:
                    coordenadas = eval(input("Coordenadas: "))
                    if not isinstance(coordenadas, list):
                        print("Debe ingresar una lista")
                        continue
                    
                    valido = True
                    for fila, col in coordenadas:
                        if fila<0 or fila>= size_row or col<0 or col>=size_col:
                            valido= False
                    if valido:
                        break
                    
                    else:
                        print("Rango de las coordenadas equivocado")

                except:
                    print("Formato de coordenadas incorrecto")

            obstaculos(coordenadas)
            
        elif opcion == 4:
            ver_mapa()

        elif opcion == 5:
            print("Saliendo del programa...")
            break
            
        else:
            print("Opcion Invalida vuelva a intentarlo")

                
generador_mapa()







                    
