#!/bin/bash
sudo docker build -t amalnuaimi:sensibo .
sudo rm -r out
sudo docker run --rm -v ${PWD}:/local  amalnuaimi:sensibo generate -i sensibo.openapi.yaml -g python -o /local/out/python
sudo /home/abdulla/anaconda3/envs/dev/bin/python -m pip install ./out/python