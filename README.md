Role Name
=========

Example bootstrap role.

Role Variables
--------------

See `defaults/main.yml`

* `bootstrap_apt_packages` - list of apt packages for installing
* `bootstrap_timezone` - host TZ, example `Europe/Moscow`
* `bootstrap_hostname` - host FQDN, default `{{ inventory_hostname }}`


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
