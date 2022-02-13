Role Name
=========

Example bootstrap role.

Role Variables
--------------

See `defaults/main.yml`

| Variable | Default | Description |
|----------|---------|-------------|
| `bootstrap_apt_packages` | `jq, vim, python3-pip` | list of apt packages for installing |
| `bootstrap_timezone` | `Asia/Dubai` | host timezone |
| `bootstrap_hostname` | `{{ inventory_hostname }}` | host FQDN |
| `bootstrap_ntp_install` | `true` | NTP service installation and configuration flag |
| `bootstrap_ntp_servers` | Ubuntu NTP servers | list of NTP servers |

> Using NTP is only available in version 1.0.1 or higher.


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
      - rfc2_bootstrap
```

License
-------

MIT

Author Information
------------------

akimrx
