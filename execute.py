# ========================================
# Scheduler Jobs
# ========================================
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
import scheduler_jobs
from podcast_app import scrape_castbox

scheduler = BackgroundScheduler()
scheduler.configure(timezone=utc)
# jobs
# scheduler.add_job(scheduler_jobs.podcast_insertion, 'interval', seconds=12)
scheduler.add_job(scrape_castbox.updateStatsList, 'interval', hours=12)
scheduler.start()
