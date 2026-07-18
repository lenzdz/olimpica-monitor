import requests

from config import DISCORD_WEBHOOK
from config import JUMBO_DISCORD_WEBHOOK

def enviar_mensaje_canal_olimpica(texto):

    requests.post(
        DISCORD_WEBHOOK,
        json={
            "content": texto
        }
    )

def enviar_mensaje_canal_jumbo(texto):

    requests.post(
        JUMBO_DISCORD_WEBHOOK,
        json={
            "content": texto
        }
    )