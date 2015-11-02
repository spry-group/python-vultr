'''Partial class to handle Vultr OS API calls'''
from .utils import VultrBase


class VultrOS(VultrBase):
    '''Handles Vultr OS API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def list(self, params=None):
        ''' /v1/os/list
        GET - public
        Retrieve a list of available operating systems. If
        the 'windows' flag is true, a Windows licenses will
        be included with the instance, which will increase the cost.

        Link: https://www.vultr.com/api/#os_os_list
        '''
        params = params if params else dict()
        return self.request('/v1/os/list', params, 'GET')
