/etc/hosts

192.168.49.2 nodo01-host
192.168.49.2 nodo02-host
192.168.49.2 nodo03-host




kubectl apply -f myrs.yaml

kubectl apply -f nodo01.yaml

kubectl exec -ti nodo01 -c nodo01 -- mongosh --username admin --password admin --authenticationDatabase admin

kubectl exec -ti nodo01 -c nodo01 -- mongosh

db.getSiblingDB("admin").createUser({user:"admin",pwd:"admin",roles:[{role:"root",db:"admin"}]});

kubectl exec -ti nodo01 -c nodo01 -- mongosh -u admin -p admin

rs.reconfig({_id: "rs0", version: 1, members: [ {_id: 0, host: "nodo01-host:27017"} ]});

rs.status()


kubectl apply -f nodo02.yaml

rs.add({_id: 1, host: "nodo02-host:30001"});


kubectl apply -f nodo03.yaml
rs.add({_id: 2, host: "nodo03-host:30002"});

