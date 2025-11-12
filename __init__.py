from nautobot.extras.jobs import register_jobs
from .job_ex1 import HelloWorldJob

register_jobs(HelloWorldJob)
