from nautobot.extras.jobs import Job, StringVar

class HelloWorldJob(Job):
    name = "Hello Job"
    description = "Một job đơn giản chỉ in ra thông tin"

    def run(self):
        self.log_info("Xin chào từ Nautobot! 👋")
