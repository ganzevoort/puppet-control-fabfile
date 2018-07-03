# puppet-control-fabfile

Available commands
------------------

- `fwblock`
- `fwflush`
- `fwstatus`
- `fwunblock`
- `port_process`
- `puppetenable`
- `puppetrun`

Example usage
-------------
```fab -H tst fwblock:9200,9300 fwstatus```
Block 2 ports on all `tst` servers (see hostgroups.yaml) and show result.
The fwblock, fwflush, fwstatus, fwunblock scripts use `iptables`.

```fab port_process:9200```
```fab port_process:9200,action=kill```
Show or kill the processes listening on that port.

```fab puppetrun```
Runs `puppet agent -t --environment $currentbranch`, convenient if you're working
on some branch of the puppet configuration tree and your puppet master is
setup to provide branches as environments.

Runs `puppet agent -t disable` to prevent automatic switch back to `production`.

```fab puppetenable```
Switches back to default environment.
