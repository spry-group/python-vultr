'''Partial class to handle Vultr App API calls'''
from .utils import VultrBase


class VultrApp(VultrBase):
    '''Handles Vultr App API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def list(self, params=None):
        ''' /v1/app/list
        GET - account
        Retrieve a list of available applications. These
        refer to applications that can be launched when
        creating a Vultr VPS.

        Link: https://www.vultr.com/api/#app_app_list
        '''
        params = params if params else dict()
        return self.request('/v1/app/list', params, 'GET')
