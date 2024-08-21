#!/bin/bash

sudo apt-get clean

sudo apt-get autoclean

sudo rm -rf /var/cache/apt/archives/*

sudo rm -rf /var/cache/apt/archives/partial/

sudo rm -rf /tmp/*

rm -rf ~/.cache/*

sudo journalctl --vacuum-time=0.1weeks