docker run -d --name haproxy \
-p 27017:27017 -p 27018:27018 -p 27019:27019 \
-v ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro \
haproxy:alpine \
haproxy -f /usr/local/etc/haproxy/haproxy.cfg
