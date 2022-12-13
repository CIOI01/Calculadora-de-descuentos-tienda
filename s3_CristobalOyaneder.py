precio = 1
suma_total = 0

while precio != 0:
    precio = float(input('Ingrese el Precio de los Productos: '))
    suma_total += precio

if suma_total < 50001:
     descuento = suma_total * 0.07
else:
    descuento = suma_total * 0.12


monto_a_pagar = suma_total - descuento

print(f'La sumatoria de todos los precios es: ${suma_total:.2f}')
print(f'El monto del descuento es: ${descuento:.2f}')
print(f'El monto a pagar es: ${monto_a_pagar:.2f}')