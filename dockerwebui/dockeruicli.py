import cmd2
from termcolor import colored
from dockerGateway.manager import DockerManager
from dockerwebuicfg import DOCKER_URI
from docker import Client

class DockerUICli(cmd2.Cmd):

    client = None
    containersId = None

    def __init__(self, client):
        self.client = client
        cmd2.Cmd.__init__(self)

    def do_containers(self, line):
        color='red'
        listContainers = self.client.containers(all=True)
        for container in listContainers:
            if 'Exited' in container['Status']:
                color='red'
            else:
                color='green'
            print(colored('{:>10} {:>50} {:<30}'.format(container['Id'][:10],container['Names'][0], container['Status']), color))


if __name__ == '__main__':
    console = DockerUICli(DockerManager(Client(DOCKER_URI)))
    console.cmdloop()
