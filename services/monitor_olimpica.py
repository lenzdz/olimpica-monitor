import json

# Módulos externos
from datetime import datetime

from scraper.olimpica_api import info_producto_olimpica
from services.monitor_comparables import comparacion_olimpica_a_jumbo

from notifiers.discord import enviar_mensaje_canal_olimpica

fecha_hoy = datetime.now().strftime("%d/%m/%Y")

# LÓGICA OLÍMPICA -------------------------------------------------- 

def monitor_olimpica():

    with open("data/productos_olimpica.json", encoding="utf-8") as archivo:
        productos_olimpica = json.load(archivo)

    with open("data/productos_comparables.json", encoding="utf-8") as archivo:
        productos_comparables = json.load(archivo)

    enviar_mensaje_canal_olimpica(f"🎉 Productos en oferta ahora ({fecha_hoy}) 🎉")

    counter = 0
    for producto in productos_olimpica:
        id_producto = producto["id"]

        # Verifica si el producto tiene descuentos. Si hay descuentos, devuelve la información del producto; si no los hay, devuelve None.
        resultado = revisar_producto_olimpica(id_producto)

        mensaje = ""
        if resultado:
            counter += 1

            nombre = resultado["nombre"]
            precio_pleno = resultado["precio_pleno"]
            precio_hoy = resultado["precio_hoy"]
            precio_con_descuento = resultado["precio_con_descuento"]

            mensaje += (
                f"-------------------------------------------\n"
                f"{producto['emoji']} **{nombre}**\n"
                f"**Precio normal:** ${precio_pleno:,.0f}\n"
                f"**Precio actual:** ${precio_hoy:,.0f}\n"
                f"**Con tarjeta Olímpica:** ${precio_con_descuento:,.0f}\n"
            )

            mensaje += comparadores_olimpica(producto)

            mensaje += comparacion_olimpica_a_jumbo(id_producto, resultado)

            enviar_mensaje_canal_olimpica(mensaje)

    if (counter == 0):
        mensaje_final = f"-------------------------------------------\n Hoy no hay productos en oferta 🙁"
    elif (counter == 1):
        mensaje_final = (
            f"-------------------------------------------\n"
            f"🎉 Hoy hay {counter} producto en oferta ({fecha_hoy}) 🎉 \n"
        )
    else:
        mensaje_final = (
            f"-------------------------------------------\n"
            f"🎉 Hoy hay {counter} productos en oferta ({fecha_hoy}) 🎉 \n"
        )

    enviar_mensaje_canal_olimpica(mensaje_final)

def revisar_producto_olimpica(id_producto):

    datos_producto = info_producto_olimpica(id_producto)

    if datos_producto["precio_hoy"] < datos_producto["precio_pleno"]:
        return datos_producto
    elif datos_producto["precio_con_descuento"] < datos_producto["precio_pleno"]:
        return datos_producto
    
    # Para ver todos los productos en la base de datos, devolver datos_producto
    return None

def comparadores_olimpica(producto):
    mensaje = ""

    # Comparador Van Camp's 320G vs. prod. de referencia Atún Zenu
    if (producto["id"] == 2299909):
        comparador = info_producto_olimpica(2219454)
        mensaje += (
            f"_Producto de referencia: {comparador['nombre']} > ${comparador['precio_hoy']:,.0f}_\n"
        )

    # Comparador Atún Zenu 160G vs. prod. de referencia Van Camp's 320G
    if (producto["id"] == 2219454):
        primer_comparador = info_producto_olimpica(2299909)
        segundo_comparador = info_producto_olimpica(2328698)
        mensaje += (
            f"_Producto de referencia: {primer_comparador['nombre']} > ${primer_comparador['precio_hoy']:,.0f}_\n"
        )
        mensaje += (
            f"_Producto de referencia: {segundo_comparador['nombre']} > ${segundo_comparador['precio_hoy']:,.0f}_\n"
        )

    # Comparador Atun Zenu 240G vs. prod. de referencia Atún Zenu
    if (producto["id"] == 2328698):
        primer_comparador = info_producto_olimpica(2219454)
        segundo_comparador = info_producto_olimpica(453544)
        mensaje += (
            f"_Producto de referencia: {primer_comparador['nombre']} > ${primer_comparador['precio_hoy']:,.0f}_\n"
        )
        mensaje += (
            f"_Producto de referencia: {segundo_comparador['nombre']} > ${segundo_comparador['precio_hoy']:,.0f}_\n\n"
        )

    # Comparador Tortillas x8 vs. Tortillas x15
    if (producto["id"] == 991917):
        comparador = info_producto_olimpica(927656)
        mensaje += (
            f"_Producto de referencia: {comparador['nombre']} > ${comparador['precio_hoy']:,.0f}_\n"
        )
    
    # Comparador Tortillas x15 vs. Tortillas x8 
    if (producto["id"] == 927656):
        comparador = info_producto_olimpica(991917)
        mensaje += (
            f"_Producto de referencia: {comparador['nombre']} > ${comparador['precio_hoy']:,.0f}_\n"
        )
    
    # Comparador Queso Colanta Tajado 250G vs. 500G 
    if (producto["id"] == 230851):
        comparador = info_producto_olimpica(230849)
        mensaje += (
            f"_Producto de referencia: {comparador['nombre']} > ${comparador['precio_hoy']:,.0f}_\n"
        )

    # Comparador Queso Colanta Tajado 500G vs. 250G 
    if (producto["id"] == 230849):
        comparador = info_producto_olimpica(230851)
        mensaje += (
            f"_Producto de referencia: {comparador['nombre']} > ${comparador['precio_hoy']:,.0f}_\n"
        )

    # Comparador Jamón Zenú 450G vs. prod. de referencia
    if (producto["id"] == 1149613):
        primer_comparador = info_producto_olimpica(1149617)
        segundo_comparador = info_producto_olimpica(1562174)
        mensaje += (
            f"_Producto de referencia: {primer_comparador['nombre']} > ${primer_comparador['precio_hoy']:,.0f}_\n"
        )
        mensaje += (
            f"_Producto de referencia: {segundo_comparador['nombre']} > ${segundo_comparador['precio_hoy']:,.0f}_\n\n"
        )

    # Comparador Jamón Zenú 250G vs. prod. de referencia
    if (producto["id"] == 1149617):
        primer_comparador = info_producto_olimpica(1149613)
        segundo_comparador = info_producto_olimpica(1571863)
        mensaje += (
            f"_Producto de referencia: {primer_comparador['nombre']} > ${primer_comparador['precio_hoy']:,.0f}_\n"
        )
        mensaje += (
            f"_Producto de referencia: {segundo_comparador['nombre']} > ${segundo_comparador['precio_hoy']:,.0f}_\n\n"
        )

    # Comparador Jamon Colanta Montefrio 450 G vs. prod. de referencia
    if (producto["id"] == 1562174):
        comparador = info_producto_olimpica(1149613)
        mensaje += (
            f"_Producto de referencia: {comparador['nombre']} > ${comparador['precio_hoy']:,.0f}_\n"
        )

    # Comparador Jamon Colanta 225 G vs. prod. de referencia
    if (producto["id"] == 1571863):
        comparador = info_producto_olimpica(1149617)
        mensaje += (
            f"_Producto de referencia: {comparador['nombre']} > ${comparador['precio_hoy']:,.0f}_\n"
        )
        
    return mensaje