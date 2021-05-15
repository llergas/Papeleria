print("Tienda escolar\n")

# Se ingresa el capital total de trabajo y se deja almacenada en una variable

cap_total = float(input("Ingrese el capital total: $"))
print()

# Se ingresa los datos del producto con sus diferentes tipos de datos.

nom1 = input("Ingrese el nombre del producto 1: ")
cant1 = int(input(f"Ingrese la cantidad que se compró del producto {nom1}: "))
valor_compra1 = int(input(f"Ingrese el valor de la compra del producto {nom1}: $"))
print()

nom2 = input("Ingrese el nombre del producto 2: ")
cant2 = int(input(f"Ingrese la cantidad que se compró del producto {nom2}: "))
valor_compra2 = int(input(f"Ingrese el valor de la compra del producto {nom2}: $"))
print()

nom3 = input("Ingrese el nombre del producto 3: ")
cant3 = int(input(f"Ingrese la cantidad que se compró del producto {nom3}: "))
valor_compra3 = int(input(f"Ingrese el valor de la compra del producto {nom3}: $"))
print()

# Se utiliza un dato de tipo bool para confirmar si se tuvo o no problemas con la compra del producto.

prob = bool(int(input("Tuvo algún problema con la compra: Si = 1 / No = 0: ")))
print(prob)

valor_total1 = int(valor_compra1 * cant1)
valor_total2 = int(valor_compra2 * cant2)
valor_total3 = int(valor_compra3 * cant3)

print("\n")

# Se hace el informe de la compra que se realizo. se utiliza el formato de impresión f"{}"
# Se utiliza multiplicaciones y divisiones para darles valores a las variables.

print("Valor unitario por producto".center(50))
print()

print(f"El valor por unidad del producto {nom1} fue de: ${valor_compra1 / cant1:,}")
print(f"El valor por unidad del producto {nom2} fue de: ${valor_compra2 / cant2:,}")
print(f"El valor por unidad del producto {nom3} fue de: ${valor_compra3 / cant3:,} \n")


print("Valor invertido por producto y total".center(50))
print()

print(f"El valor invertido en la compra del producto {nom1} fue de: ${valor_compra1:,}")
print(f"El valor invertido en la compra del producto {nom2} fue de: ${valor_compra2:,}")
print(f"El valor invertido en la compra del producto {nom3} fue de: ${valor_compra3:,}")
total_invertido = valor_compra1 + valor_compra2 + valor_compra3
print(f"El valor invertido total fue de: ${total_invertido:,}\n")

# Se utiliza el operador de asignación += para darle un nuevo valor a la variable cap_total

cap_total -= total_invertido

print()

print(f"El capital total actual es de: ${cap_total:,} \n")

print("Valor de venta por producto".center(50))
print()

valor_ventaun1 = int(input(f"¿A que valor desea vender el producto {nom1}, si el valor por unidad "
                           f"es de ${valor_compra1 / cant1:,}?: $"))

valor_ventaun2 = int(input(f"¿A que valor desea vender el producto {nom2}, si el valor por unidad "
                           f"es de ${valor_compra2 / cant2:,}?: $"))

valor_ventaun3 = int(input(f"¿A que valor desea vender el producto {nom3}, si el valor por unidad "
                           f"es de ${valor_compra3 / cant3:,}?: $"))

print("Ventas".center(50))
print()

uni1 = int(input(f"Ingrese la cantidad de unidades vendidas del producto {nom1}, si el stock es de {cant1}: "))
uni2 = int(input(f"Ingrese la cantidad de unidades vendidas del producto {nom2}, si el stock es de {cant2}: "))
uni3 = int(input(f"Ingrese la cantidad de unidades vendidas del producto {nom3},si el stock es de {cant3}: "))

print()


print(f"El valor total de las ventas del producto {nom1} es de: ${uni1 * valor_ventaun1:,}")
print(f"El valor total de las ventas del producto {nom2} es de: ${uni2 * valor_ventaun2:,}")
print(f"El valor total de las ventas del producto {nom3} es de: ${uni3 * valor_ventaun3:,}")
vventa_total = (uni1 * valor_ventaun1) + (uni2 * valor_ventaun2) + (uni3 * valor_ventaun3)
print(f"El Valor total de todas las ventas es de ${vventa_total:,}\n")

print("Inventario sobrante".center(50))
print()

stock1 = cant1 - uni1
stock2 = cant2 - uni2
stock3 = cant3 - uni3

print(f"Las unidades sobrantes del producto son: {stock1} unidades")
print(f"Las unidades sobrantes del producto son: {stock2} unidades")
print(f"Las unidades sobrantes del producto son: {stock3} unidades")

# Se utiliza comparativos para darle respuesta a una pregunta de si / True o No / False.

print(f"Las ventas del producto {nom1} superaron la inversion del producto: {(uni1 * valor_ventaun1) > valor_compra1}")
print(f"Las ventas del producto {nom2} superaron la inversion del producto: {(uni2 * valor_ventaun2) > valor_compra2}")
print(f"Las ventas del producto {nom3} superaron la inversion del producto: {(uni3 * valor_ventaun3) > valor_compra3}")
print(f"Las ventas totales superaron las inversiones totales: {vventa_total > total_invertido}\n")

gan_total = vventa_total  - total_invertido


print("Ganancia".center(50))
print()
print(f"El valor de la ganancia total es de: ${gan_total:,}\n")

print("Nuevo capital".center(50))
print()
cap_total += gan_total
print(f"Su nuevo capital total es de: ${int(cap_total):,}")