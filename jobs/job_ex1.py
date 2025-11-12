from nautobot.extras.jobs import Job, StringVar

class HelloWorldJob(Job):
    name = "Hello World Job"

    your_name = StringVar(
        description="Tên của bạn là gì?",
        default="Quốc Kiên"
    )

    def run(self, data, commit):
        return "Job chạy thành công!"
