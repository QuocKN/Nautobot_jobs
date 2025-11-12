from nautobot.extras.jobs import Job, StringVar

class HelloWorldJob(Job):
    name = "Hello World Job"

    your_name = StringVar(
        description="Tên của bạn là gì?",
        default="Quốc Kiên"
    )

    def run(self, data, commit):
        # Lấy giá trị từ data dict
        name_value = data["your_name"]
        self.log_info(f"Xin chào, {name_value} 👋")
        return "Job chạy thành công!"
