from nautobot.extras.jobs import register_jobs
from .job_ex1 import HelloWorldJob

# Bắt buộc phải gọi register_jobs để Nautobot load Job
register_jobs(HelloWorldJob)

