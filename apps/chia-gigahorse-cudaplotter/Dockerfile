FROM debian:12-slim AS base
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
	ocl-icd-libopencl1 tzdata \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /chia-cuda-plotter

COPY cuda_plot_k32_v3 .

CMD ["sleep", "infinity"]

RUN mkdir -p /etc/OpenCL/vendors && \
    echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
