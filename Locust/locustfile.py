from locust import TaskSet, task, HttpLocust

class ConverterTasks(TaskSet):
    @task
    def request_page(self):
        self.client.get("/2019/10/27/imagem-300-kb-com-texto-20-kb/")


class ApiUser(HttpLocust):
    task_set = ConverterTasks