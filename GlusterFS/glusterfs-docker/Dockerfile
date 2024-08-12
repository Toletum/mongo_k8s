# Usa una imagen base de Ubuntu
FROM ubuntu:latest

# Instalar GlusterFS y otras dependencias
RUN apt-get update && \
    apt-get install -y glusterfs-server policycoreutils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config

# Exponer los puertos de GlusterFS
EXPOSE 24007 24008 49152

# Configurar el punto de entrada para el contenedor
ENTRYPOINT ["/usr/sbin/glusterd"]
CMD ["-N"]
