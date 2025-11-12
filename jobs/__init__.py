from nautobot.core.celery import register_jobs

from .job_ex1 import HelloWorldJob
from .job_ex2 import HelloWorld

register_jobs(HelloWorldJob, HelloWorld)

