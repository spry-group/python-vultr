'''Partial class to handle Vultr Firewall API calls'''
from .utils import VultrBase


class VultrFirewall(VultrBase):
    '''Handles Vultr Firewall API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def group_list(self, params=None):
        ''' /v1/firewall/group_list
        GET - account
        List all firewall groups on the current account.

        Link: https://www.vultr.com/api/#firewall_group_list
        '''
        params = params if params else dict()
        return self.request('/v1/firewall/group_list', params, 'GET')
