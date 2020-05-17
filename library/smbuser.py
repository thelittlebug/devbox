#!/usr/bin/python

from ansible.module_utils.basic import *

def main():
    changed = False

    m = AnsibleModule(argument_spec={
        "user":{"type":"str"},
        "password":{"type":"str","no_log":True}
    })

    cmd = 'pdbedit -L'
    rc, stdout, stderr = m.run_command(cmd)
    if rc != 0:
        m.fail_json(msg="%s failed" % cmd, stdout=stdout, sstderr=stderr)
    
    if m.params['user'] not in [x.split(':')[0] for x in stdout.splitlines()]:
        changed = True
        r = {"user": "created"}
    else:
        r = {"user": "not created"}

    m.exit_json(changed=changed, meta=r)

if __name__ == '__main__':
    main()
