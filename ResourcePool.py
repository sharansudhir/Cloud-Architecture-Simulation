
class ResourceAllocation:
    def __init__(self, paid_resources, hybrid_resources, free_resources):
        self.paid_resources = paid_resources
        self.hybrid_resources = hybrid_resources
        self.free_resources = free_resources

    def no_of_resources_allocated(self, user_type):

        if(user_type == 3):
            return self.paid_resources
        elif(user_type == 2):
            return self.hybrid_resources
        elif(user_type == 1):
            return self.free_resources

    def get_resources_for_user(self, num, user_type):
        if(user_type == 3):
            self.paid_resources = self.paid_resources - num
        elif(user_type == 2):
            self.hybrid_resources =self.hybrid_resources - num
        elif(user_type == 1):
            self.free_resources =self.free_resources - num

    def release_resources_of_user(self, num, user_type):
        if(user_type == 3):
            self.paid_resources =self.paid_resources + num
        elif(user_type == 2):
            self.hybrid_resources = self.hybrid_resources + num
        elif(user_type == 1):
            self.free_resources =self.free_resources + num



