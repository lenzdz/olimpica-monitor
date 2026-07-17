import requests

from config import DISCORD_WEBHOOK


def enviar_mensaje(texto):

    requests.post(
        DISCORD_WEBHOOK,
        json={
            "content": texto
        }
    )