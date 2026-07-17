from dotenv import load_dotenv
import os

load_dotenv()

WEBHOOK = os.getenv("DISCORD_WEBHOOK")