FROM  steamcmd/steamcmd:debian-trixie

ARG TARGETPLATFORM
ARG VERSION
ARG CHANNEL

SHELL ["/bin/bash", "-e", "-x", "-u", "-c"]

RUN   apt-get update; \
      apt-get install -o APT::Keep-Downloaded-Packages="false" -y \
          ca-certificates curl wget tar unzip xz-utils bzip2 coreutils procps \
          iproute2 iputils-ping socat jq git git-lfs gnupg dbus tini tzdata \
          locales libssl3t64 libcurl4t64 libsqlite3-0 libzstd1 \libsdl2-2.0-0 \
          libsdl1.2debian libfontconfig1 libicu76 python3 xvfb xauth libxi6 \
          libc6 libatomic1 libpulse0 libpulse-mainloop-glib0 liblua5.3-0 \
          libgdiplus gdb libc++1 libc++abi1 libunwind8 libgcc-s1; \
      \
      apt-get clean; \
      rm -rf /var/lib/apt/lists/*;

ENV         USER=gamer
ARG         PUID=1000
ENV         HOME=/games

RUN         useradd -u $PUID -d $HOME -m $USER

USER        $USER
WORKDIR     /games
VOLUME      /games

ENTRYPOINT  ["/usr/bin/tini", "-g", "--"]
