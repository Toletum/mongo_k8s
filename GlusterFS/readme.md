
docker build -t my-glusterfs-server .


docker network create gluster-network
docker volume create gluster-node1-brick
docker volume create gluster-node2-brick
docker volume create gluster-node3-brick

docker run -d --privileged --name gluster-node1 \
--hostname gluster-node1 \
--network gluster-network \
-v gluster-node1-brick:/data/brick1 \
my-glusterfs-server


docker run -d --privileged --name gluster-node2 \
--hostname gluster-node2 \
--network gluster-network \
-v gluster-node2-brick:/data/brick1 \
my-glusterfs-server

docker run -d --privileged --name gluster-node3 \
--hostname gluster-node3 \
--network gluster-network \
-v gluster-node3-brick:/data/brick1 \
my-glusterfs-server



docker exec gluster-node1 gluster peer probe gluster-node2
docker exec gluster-node1 gluster peer probe gluster-node3
docker exec gluster-node1 gluster peer status


docker exec gluster-node1 mkdir -p /data/brick1/brick
docker exec gluster-node2 mkdir -p /data/brick1/brick
docker exec gluster-node3 mkdir -p /data/brick1/brick

gluster volume create gv0 replica 3 \
  gluster-node1:/data/brick1/brick \
  gluster-node2:/data/brick1/brick \
  gluster-node3:/data/brick1/brick



docker run -it --rm --network gluster-network --privileged ubuntu bash

apt-get update
apt-get install -y glusterfs-client fuse
mkdir /mnt/glusterfs

mount -t glusterfs -o tcp glusterfs-gluster-node1-1:/gv0 /mnt/glusterfs
