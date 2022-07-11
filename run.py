"""
Checks for CrashLoopBackOff status in podstatus of kubernetes namespace kube-system
Restarts the service if found
"""
import subprocess
import sys

from loguru import logger

try:
    OUTPUT = subprocess.check_output(
        "kubectl get pods -n kube-system | grep CrashLoopBackOff",
        shell=True
    ).decode()
except subprocess.CalledProcessError:
    sys.exit(0)

for row in OUTPUT.splitlines():
    if 'CrashLoopBackOff' in row:
        logger.info('restarting k3s service')
        subprocess.call(['sudo', 'systemctl', 'restart',  'k3s'])
        sys.exit(0)
