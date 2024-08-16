opciones={
    "izquierda": "Te encontaste con un dragon",
    "derecha": "Encontraste un tesoro",
    "delante": "Caiste en un pozo"
}
eleccion=input("Estas en un cruce, ¿Quieres ir a la derecha, izquierda o adelante?: ").lower()

if eleccion in opciones:
    print("Respuesta:", opciones[eleccion])
else:
    print("opcion equivocada")