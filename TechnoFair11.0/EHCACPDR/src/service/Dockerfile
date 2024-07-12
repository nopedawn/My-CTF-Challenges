FROM python:3.10-slim

RUN apt-get update && apt-get install -y socat

ARG USERNAME=ctf
RUN useradd -m $USERNAME
WORKDIR /home/$USERNAME

COPY chall.py /home/$USERNAME
COPY run.sh /home/$USERNAME

RUN chown root:$USERNAME /home/$USERNAME
RUN chmod -R 755 /home/$USERNAME

USER $USERNAME

CMD ["socat", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:/home/ctf/run.sh"]