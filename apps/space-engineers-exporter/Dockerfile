FROM python:3.12-slim

ARG TARGETPLATFORM
ARG VERSION
ARG CHANNEL

RUN pip3 install se-exporter

ENV RCON_HOST=localhost \
    RCON_PORT=8766

CMD [ "bash", "-c", "exec se-exporter -h $RCON_HOST -p $RCON_PORT -t $RCON_TOKEN" ]
