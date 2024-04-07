FROM debian:12-slim AS base

ARG TARGETPLATFORM
ARG VERSION
ARG CHANNEL

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
	vim-tiny python3-parted udev xfsprogs python3-yaml \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

CMD ["/app/partsetup.py" ]

COPY ./apps/partsetup/scripts/partsetup.py .
