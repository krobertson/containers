FROM  ghcr.io/krobertson/gameserver-base:2026.02.16

USER  "root"

# Install Wine
ARG   WINE_DIST="trixie"
ARG   WINE_BRANCH="stable"

RUN   apt-get update; \
      apt-get install -o APT::Keep-Downloaded-Packages="false" -y --no-install-recommends \
          cabextract winbind; \
      \
      install -d -m 0755 /etc/apt/keyrings; \
      wget -qO- https://dl.winehq.org/wine-builds/winehq.key | gpg --dearmor -o /etc/apt/keyrings/winehq-archive.key -; \
      wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/${WINE_DIST}/winehq-${WINE_DIST}.sources; \
      \
      apt-get update; \
      apt-get install -o APT::Keep-Downloaded-Packages="false" -y --install-recommends \
          winehq-${WINE_BRANCH} winetricks; \
      \
      apt-get clean; \
      rm -rf /var/lib/apt/lists/*;

ADD   --chmod=0755 ./apps/gameserver-wine-stable/setupwinetricks.sh /usr/local/bin

ENV  XDG_RUNTIME_DIR="/tmp" \
     WINEPREFIX="/games/.wine" \
     WINEARCH="win64" \
     WINEDEBUG="-all"

USER $USER
