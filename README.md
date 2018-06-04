# Vultr

[![build status](https://travis-ci.org/spry-group/python-vultr.svg?branch=master)](https://travis-ci.org/spry-group/python-vultr)

Vultr provides a client library to the [Vultr.com](http://www.vultr.com/?ref=6989379-3B) API.

## Usage

```python
api_key = 'XXXXXXXXX'
vultr = Vultr(api_key)
plans_json = vultr.plans.list()
```

## Testing

From the repo root directory
Performs generic, unauthenticated tests
    
```shell
python -m unittest -v tests.test_vultr.UnauthenticatedTests
```

Requires the environment variable VULTR_KEY to be set

```shell
python -m unittest -v tests.test_vultr.AuthenticatedTests
```

## Support

Python Vultr is supported on a volunteer basis.

* [Open an Issue](https://github.com/spry-group/python-vultr/issues/new)
* [![Gitter.im](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/spry-group/python-vultr)


## API

* def account.info(self, params=None):
* def app.list(self, params=None):
* def backup.list(self, params=None):
* def dns.create_domain(self, domain, ipaddr, params=None):
* def dns.create_record(self, domain, name, _type, data, params=None):
* def dns.delete_domain(self, domain, params=None):
* def dns.delete_record(self, domain, recordid, params=None):
* def dns.list(self, params=None):
* def dns.records(self, domain, params=None):
* def dns.update_record(self, domain, recordid, params=None):
* def iso.list(self, params=None):
* def iso.create_from_url(self, url, params=None)
* def os.list(self, params=None):
* def plans.list(self, params=None):
* def regions.availability(self, dcid, params=None):
* def regions.list(self, params=None):
* def server.ipv4.create(self, subid, params=None):
* def server.ipv4.destroy(self, subid, ipaddr, params=None):
* def server.ipv4.list(self, subid, params=None):
* def server.ipv4.reverse_default(self, subid, ipaddr, params=None):
* def server.ipv4.reverse_set(self, subid, ipaddr, entry, params=None):
* def server.ipv6.list_ipv6(self, subid, params=None):
* def server.ipv6.reverse_delete_ipv6(self, subid, ipaddr, params=None):
* def server.ipv6.reverse_list_ipv6(self, subid, params=None):
* def server.ipv6.reverse_set_ipv6(self, subid, ipaddr, entry, params=None):
* def server.bandwidth(self, subid, params=None):
* def server.create(self, dcid, vpsplanid, osid, params=None):
* def server.destroy(self, subid, params=None):
* def server.get_user_data(self, subid, params=None):
* def server.halt(self, subid, params=None):
* def server.label_set(self, subid, label, params=None):
* def server.list(self, subid=None, params=None):
* def server.neighbors(self, subid, params=None):
* def server.os_change(self, subid, osid, params=None):
* def server.os_change_list(self, subid, params=None):
* def server.reboot(self, subid, params=None):
* def server.reinstall(self, subid, params=None):
* def server.restore_backup(self, subid, backupid, params=None):
* def server.restore_snapshot(self, subid, snapshotid, params=None):
* def server.set_user_data(self, subid, userdata, params=None):
* def server.start(self, subid, params=None):
* def server.upgrade_plan(self, subid, vpsplanid, params=None):
* def server.upgrade_plan_list(self, subid, params=None):
* def snapshot.create(self, subid, params=None):
* def snapshot.destroy(self, snapshotid, params=None):
* def snapshot.list(self, params=None):
* def sshkey.create(self, name, ssh_key, params=None):
* def sshkey.destroy(self, sshkeyid, params=None):
* def sshkey.list(self, params=None):
* def sshkey.update(self, sshkeyid, params=None):
* def startupscript.create(self, name, script, params=None):
* def startupscript.destroy(self, scriptid, params=None):
* def startupscript.list(self, params=None):
* def startupscript.update(self, scriptid, params=None):
