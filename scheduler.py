from apscheduler.schedulers.background import BackgroundScheduler
from app.logger import logger

scheduler=BackgroundScheduler()

def job():
    logger.info('Scheduled job executed')

scheduler.add_job(job,'interval',hours=24)
scheduler.start()
