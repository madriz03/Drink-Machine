print("===============================================")
print("Bienvenido a tu maquina dispensadora de bebida")
print("===============================================")

a01 = "Cocacola"
a02 = "Agua"
a03 = "Cerveza Pilsen"
a04 = "Cerveza Light"

inventario = {"a01": 2000, "a02": 3000, "a03": 4000, "a04": 5000} 

credito = int(input("Ingresa el Dinero para Abonar a tu Credito: "))

producto = input("Ingresa el codigo del producto que quieres comprar: ")

if producto == "a01":
    print(f"Compraste, {a01}")
elif producto == "a02":
    print(f"Compraste, {a02}")
elif producto == "a03":
    print(f"compraste, {a03}")
else:
    print(f"Compraste,  {a04}")
    

costo = inventario.get(producto)
while costo > credito:
    credito2 = int(input("Tu credito no es suficiente, agrega saldo a tu credito: "))
    credito = credito + credito2 
    if credito > costo:
        break

print("Tu compra fue  exitosa")
cambio = credito - costo 
print("==================")
print("Resumen de compra")
print("==================")

print(f"Tu credito era de \n{credito}")
print(f"Pagaste \n{costo}")
print(f"Tu cambio es de \n{cambio}")