import os
import yaml


yamlfile = os.path.join(os.path.dirname(__file__), 'hostgroups.yaml')
hostgroups = yaml.load(file(yamlfile))

def gethosts(hosts):
    for host in hosts:
        if host in hostgroups:
            for host in gethosts(hostgroups[host]):
                yield host
        else:
            yield host

