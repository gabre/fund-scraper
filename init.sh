echo "Downloading gecko."
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar -xvzf geckodriver*tar.gz
chmod +x geckodriver
PATH=$PATH:.
