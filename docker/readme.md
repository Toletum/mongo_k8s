/usr/bin/openssl rand -base64 741 > keyfile


mongosh -u $MONGO_INITDB_ROOT_USERNAME -p $MONGO_INITDB_ROOT_PASSWORD

rs.initiate()


rs.add("nodo02:27018")
rs.add("nodo03:27019")

rs.status()


mongosh 'mongodb://admin:admin@nodo01:27017,nodo02:27018,nodo03:27019/?replicaSet=rs0&authSource=admin'
