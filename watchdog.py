"""
Checks for CrashLoopBackOff status in podstatus of kubernetes namespace kube-system
Restarts the service if found
"""
import subprocess
from datetime import datetime

from loguru import logger

from scheduler import scheduler


class WatchDog:
    """
    Watchdog class
    """

    @staticmethod
    def check():
        """
        Checks for crashed pods in kube-system
        """
        try:
            output = subprocess.check_output(
                "kubectl get pods -n kube-system | grep CrashLoopBackOff",
                shell=True
            ).decode()
        except subprocess.CalledProcessError:
            return

        for row in output.splitlines():
            if 'CrashLoopBackOff' in row:
                WatchDog.restart_k3s()
                break

    @staticmethod
    def restart_k3s():
        """
        Restarts the k3s service
        """
        logger.info('restarting k3s service')
        subprocess.call(['sudo', 'systemctl', 'restart', 'k3s'])

    @staticmethod
    def run():
        """
        Starts a scheduled watchdog loop
        """
        task_scheduler = scheduler.Scheduler().scheduler_generator()
        task_scheduler.add_job(
            WatchDog.check,
            'interval',
            seconds=300,
            next_run_time=datetime.now()
        )


WatchDog.run()
