# mongo_k8s
Mongodb on k8s

# Create keyfile for replicaset
/usr/bin/openssl rand -base64 741 > keyfile
kubectl create secret generic keyfile --from-file=keyfile=keyfile
rm keyfile

# Up 
kubectl apply -f mongodb-replicaset.yaml

kubectl get pods

waiting all RUNNING

# Setting ReplicaSet
<code>
kubectl exec mongodb-0 -c mongodb -- mongosh --eval 'rs.initiate({_id: "rs0", version: 1, members: [ {_id: 0, host: "mongodb-0.mongodb-service.default.svc.cluster.local:27017"}, {_id: 1, host: "mongodb-1.mongodb-service.default.svc.cluster.local:27017"}, {_id: 2, host: "mongodb-2.mongodb-service.default.svc.cluster.local:27017"} ]});'
</code>

# Check status
kubectl exec mongodb-0 -c mongodb -- mongosh --eval 'rs.status();'

# Add user
kubectl exec mongodb-0 -c mongodb -- mongosh --eval 'db.getSiblingDB("admin").createUser({user:"admin",pwd:"admin",roles:[{role:"root",db:"admin"}]});'



# Testing minikube
curl -v http://192.168.49.2:30002
