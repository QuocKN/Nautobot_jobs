from nautobot.extras.jobs import Job, StringVar

class HelloWorld(Job):
    name = "Hello World"

    your_name = StringVar(
        description="Tên của bạn là gì?",
        default="Quốc Kiên"
    )

    def run(self, data, commit):
        self.log_info(f"Xin chào, {data['your_name']} 👋")
        return "Job chạy thành công!"
