from pymongo import MongoClient
from pymongo.database import Database

from pymongo.errors import ConnectionFailure

# Detalles de la conexión
username = "admin"
password = "admin"
hosts = "nodo01:27017,nodo02:27018,nodo03:27019"
replica_set_name = "rs0"
auth_source = "admin"  # Base de datos donde se autentica el usuario

# URI de conexión
uri = f"mongodb://{username}:{password}@{hosts}/?replicaSet={replica_set_name}&authSource={auth_source}"
print(uri)
try:
    # Crear el cliente MongoDB
    client = MongoClient(uri)

    db: Database = client.get_database("admin")
    print(db.list_collection_names())

    # Verificar la conexión
    print("Conectando a MongoDB...")
    client.admin.command('ping')
    print("Conectado exitosamente al replica set.")

    # Mostrar el estado del replica set
    print("Estado del replica set:")
    print(client.admin.command("replSetGetStatus"))
    print(client.nodes)

except ConnectionFailure as e:
    print(f"Error de conexión a MongoDB: {e}")
finally:
    # Cerrar la conexión cuando sea necesario
    client.close()
