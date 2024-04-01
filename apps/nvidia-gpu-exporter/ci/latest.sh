#!/usr/bin/env bash
channel=$1
version=$(curl -sX GET "https://api.github.com/repos/utkuozdemir/nvidia_gpu_exporter/releases" | jq --raw-output '.[0].tag_name' 2>/dev/null)
printf "%s" "${version:1}"