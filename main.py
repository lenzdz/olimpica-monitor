import json

# Módulos externos
from datetime import datetime

# Módulos de mi proyecto
from services.monitor import revisar_producto
from notifiers.discord import enviar_mensaje

#enviar_mensaje("Hola desde Python")

with open("data/productos.json", encoding="utf-8") as archivo:
    productos = json.load(archivo)

fecha_hoy = datetime.now().strftime("%d/%m/%Y")

mensaje = ""
counter = 0
counter_two = 0
for producto in productos:
    counter_two += 1
    id_producto = producto["id"]

    # Verifica si el producto tiene descuentos. Si hay descuentos, devuelve la información del producto; si no los hay, devuelve None.
    resultado = revisar_producto(id_producto)

    if resultado:
        counter += 1

        nombre = resultado["nombre"]
        precio_pleno = resultado["precio_pleno"]
        precio_hoy = resultado["precio_hoy"]
        precio_con_descuento = resultado["precio_con_descuento"]

        mensaje += (
            f"{producto['emoji']} **{nombre}**\n"
            f"**Precio normal:** ${precio_pleno:,.0f}\n"
            f"**Precio actual:** ${precio_hoy:,.0f}\n"
            f"**Con tarjeta Olímpica:** ${precio_con_descuento:,.0f}\n\n"
        )

if (counter == 0):
    mensaje_final = "🙁 Hoy no hay productos en oferta."
elif (counter == 1):
    mensaje_final = f"🎉 Hoy hay {counter} producto en oferta ({fecha_hoy}))\n\n" + mensaje
else:
    mensaje_final = f"🎉 Hoy hay {counter} productos en oferta ({fecha_hoy}))\n\n" + mensaje

print("Se revisaron " + str(counter_two) + " productos.")
enviar_mensaje(mensaje_final)