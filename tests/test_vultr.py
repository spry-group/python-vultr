'''Tests for the Vultr cloud API client library'''
import unittest
import os
from time import sleep
import warnings
import pprint
from vultr import Vultr, VultrError

VULTR_TEST_LABEL = 'python-vultr: test'


class UnauthenticatedTests(unittest.TestCase):
    '''Tests without authentication (no VULTR_KEY)'''
    def setUp(self):
        self.vultr = Vultr('')

    def test_plans_list(self):
        '''List plans'''
        self.vultr.plans.list()

    def test_regions_list(self):
        '''List regions'''
        self.vultr.regions.list()

    def test_os_list(self):
        '''List operating systems'''
        self.vultr.os.list()

    def test_app_list(self):
        '''List applications'''
        self.vultr.app.list()


@unittest.skipIf(not os.environ.get('VULTR_KEY'),
                 'Skipping AuthenticatedTests')
class AuthenticatedTests(unittest.TestCase):
    '''Tests with authentication (VULTR_KEY)'''
    @classmethod
    def setUpClass(cls):
        cls.VULTR_KEY = os.environ.get('VULTR_KEY')
        cls.vultr = Vultr(cls.VULTR_KEY)
        cls.server_list = {}

    def test_backup_list(self):
        '''List backups'''
        self.vultr.backup.list()

    def test_dns_list(self):
        '''List DNS records'''
        self.vultr.dns.list()

    def test_firewall_group_list(self):
        '''List firewall groups'''
        self.vultr.firewall.group_list()

    def test_iso_list(self):
        '''List ISOs / images'''
        self.vultr.iso.list()

    def test_snapshot_list(self):
        '''List snapshots'''
        self.vultr.snapshot.list()

    def test_sshkey_list(self):
        '''List SSH public keys'''
        self.vultr.sshkey.list()

    def test_startupscript_list(self):
        '''List startup scripts'''
        self.vultr.startupscript.list()

    def test_label_set(self):
        '''Set an instance label'''
        try:
            self.vultr.server.label_set('', '')
        except VultrError as ex:
            msg = str(ex)
            self.assertEqual(
                msg,
                'Request failed. Check the response body '
                'for a more detailed description. Body: '
                '\nInvalid server.  Check SUBID value and '
                'ensure your API key matches the server\'s account')

    def test_account_info(self):
        '''Get account information'''
        self.vultr.account.info()

    def test_server_create(self):
        '''Create a server instance (this will take 5-10 minutes)'''
        response = self.vultr.server.create(
            1,      # DCID (New Jersey, USA)
            29,     # VPSPLANID (768 MB RAM,15 GB SSD,1.00 TB BW)
            216,    # OSID (Ubuntu 16.04 i386)
            {
                'label': VULTR_TEST_LABEL
            }
        )
        warnings.warn('Creating VM: {0}'
                      '\n This will cost money.'
                      '\n Sleeping for 5 minutes...'
                      . format(response))
        sleep(300)

    def test_server_list(self):
        '''List servers'''
        AuthenticatedTests.server_list = self.vultr.server.list()

    def test_server_list_by_subid(self):
        '''List server by SUBID'''
        for subid in AuthenticatedTests.server_list:
            self.vultr.server.list(subid=subid)

    def test_server_destroy(self):
        '''Destroy a server instance'''
        servers = self.vultr.server.list()
        for subid in servers:
            # skip machines not made by tests.
            if servers[subid]['label'] != VULTR_TEST_LABEL:
                warnings.warn('skipping [{0}]:\n{1}'
                              . format(subid, str(servers[subid])))
                continue
            self.vultr.server.destroy(subid)
            warnings.warn('Destroying VM: {0}' . format(subid))

if __name__ == '__main__':
    unittest.main()
