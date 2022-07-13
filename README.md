# k3s-watchdog
Checks for crashed pods in kube-system and restarts service.

To use it just run it as a service or call it as a cronjob.

### create venv
```commandline
wget -qO - https://raw.githubusercontent.com/JoeKae/sh-python-installer/main/python.sh | sudo bash -s 3.10.0
python -m venv --without-pip ./venv

. ./venv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

sudo cp k3s-watchdog.service /etc/systemd/system
sudo nano /etc/systemd/system/k3s-watchdog.service

-> ExecStart= ...

sudo systemctl daemon-reload
sudo systemctl enable k3s-watchdog.service
sudo systemctl start k3s-watchdog.service
systemctl status k3s-watchdog.service
```