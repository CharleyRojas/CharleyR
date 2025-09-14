# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [  # Madrid
        [  # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 31}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [  # Barcelona
        [  # Semana 1
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 34}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 33}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 35}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 36}
        ]
    ],
    [  # Sevilla
        [  # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 38}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 40}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 39}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 37}
        ]
    ]
]

def calcular_promedio_ciudades(temperaturas_data, nombres_ciudades):

    promedios = {}

    for i in range(len(nombres_ciudades)):
        total_temp = 0
        total_dias = 0

        # Recorrer todas las semanas y días de la ciudad
        for semana in temperaturas_data[i]:
            for dia in semana:
                total_temp += dia["temp"]
                total_dias += 1

        # Calcular el promedio
        promedio = total_temp / total_dias
        promedios[nombres_ciudades[i]] = round(promedio, 1)

    return promedios


# Lista de nombres de ciudades
ciudades = ["Madrid", "Barcelona", "Sevilla"]

# Usar la función
resultados = calcular_promedio_ciudades(temperaturas, ciudades)

# Mostrar resultados
print("PROMEDIO DE TEMPERATURAS POR CIUDAD")
print("=" * 35)
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio}°C")