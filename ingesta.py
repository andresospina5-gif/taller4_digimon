import requests
from pymongo import MongoClient

# Mongo
client = MongoClient("mongodb://localhost:27017/")
db = client["taller4_db"]
collection = db["raw_data"]

# Limpiar colección
collection.delete_many({})

# Obtener lista inicial
url = "https://digi-api.com/api/v1/digimon?pageSize=250"

response = requests.get(url)
data = response.json()

digimons = data["content"]

detalles = []

for digimon in digimons:

    digimon_id = digimon["id"]

    detalle_url = f"https://digi-api.com/api/v1/digimon/{digimon_id}"

    detalle = requests.get(
        detalle_url,
        timeout=10
    ).json()

    detalles.append(detalle)

    print(f"Descargado: {digimon['name']}")

collection.insert_many(detalles)

print(f"Se cargaron {len(detalles)} Digimon")