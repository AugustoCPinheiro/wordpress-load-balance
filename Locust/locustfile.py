from locust import TaskSet, task, HttpLocust

class ConverterTasks(TaskSet):
#    @task
#    def request_page(self):
#        self.client.get("/2019/10/31/texto-400kb")

    @task
    def request_page(self):
       self.client.get("/2019/10/31/20kb-e-imagem")


class ApiUser(HttpLocust):
    task_set = ConverterTasks