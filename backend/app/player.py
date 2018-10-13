class InsufficientResource(Exception):
    pass


class Player:

    def __init__(self, cid, name):
        self.cid = cid
        self.name = name
        self.resources = {}

    @property
    def get_cid(self):
        return self.cid

    @property
    def get_name(self):
        return self.name

    def get_resource(self, resource):
        return self.resources[resource]


    def dec_resource(self, resource, amt):
        self.resources[resource] -= amt

        if resources[resource] < 0:
            resources[resource] += amt
            raise InsufficientResource
        
        return resources[resource]

    def inc_resource(self, resource, amt):
        self.resource[resource] += amt
