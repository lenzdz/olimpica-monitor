import json

# Módulos externos
from datetime import datetime

# Módulos de mi proyecto
from services.monitor_olimpica import monitor_olimpica
from services.monitor_jumbo import monitor_jumbo


monitor_olimpica()
monitor_jumbo()

print("Fin ejecución.")