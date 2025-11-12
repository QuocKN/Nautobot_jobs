from nautobot.extras.jobs import register_jobs
from .hello_world import HelloWorldJob

# Bắt buộc phải gọi register_jobs để Nautobot load Job
register_jobs(HelloWorldJob)
