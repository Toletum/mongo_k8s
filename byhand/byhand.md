/etc/hosts

192.168.49.2 nodo01-host
192.168.49.2 nodo02-host
192.168.49.2 nodo03-host




kubectl apply -f myrs.yaml

kubectl apply -f nodo01-pvc.yaml
kubectl apply -f nodo02-pvc.yaml
kubectl apply -f nodo03-pvc.yaml

NOTE: Maybe you have to clean /data/db/*
      kubectl apply -f clean.yaml
      kubectl exec -ti clean -- sh
      rm -rf /data1/db/*
      rm -rf /data2/db/*
      rm -rf /data3/db/*

kubectl apply -f nodo01.yaml
kubectl apply -f nodo02.yaml
kubectl apply -f nodo03.yaml


kubectl exec -ti nodo01 -c nodo01 -- mongosh -eval 'rs.initiate();'
kubectl exec -ti nodo01 -c nodo01 -- mongosh -eval 'db.getSiblingDB("admin").createUser({user:process.env.MONGO_INITDB_ROOT_USERNAME,pwd:process.env.MONGO_INITDB_ROOT_PASSWORD,roles:[{role:"root",db:"admin"}]});'
kubectl exec -ti nodo01 -c nodo01 -- bash
mongosh -u $MONGO_INITDB_ROOT_USERNAME -p $MONGO_INITDB_ROOT_PASSWORD

rs.reconfig({_id: "rs0", version: 1, members: [ {_id: 0, host: "nodo01-host:27017"} ]});
rs.add({_id: 1, host: "nodo02-host:27018"});
rs.add({_id: 2, host: "nodo03-host:27019"});
rs.status()



rs.remove({"nodo02-host:27017"});
rs.remove({"nodo03-host:27017"});






kubectl apply -f nodo03-pvc.yaml

NOTE: clean /data/db/

rs.add({_id: 2, host: "nodo03-host:30002"});

