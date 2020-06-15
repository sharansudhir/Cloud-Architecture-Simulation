
import ResourcePool
import random
from concurrent.futures import ThreadPoolExecutor


def service_request(client, type_of_user, resources_required):
    auto_scale_listener = AutoScaler(resources_required, type_of_user)
    auto_scale_listener.scale_process()

    RequestLoadBalancer().request_complete(client, type_of_user, resources_required)


def singleton(cls):
    obj = cls()
    cls.__new__ = staticmethod(lambda cls: obj)
    try:
        del cls.__init__
    except AttributeError:
        pass
    return cls


@singleton
class RequestLoadBalancer:


    def __init__(self):
        self.list = []
        self.resource_final = {1:[], 2:[], 3:[]}
        self.pool_Data = ResourcePool.ResourceAllocation(50, 30, 20)

    def service(self, client, type_of_user):
        resources_required = random.randint(1, type_of_user*15+1)

        print("Resources Allocated:", resources_required)
        self.pool_Data.get_resources_for_user(resources_required, type_of_user)

        self.list.append(client)

        service_request(client, type_of_user, resources_required)


    def request_complete(self, client, type_of_user, resources_used):
        self.list.remove(client)
        self.resource_final[type_of_user].append(self.pool_Data.no_of_resources_allocated(type_of_user))
        self.pool_Data.release_resources_of_user(resources_used, type_of_user)
        print("Task Executed")


class AutoScaler:
    def __init__(self, resources_required, type_of_user):
        self.resources_required = resources_required
        self.type_of_user = type_of_user

    def scale_process(self):
        executor = ThreadPoolExecutor(max_workers=self.resources_required)
        if self.type_of_user == 3:
            print("Scaling done for Paid User")
            task = TaskExecution(self.resources_required)

            executor.submit(task.execute())
        elif self.type_of_user == 2:
            print("Partially Paid User, Scaling not Available yet")
            partial_task = TaskExecution(1)
            if partial_task.complete(60):
                print("Task Completed : 60%, Scaling done")
                finish_task = TaskExecution(self.resources_required-1)

                executor.submit(finish_task.execute())
        else:
            if self.resources_required > 1:
                print("No Scaling for Free User")
            else:
                print("No Scaling for Free Users")
                task = TaskExecution(self.resources_required)

                executor.submit(task.execute())

class TaskExecution:
    def __init__(self, resources_count):
        self.resources_count = resources_count

    def execute(self, percent_complete=100):
        for i in range(self.resources_count):
            for t in range(round(percent_complete/self.resources_count)):
                if t+1 == percent_complete:
                    return True

    def complete(self, complete):
        return self.execute(complete)

