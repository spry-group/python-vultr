Vultr
=====
.. image:: https://travis-ci.org/spry-group/python-vultr.svg?branch=master
    :target: https://travis-ci.org/spry-group/python-vultr
    
Vultr provides a client library to the Vultr.com API.

**Usage**


    api_key = 'XXXXXXXXX'

    vultr = Vultr(api_key)

    plans_json = vultr.plans_list()


**Support**


Python Vultr is supported on a volunteer basis. 

* `Open an Issue <https://github.com/spry-group/python-vultr/issues/new>`_

* .. image:: https://badges.gitter.im/Join%20Chat.svg
      :target: https://gitter.im/spry-group/python-vultr


**API**


* def __init__(self, api_key):
* def snapshot_list(self):
* def snapshot_destroy(self, snapshotid):
* def snapshot_create(self, subid):
* def iso_list(self):
* def plans_list(self):
* def regions_list(self):
* def regions_availability(self, dcid):
* def startupscript_list(self):
* def startupscript_destroy(self, scriptid):
* def startupscript_create(self, name, script):
* def startupscript_update(self, scriptid, name, script):
* def dns_list(self):
* def dns_records(self, domain):
* def dns_create_domain(self, domain, serverip):
* def dns_delete_domain(self, domain):
* def dns_delete_record(self, domain, recordid):
* def dns_create_record(self, domain, name, type, data, ttl=None,
* def sshkey_list(self):
* def sshkey_destroy(self, sshkeyid):
* def sshkey_create(self):
* def sshkey_update(self, sshkeyid, name=None, ssh_key=None):
* def backup_list(self):
* def server_list(self, subid):
* def server_bandwidth(self):
* def server_reboot(self):
* def server_halt(self):
* def server_start(self):
* def server_destroy(self):
* def server_reinstall(self):
* def server_restore_snapshot(self, subid, snapshotid):
* def server_restore_backup(self, subid, backupid):
* def server_create(self, dcid, vpsplanid, osid, ipxe_chain_url=None,
* def server_list_ipv4(self, subid):
* def server_reverse_set_ipv4(self):
* def server_reverse_default_ipv4(self, subid, ip):
* def server_list_ipv6(self):
* def server_reverse_list_ipv6(self):
* def server_reverse_set_ipv6(self, subid, ip, entry):
* def server_reverse_delete_ipv6(self, subid, ip):
* def server_label_set(self, subid, label):
* def server_create_ipv4(self, subid, reboot):
* def server_destroy_ipv4(self, subid, ip):
* def server_os_change_list(self):
* def server_os_change(self, subid, osid):
* def server_upgrade_plan_list(self):
* def server_upgrade_plan(self, subid, vpsplanid):
* def app_list(self):
* def account_info(self):
* def os_list(self):
* def request(self, path, params={}, method='GET'):
