FROM nvcr.io/nvidia/cuda:12.1.0-base-ubuntu22.04 AS base

ARG TARGETPLATFORM
ARG VERSION
ARG CHANNEL

RUN apt-get update \
	&& apt-get install -y wget \
	&& rm -rf /var/lib/apt/lists/*

RUN wget -O /usr/bin/yq https://github.com/mikefarah/yq/releases/download/v4.43.1/yq_linux_amd64 \
	&& chmod a+x /usr/bin/yq

CMD ["nvidia_gpu_exporter"]
COPY ./apps/nvidia-gpu-exporter/setpowerlimit.sh .

RUN wget https://github.com/utkuozdemir/nvidia_gpu_exporter/releases/download/v${VERSION}/nvidia_gpu_exporter_${VERSION}_linux_x86_64.tar.gz \
 	&& tar -xvzf nvidia_gpu_exporter_${VERSION}_linux_x86_64.tar.gz \
	&& mv nvidia_gpu_exporter /usr/bin/
