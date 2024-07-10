FROM ubuntu:latest

RUN apt update && apt install openssh-server sudo -y

ARG USERNAME=leus
ARG GROUP=groupleus
RUN groupadd $GROUP && \
    useradd -ms /bin/rbash -g $GROUP $USERNAME && \
    usermod -aG sudo $USERNAME

RUN mkdir -p /home/$USERNAME/.ssh
COPY id_rsa.pub /home/$USERNAME/.ssh/authorized_keys

COPY flag.txt /home/$USERNAME/

RUN chown -R $USERNAME:$GROUP /home/$USERNAME && \
    chmod 500 /home/$USERNAME && \
    chmod 400 /home/$USERNAME/.ssh/authorized_keys && \
    chmod 500 /home/$USERNAME/.ssh && \
    chmod 400 /home/$USERNAME/flag.txt

RUN echo "export PATH=/usr/bin:/bin:/usr/sbin:/sbin" > /home/$USERNAME/.bashrc && \
    echo "set +h" >> /home/$USERNAME/.bashrc && \
    echo "unset HISTFILE" >> /home/$USERNAME/.bashrc && \
    echo "PS1='\u@\h:\w\$ '" >> /home/$USERNAME/.bashrc && \
    echo "alias ls='ls --color=auto'" >> /home/$USERNAME/.bashrc && \
    echo "function ls { if [ $# -eq 0 ]; then command ls --color=auto; else echo 'ls command with options is disabled'; fi; }" >> /home/$USERNAME/.bashrc && \
    echo "alias chmod='echo chmod command is disabled'" >> /home/$USERNAME/.bashrc && \
    echo "alias cat='echo cat command is disabled'" >> /home/$USERNAME/.bashrc && \
    echo "set -r" >> /home/$USERNAME/.bashrc

RUN service ssh start

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
