def calcular_descuento(monto_total, porcentaje_descuento=10):

    return monto_total * (porcentaje_descuento / 100)


monto1 = 100.0
descuento1 = calcular_descuento(monto1)
total1 = monto1 - descuento1

print(f"Compra 1: ${monto1}")
print(f"Descuento (10%): ${descuento1}")
print(f"Total a pagar: ${total1}")
print()

# Segunda llamada: con monto y porcentaje personalizado
monto2 = 200.0
porcentaje2 = 15
descuento2 = calcular_descuento(monto2, porcentaje2)
total2 = monto2 - descuento2

print(f"Compra 2: ${monto2}")
print(f"Descuento ({porcentaje2}%): ${descuento2}")
print(f"Total a pagar: ${total2}")