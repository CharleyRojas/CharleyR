


#LECTURA COMPLETA DEL ARCHIVO

print("leyendo tu achivo espere..........")
#Volvemos a abrir el archivo para leer todo su contenido
archivo = open("my_notes.txt")
contenido = archivo.read()  # Lee todo el archivo como un solo texto
print("\nLectura completa del archivo:\n")
print(contenido)
archivo.close()
print("\nLectura completada y archivo cerrado correctamente.")
