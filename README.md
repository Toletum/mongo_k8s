# mongo_k8s
Mongodb on k8s

# Create keyfile for replicaset
<code>/usr/bin/openssl rand -base64 741 > keyfile
kubectl create secret generic keyfile --from-file=keyfile=keyfile
rm keyfile</code>

# Up 
<code>kubectl apply -f mongodb-replicaset.yaml</code>

<code>kubectl get pods</code>

waiting all RUNNING

# Setting ReplicaSet
<code>kubectl exec mongodb-0 -c mongodb -- mongosh --eval 'rs.initiate({_id: "rs0", version: 1, members: [ {_id: 0, host: "mongodb-0.mongodb-service.default.svc.cluster.local:27017"}, {_id: 1, host: "mongodb-1.mongodb-service.default.svc.cluster.local:27017"}, {_id: 2, host: "mongodb-2.mongodb-service.default.svc.cluster.local:27017"} ]});'
</code>

# Check status
<code>kubectl exec mongodb-0 -c mongodb -- mongosh --eval 'rs.status();'</code>

# Add user
<code>kubectl exec mongodb-0 -c mongodb -- mongosh --eval 'db.getSiblingDB("admin").createUser({user:"admin",pwd:"admin",roles:[{role:"root",db:"admin"}]});'</code>



# Testing minikube
<code>curl -v http://192.168.49.2:30002</code>
