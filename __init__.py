from fabric.api import env

from .hostgroups import gethosts
from .puppetrun import puppetrun, puppetenable
from .processes import port_process
from .firewall import fwblock, fwunblock, fwstatus, fwflush


env.forward_agent = True
env.always_use_pty = True
env.linewise = True
env.shell = '/bin/bash -c'
env.use_ssh_config = True

env.hosts = list(gethosts(env.hosts or ['dev']))

