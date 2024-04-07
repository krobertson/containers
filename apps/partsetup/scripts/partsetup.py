#!/usr/bin/env python3
#
# coding=utf-8
#

from glob import glob
from logging import getLogger
import logging
import sys
import os
import os.path
import parted
from pathlib import Path
import yaml


class _ConsoleHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()
        self.setFormatter(logging.Formatter("{levelname} - {message}", style="{"))


class Device(object):
    def __init__(self, dev):
        self.givenDev = dev
        self.device = parted.getDevice(dev)
        self.path = self.device.path
        self.logger = getLogger(__name__)

    @property
    def partition_names(self):
        names = glob("{}[0-9]*".format(self.path))
        return names

    def partition(self):
        disk = parted.freshDisk(self.device, "gpt")
        geometry = parted.Geometry(
            device=self.device, start=1, length=self.device.getLength() - 1
        )
        filesystem = parted.FileSystem(type="xfs", geometry=geometry)
        partition = parted.Partition(
            disk=disk, type=parted.PARTITION_NORMAL, fs=filesystem, geometry=geometry
        )
        disk.addPartition(
            partition=partition, constraint=self.device.optimalAlignedConstraint
        )
        partition.setFlag(parted.PARTITION_BOOT)
        disk.commit()

    def format(self):
        for partition in self.partition_names:
            os.system("mkfs.xfs {}".format(partition))

    def mount(self, dest):
        src = self.partition_names[0]
        os.makedirs(dest, exist_ok=True)

        if not os.path.ismount(dest):
            Path(os.path.join(dest, ".not_mounted")).touch()
            self.logger.info("mounting %s to %s", src, dest)
            os.system("mount {} {}".format(src, dest))
        else:
            self.logger.info("filesystem at %s already mounted", dest)

    def wipe_dev(self, dev_path):
        self.logger.debug("wiping %s", dev_path)
        with open(dev_path, "wb") as p:
            p.write(bytearray(1024))

    def wipe(self):
        self.logger.info("wiping partitions and other meta-data")
        for partition in self.partition_names:
            self.wipe_dev(partition)
        self.wipe_dev(self.path)


if __name__ == "__main__":

    # Set up a logger for nice visibility.
    logger = getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(_ConsoleHandler())

    # load config
    cfgFile = "/config/{}.yaml".format(os.environ["NODE_NAME"])
    with open(cfgFile, 'r') as stream:
        data = yaml.safe_load(stream)

    # loop each source
    for source in data["source"].keys():
        for idx, devpath in enumerate(data["source"][source]):
            if not os.path.exists(devpath):
                logger.warning("disk %s not found", devpath)
                continue

            disk = Device(devpath)
            if len(disk.partition_names) == 0:
                logger.info("no partitions on %s, partitioning", disk.path)
                disk.partition()
                disk.format()
            mntname = "-".join((source, "hdd%02d" % (idx+1)))
            mntpath = os.path.join(data["destination"], mntname)
            disk.mount(mntpath)
