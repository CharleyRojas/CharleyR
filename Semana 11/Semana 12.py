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

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Madrid", "Barcelona", "Sevilla"]

print("ANÁLISIS DE TEMPERATURAS POR CIUDAD Y SEMANA")
print("=" * 50)

for ciudad_idx, ciudad in enumerate(temperaturas):
    print(f"\n{ciudades[ciudad_idx]}:")
    print("-" * 30)

    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Semana {semana_idx + 1}: {promedio:.1f}°C")

# Mostrar también la temperatura más alta y más baja de cada ciudad
print("\n" + "=" * 50)
print("TEMPERATURAS EXTREMAS POR CIUDAD")
print("=" * 50)

for ciudad_idx, ciudad in enumerate(temperaturas):
    todas_temperaturas = []
    for semana in ciudad:
        for dia in semana:
            todas_temperaturas.append(dia["temp"])

    max_temp = max(todas_temperaturas)
    min_temp = min(todas_temperaturas)

    print(f"{ciudades[ciudad_idx]}:")
    print(f"  Máxima: {max_temp}°C")
    print(f"  Mínima: {min_temp}°C")
    print()