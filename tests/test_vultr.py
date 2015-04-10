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


class AuthenticatedTests(unittest.TestCase):

    def setUp(self):
        self.VULTR_KEY = os.environ.get('VULTR_KEY')

        if self.VULTR_KEY is None:
            warnings.warn('The VULTR_KEY environment variable is not ' +
                          'set. AuthenticatedTests will be bypassed.',
                          UserWarning)
        else:
            self.vultr = Vultr(self.VULTR_KEY)

    def test_get_api_key(self):
        if self.VULTR_KEY is None:
            return
        response = self.vultr.iso_list()

    def test_post_api_key(self):
        if self.VULTR_KEY is None:
            return
        try:
            response = self.vultr.server_label_set('', '')
        except VultrError as e:
            msg = str(e)
            self.assertEqual(msg, "Request failed. Check the response body" +
                                  " for a more detailed description. Body:" +
                                  " \nInvalid server.  Check SUBID value and" +
                                  " ensure your API key matches the server's" +
                                  " account")

if __name__ == '__main__':
    unittest.main()
