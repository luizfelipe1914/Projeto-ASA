FROM centos:7
RUN yum update -y
RUN yum install openssh-server -y
RUN yum install -y bind bind-utils
RUN yum clean all
WORKDIR /root/.ssh/
COPY id_rsa.pub .
WORKDIR /etc/ssh/
COPY sshd_config .
RUN systemctl restart sshd
RUN systemctl enable sshd
RUN systemctl restart named
EXPOSE 53/udp
EXPOSE 2222/tcp
CMD [ "systemctl", "start", "named" ]