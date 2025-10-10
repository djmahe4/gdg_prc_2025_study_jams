pkg update && pkg upgrade
pkg install git wget curl python openssh zip unzip
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-arm.tar.gz
tar -xf google-cloud-cli-linux-arm.tar.gz
./google-cloud-sdk/install.sh
source ./google-cloud-sdk/path.bash.inc
gcloud init
gcloud auth login
