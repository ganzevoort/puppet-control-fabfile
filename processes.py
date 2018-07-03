import re
from fabric.api import task, parallel, sudo
from fabric.context_managers import settings, hide, quiet

__all__ = []  # don't expose namespace


@task
@parallel
def port_process(port, action='check'):
    with settings(hide('warnings'), warn_only=True):
        output = sudo("netstat -ntlp | grep ':{port} '".format(port=port))
    pids = re.findall('LISTEN *(\d+)/', output)
    pids = sorted(set(pids), key=int)  # numeric sort, dedup
    if not pids:
        return
    elif action == 'kill':
        sudo('kill {pids}'.format(pids=' '.join(pids)))
    else:
        sudo('ps -lww {pids}'.format(pids=' '.join(pids)))

