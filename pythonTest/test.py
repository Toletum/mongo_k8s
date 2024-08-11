from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Detalles de la conexión
username = "admin"
password = "admin"
hosts = "192.168.0.130:27017,192.168.0.130:27018,192.168.0.130:27019"
replica_set_name = "rs0"
auth_source = "admin"  # Base de datos donde se autentica el usuario

# URI de conexión
uri = f"mongodb://{username}:{password}@{hosts}/?replicaSet={replica_set_name}&authSource={auth_source}"

try:
    # Crear el cliente MongoDB
    client = MongoClient(uri)

    # Verificar la conexión
    print("Conectando a MongoDB...")
    client.admin.command('ping')
    print("Conectado exitosamente al replica set.")

    # Mostrar el estado del replica set
    print("Estado del replica set:")
    print(client.admin.command("replSetGetStatus"))

except ConnectionFailure as e:
    print(f"Error de conexión a MongoDB: {e}")
finally:
    # Cerrar la conexión cuando sea necesario
    client.close()
