'''Partial class to handle Vultr ISO API calls'''
from .utils import VultrBase


class VultrISO(VultrBase):
    '''Handles Vultr ISO API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def list(self, params=None):
        ''' /v1/iso/list
        GET - account
        List all ISOs currently available on this account

        Link: https://www.vultr.com/api/#iso_iso_list
        '''
        params = params if params else dict()
        return self.request('/v1/iso/list', params, 'GET')
