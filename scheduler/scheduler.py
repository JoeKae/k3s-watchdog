"""
Serves a Scheduler generator
"""
import sys

from apscheduler.schedulers.background import BlockingScheduler  # type: ignore
from loguru import logger


class Scheduler:
    """
    Class for the Scheduler
    """
    @staticmethod
    def scheduler_generator() -> BlockingScheduler | None:
        """
        Generates a scheduler instance
        :return: BlockingScheduler instance
        """
        try:
            scheduler = BlockingScheduler(daemon=True)
            return scheduler
        except:
            logger.warning('Scheduler init failed: ' + str(sys.exc_info()[1]))
            return None
