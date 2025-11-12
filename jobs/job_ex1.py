from nautobot.extras.jobs import Job, StringVar

class HelloWorldJob(Job):
    name = "Hello Job"
    description = "Một job đơn giản chỉ in ra thông tin"

    def run(self):
        self.logger.info("Xin chào từ Nautobot! 👋")
        self.logger.debug("Đây là debug message")
        self.logger.warning("Đây là warning message")
