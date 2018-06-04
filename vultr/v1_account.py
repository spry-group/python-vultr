'''Partial class to handle Vultr Account API calls'''
from .utils import VultrBase


class VultrAccount(VultrBase):
    '''Handles Vultr Account API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def info(self, params=None):
        ''' /v1/account/info
        GET - account
        Retrieve information about the current account

        Link: https://www.vultr.com/api/#account_info
        '''
        params = params if params else dict()
        return self.request('/v1/account/info', params, 'GET')
