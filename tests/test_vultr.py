import unittest
import os
import warnings
from vultr import Vultr, VultrError


class UnauthenticateTests(unittest.TestCase):

    def setUp(self):
        self.vultr = Vultr('')

    def test_plans_list(self):
        response = self.vultr.plans_list()

    def test_regions_list(self):
        response = self.vultr.regions_list()

    def test_os_list(self):
        response = self.vultr.os_list()

    def test_app_list(self):
        response = self.vultr.app_list()


@unittest.skipIf(not os.environ.get('VULTR_KEY'), 'Skipping AuthenticatedTests')
class AuthenticatedTests(unittest.TestCase):

    def setUp(self):
        self.VULTR_KEY = os.environ.get('VULTR_KEY')
        self.vultr = Vultr(self.VULTR_KEY)

    def test_get_api_key(self):
        response = self.vultr.iso_list()

    def test_post_api_key(self):
        try:
            response = self.vultr.server_label_set('', '')
        except VultrError as e:
            msg = str(e)
            self.assertEqual(msg, "Request failed. Check the response body" +
                                  " for a more detailed description. Body:" +
                                  " \nInvalid server.  Check SUBID value and" +
                                  " ensure your API key matches the server's" +
                                  " account")

    def test_account_info(self):
        response = self.vultr.account_info()

    def test_server_create(self):
        response = self.vultr.server_create(vpsplanid=29, dcid=1, osid=191 )

if __name__ == '__main__':
    unittest.main()
