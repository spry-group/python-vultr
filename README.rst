Vultr
=====
.. image:: https://travis-ci.org/spry-group/python-vultr.svg?branch=master
    :target: https://travis-ci.org/spry-group/python-vultr

Vultr provides a client library to the Vultr.com API.

**Usage**

.. code:: python

    api_key = 'XXXXXXXXX'
    vultr = Vultr(api_key)
    plans_json = vultr.plans.list()



**Testing**

    From the repo root directory
    Performs generic, unauthenticated tests
    
.. code:: shell
    
    python -m unittest -v tests.test_vultr.UnauthenticatedTests


Requires the environment variable VULTR_KEY to be set

.. code:: shell

    python -m unittest -v tests.test_vultr.AuthenticatedTests


**Support**


Python Vultr is supported on a volunteer basis.

* `Open an Issue <https://github.com/spry-group/python-vultr/issues/new>`_

* .. image:: https://badges.gitter.im/Join%20Chat.svg
      :target: https://gitter.im/spry-group/python-vultr


**API**


* def __init__(self, api_key):
* def snapshot.list(self):
* def snapshot.destroy(self, snapshotid):
* def snapshot.create(self, subid):
* def iso.list(self):
* def plans.list(self):
* def regions.list(self):
* def regions.availability(self, dcid):
* def startupscript.list(self):
* def startupscript.destroy(self, scriptid):
* def startupscript.create(self, name, script):
* def startupscript.update(self, scriptid, name, script):
* def dns.list(self):
* def dns.records(self, domain):
* def dns.create_domain(self, domain, serverip):
* def dns.delete_domain(self, domain):
* def dns.delete_record(self, domain, recordid):
* def dns.create_record(self, domain, name, type, data, ttl=None,
* def sshkey.list(self):
* def sshkey.destroy(self, sshkeyid):
* def sshkey.create(self):
* def sshkey.update(self, sshkeyid, name=None, ssh_key=None):
* def backup.list(self):
* def server.list(self, subid):
* def server.bandwidth(self):
* def server.reboot(self):
* def server.halt(self):
* def server.start(self):
* def server.destroy(self):
* def server.reinstall(self):
* def server.restore_snapshot(self, subid, snapshotid):
* def server.restore_backup(self, subid, backupid):
* def server.create(self, dcid, vpsplanid, osid, ipxe_chain_url=None,
* def server.list_ipv4(self, subid):
* def server.reverse_set_ipv4(self):
* def server.reverse_default_ipv4(self, subid, ip):
* def server.list_ipv6(self):
* def server.reverse_list_ipv6(self):
* def server.reverse_set_ipv6(self, subid, ip, entry):
* def server.reverse_delete_ipv6(self, subid, ip):
* def server.label_set(self, subid, label):
* def server.create_ipv4(self, subid, reboot):
* def server.destroy_ipv4(self, subid, ip):
* def server.os_change_list(self):
* def server.os_change(self, subid, osid):
* def server.upgrade_plan_list(self):
* def server.upgrade_plan(self, subid, vpsplanid):
* def app.list(self):
* def account.info(self):
* def os.list(self):
* def request(self, path, params={}, method='GET'):
