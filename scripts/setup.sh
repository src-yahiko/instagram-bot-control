#!/bin/sh
# This script prepares everything to run the application on linux

venvPath=.venvApp

cd $(realpath $(dirname $0))/../

echo "Install packets..."
apt-get update --fix-missing
apt-get install -y python3 python3-venv pip
apt-get install -y ffmpeg

echo "Set up python venv..."
python3 -m venv $venvPath
source $venvPath/bin/activate

echo "Install python requirements..."
pip install -r ./scripts/python_requirements.txt

