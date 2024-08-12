
docker build -t my-glusterfs-server .


docker exec gluster-node1 gluster peer probe gluster-node2
docker exec gluster-node1 gluster peer probe gluster-node3
docker exec gluster-node1 gluster peer status


docker exec gluster-node1 mkdir -p /data/brick1/brick
docker exec gluster-node2 mkdir -p /data/brick1/brick
docker exec gluster-node3 mkdir -p /data/brick1/brick

docker exec gluster-node1 gluster volume create gv0 replica 3 \
  gluster-node1:/data/brick1/brick \
  gluster-node2:/data/brick1/brick \
  gluster-node3:/data/brick1/brick


docker exec gluster-node1 gluster volume start gv0
docker exec gluster-node1 gluster volume set gv0 performance.cache-size 1GB
docker exec gluster-node1 gluster volume status
docker exec gluster-node1 gluster volume info

192.168.100.2 gluster-node1
192.168.100.3 gluster-node2
192.168.100.4 gluster-node3


apt-get update
apt-get install -y glusterfs-client fuse

sudo mkdir /mnt/glusterfs/gv0/
sudo mount -t glusterfs -o tcp glusterfs-gluster-node1-1:/gv0 /mnt/glusterfs/gv0/


docker volume create --driver local \
  --opt type=none \
  --opt device=/mnt/glusterfs/gv0/ \
  --opt o=bind glusterfs-volume

docker run -ti --rm -v glusterfs-volume:/data ubuntu bash
