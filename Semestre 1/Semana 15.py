# Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "Charley Rojas",
    "edad": 20,
    "ciudad": "Gonzalo Pizarro"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Sucumbios"  # Cambiamos la ciudad

# Agregar una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0984569255"  # Número ficticio

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print(informacion_personal)
