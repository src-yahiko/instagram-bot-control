cd $(realpath $(dirname $0))/../

apt-get update --fix-missing
apt-get install -y python3 pip chromeium-chromedriver
pip install -r ./scripts//python_requirements.txt

