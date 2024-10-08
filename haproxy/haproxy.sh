#!/bin/bash

docker run -d --name haproxy --network host \
-p 27017:27017 -p 27018:27018 -p 27019:27019 -p 8404:8404 \
-v ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro \
haproxy:alpine \
haproxy -f /usr/local/etc/haproxy/haproxy.cfg