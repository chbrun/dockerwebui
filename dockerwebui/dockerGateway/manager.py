class DockerManager():

    client = None

    def __init__(self, client):
        self.client = client

    def containers(self, all=False, detail=False):
        return self.client.containers(all=all)
