from scraper.olimpica_api import info_producto

def revisar_producto(id_producto):

    datos_producto = info_producto(id_producto)

    if datos_producto["precio_hoy"] < datos_producto["precio_pleno"]:
        return datos_producto
    elif datos_producto["precio_con_descuento"] < datos_producto["precio_pleno"]:
        return datos_producto
    
    # Para ver todos los productos en la base de datos, devolver datos_producto
    return None

def comparadores(producto):
    mensaje = ""

    # Comparador Van Camp's 320G vs. prod. de referencia Atún Zenu
    if (producto["id"] == 2299909):
        comparador = info_producto(2219454)
        mensaje += (
            f"_Producto de referencia: {comparador['nombre']} > ${comparador['precio_hoy']:,.0f}_\n"
        )

    # Comparador Atún Zenu 160G vs. prod. de referencia Van Camp's 320G
    if (producto["id"] == 2219454):
        primer_comparador = info_producto(2299909)
        segundo_comparador = info_producto(2328698)
        mensaje += (
            f"_Producto de referencia: {primer_comparador['nombre']} > ${primer_comparador['precio_hoy']:,.0f}_\n"
        )
        mensaje += (
            f"_Producto de referencia: {segundo_comparador['nombre']} > ${segundo_comparador['precio_hoy']:,.0f}_\n"
        )

    # Comparador Atun Zenu 240G vs. prod. de referencia Atún Zenu
    if (producto["id"] == 2328698):
        primer_comparador = info_producto(2219454)
        segundo_comparador = info_producto(453544)
        mensaje += (
            f"_Producto de referencia: {primer_comparador['nombre']} > ${primer_comparador['precio_hoy']:,.0f}_\n"
        )
        mensaje += (
            f"_Producto de referencia: {segundo_comparador['nombre']} > ${segundo_comparador['precio_hoy']:,.0f}_\n\n"
        )

    # Comparador Tortillas x8 vs. Tortillas x15
    if (producto["id"] == 991917):
        comparador = info_producto(927656)
        mensaje += (
            f"_Producto de referencia: {comparador['nombre']} > ${comparador['precio_hoy']:,.0f}_\n"
        )
    
    # Comparador Tortillas x15 vs. Tortillas x8 
    if (producto["id"] == 927656):
        comparador = info_producto(991917)
        mensaje += (
            f"_Producto de referencia: {comparador['nombre']} > ${comparador['precio_hoy']:,.0f}_\n"
        )
    
    # Comparador Queso Colanta Tajado 250G vs. 500G 
    if (producto["id"] == 230851):
        comparador = info_producto(230849)
        mensaje += (
            f"_Producto de referencia: {comparador['nombre']} > ${comparador['precio_hoy']:,.0f}_\n"
        )

    # Comparador Queso Colanta Tajado 500G vs. 250G 
    if (producto["id"] == 230849):
        comparador = info_producto(230851)
        mensaje += (
            f"_Producto de referencia: {comparador['nombre']} > ${comparador['precio_hoy']:,.0f}_\n"
        )
    return mensaje
        