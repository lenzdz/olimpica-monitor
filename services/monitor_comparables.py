import json

from scraper.jumbo_api import info_producto_jumbo
from scraper.olimpica_api import info_producto_olimpica

def comparacion_jumbo_a_olimpica(ean, resultado):

    with open("data/productos_comparables.json", encoding="utf-8") as archivo:
        productos_comparables = json.load(archivo) 

    for producto_comp in productos_comparables:

        mensaje = ""
        # Si el producto que tiene descuento está en la lista de artículos comparables, revisa si el precio en Jumbo es menor que el de Olímpica hoy (en general)
        if (ean == producto_comp["jumbo"]):
            item_olimpica = info_producto_olimpica(producto_comp["olimpica"])
            precio_item_olimpica = item_olimpica["precio_hoy"]
            if resultado["precio_hoy"] > precio_item_olimpica:
                mensaje += f"⚠️ Ojo: este producto hoy cuesta menos en Olímpica (${precio_item_olimpica:,.0f})."
        
        return mensaje
    
def comparacion_olimpica_a_jumbo(id_producto, resultado):

    with open("data/productos_comparables.json", encoding="utf-8") as archivo:
        productos_comparables = json.load(archivo) 

    for producto_comp in productos_comparables:

        mensaje = ""
        # Si el producto que tiene descuento está en la lista de artículos comparables, revisa si el precio en Jumbo es menor que el de Olímpica hoy (en general)
        if (id_producto == producto_comp["olimpica"]):
            item_jumbo = info_producto_jumbo(producto_comp["jumbo"])
            precio_item_jumbo = item_jumbo["precio_hoy"]
            if resultado["precio_hoy"] > precio_item_jumbo:
                mensaje += f"⚠️ Ojo: este producto hoy cuesta menos en Jumbo (${precio_item_jumbo:,.0f})."
        
        return mensaje