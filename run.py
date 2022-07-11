import subprocess
from loguru import logger

output = subprocess.check_output(
    "kubectl get pods -n kube-system | grep CrashLoopBackOff",
    shell=True
).decode()
result = {}
for row in output.splitlines():
    if 'CrashLoopBackOff' in row:
        logger.info('restarting k3s service')
        subprocess.call(['service', 'k3s', 'restart'])
        exit(0)

