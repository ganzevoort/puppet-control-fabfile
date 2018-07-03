import re
from fabric.api import task, parallel, sudo
from fabric.context_managers import settings, hide

__all__ = []  # don't expose namespace


CHAINS = ('INPUT', 'OUTPUT')
DROP_RULE = "{chain} -j DROP -p tcp --dport {port}"


@task
@parallel
def fwblock(*ports):
    for port in ports:
        for chain in CHAINS:
            sudo("iptables -A " + DROP_RULE.format(port=port, chain=chain))

@task
@parallel
def fwunblock(*ports):
    for port in ports:
        for chain in CHAINS:
            sudo("iptables -D " + DROP_RULE.format(port=port, chain=chain))

@task
def fwstatus():
    sudo('iptables -vnL')

@task
@parallel
def fwflush():
    sudo('iptables -F')

