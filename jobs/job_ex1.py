from nautobot.extras.jobs import Job, StringVar

class HelloWorldJob(Job):
    name = "Hello World Job"
    description = "Một Job mẫu chào thế giới"

    your_name = StringVar(
        description="Tên của bạn là gì?",
        default="Quốc Kiên"
    )

    def run(self, data, commit):
        self.log_info(f"Xin chào, {data['your_name']} 👋")
        return "Job chạy thành công!"
