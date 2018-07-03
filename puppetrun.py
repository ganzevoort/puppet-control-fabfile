from fabric.api import task, parallel, run, sudo
import git

__all__ = []  # don't expose namespace


@task
@parallel
def puppetrun(branch=None, message="locked"):
    if not branch:
        branch = git.Repo().head.ref.name
    username = run('id -nu')
    run('''
        sudo -i puppet agent --enable
        sudo -i puppet agent -t --environment {branch}
        sudo -i puppet agent --disable "{user}: {message} {branch}"
        :
        '''.format(user=username, message=message, branch=branch),
        warn_only=True)

@task
@parallel
def puppetenable():
    run('''
        sudo -i puppet agent --enable
        sudo -i puppet agent -t
        :
        ''',
        warn_only=True)

