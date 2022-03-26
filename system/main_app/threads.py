import threading
import time
from datetime import datetime
from random import randint

from main_app.models import Job
from main_app.web_scraper import fetch_job_details, fetch_jobs, prepare_soup


class ScrapeThread(threading.Thread):

    def __init__(self):
        self.url = "https://www.brightermonday.co.ke/jobs"
        threading.Thread.__init__(self)

    def run(self):
        page = 1
        while True:
            current_url = self.url + f'?page={page}'
            print(current_url)
            page += 1
            job_data = []
            job_urls = fetch_jobs(current_url)[0]
            total_pages = int(fetch_jobs(current_url)[1])
            for job_url in job_urls:
                soup = prepare_soup(job_url)
                if soup != None:
                    job_details = fetch_job_details(soup, job_url)
                    job_data.append(job_details)
                else:
                    break
            job_instances = [
                Job(scrap_date=datetime.today(),
                    title=job['title'],
                    location=job['location'],
                    function=job['function'],
                    industry=job['industry'],
                    description=job['description'],
                    qualifications=job['qualifications'],
                    hyperlink=job['hyperlink']) for job in job_data
            ]
            Job.objects.bulk_create(job_instances)
            print("Created %s Jobs!" % (len(job_instances) * (page - 1)))
            if page <= total_pages:
                time.sleep(randint(1, 5))
            else:
                break
