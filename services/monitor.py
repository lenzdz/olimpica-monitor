from scraper.olimpica_api import info_producto

def revisar_producto(id_producto):

    datos_producto = info_producto(id_producto)

    if datos_producto["precio_hoy"] < datos_producto["precio_pleno"]:
        return datos_producto
    elif datos_producto["precio_con_descuento"] < datos_producto["precio_pleno"]:
        return datos_producto
    
    return None