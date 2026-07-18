import base64
import json
import requests

# BASE_URL = "https://www.jumbocolombia.com/_v/segment/graphql/v1"


# def obtener_flags_producto(product_id):
#     # 1. Crear {"id":98321}
#     variables = json.dumps(
#         {"id": product_id},
#         separators=(",", ":")
#     )

#     # 2. Convertir a Base64
#     variables_b64 = base64.b64encode(
#         variables.encode("utf-8")
#     ).decode("utf-8")

#     # 3. Crear el objeto extensions
#     extensions = {
#         "persistedQuery": {
#             "version": 1,
#             "sha256Hash": "7c16412d187093332665a3e33f79165687dbedbe291daa6842655678493fd1fd",
#             "sender": "tiendasjumboqaio.jumbo-minicart@2.x",
#             "provider": "vtex.search-graphql@0.x"
#         },
#         "variables": variables_b64
#     }

#     params = {
#         "workspace": "master",
#         "maxAge": "short",
#         "appsEtag": "remove",
#         "domain": "store",
#         "locale": "es-CO",
#         "operationName": "getProductInfo",
#         "variables": "{}",
#         "extensions": json.dumps(
#             extensions,
#             separators=(",", ":")
#         )
#     }

#     headers = {
#         "User-Agent": "Mozilla/5.0",
#         "Accept": "application/json"
#     }

#     respuesta = requests.get(
#         BASE_URL,
#         params=params,
#         headers=headers
#     )

#     # print("URL generada:")
#     # print(respuesta.url)
#     # print()

#     # print("Status:", respuesta.status_code)

#     #print(respuesta.text)
#     return respuesta.json()

BASE_URL = "https://www.jumbocolombia.com/_v/public/graphql/v1"


def obtener_producto(ean):

    variables = json.dumps(
        {
            "productId": str(ean)
        },
        separators=(",", ":")
    )

    variables_b64 = base64.b64encode(
        variables.encode()
    ).decode()

    extensions = {
        "persistedQuery": {
            "version": 1,
            "sha256Hash": "760fc6caac935139a1e999b6307073b64d789f9437c54d17dd9e75212b089a1b",
            "sender": "tiendasjumboqaio.custom-search@0.x",
            "provider": "jumbocolombiaio.jumbo-bff-web@1.x"
        },
        "variables": variables_b64
    }

    params = {
        "workspace": "master",
        "maxAge": "300",
        "appsEtag": "remove",
        "domain": "store",
        "locale": "es-CO",
        "operationName": "GetProduct",
        "variables": "{}",
        "extensions": json.dumps(
            extensions,
            separators=(",", ":")
        )
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    respuesta = requests.get(
        BASE_URL,
        params=params,
        headers=headers
    )

    return respuesta.json()

def obtener_descuento(info_producto):
    cards = (
        info_producto["data"]["getProduct"]["product"]["cards"]
    )

    if not cards:
        return None

    return cards[0]["finalPrice"]

def info_producto_jumbo(id_producto):
    info_producto_desde_api = obtener_producto(id_producto)
    precio_con_descuento = obtener_descuento(info_producto_desde_api)

    # Nombre del producto
    nombre_del_producto = str(info_producto_desde_api["data"]["getProduct"]["product"]["name"]).title()

    # Precio pleno del producto
    precio_pleno = info_producto_desde_api["data"]["getProduct"]["product"]["listPrice"]

    # Precio de hoy del producto (puede ser pleno o tener descuento para todos los medios de pago)
    precio_hoy = info_producto_desde_api["data"]["getProduct"]["product"]["price"]

    informacion_del_producto = {
        "id": id_producto,
        "nombre": nombre_del_producto,
        "precio_pleno": precio_pleno,
        "precio_hoy": precio_hoy,
        "precio_con_descuento": precio_con_descuento
    }

    return informacion_del_producto