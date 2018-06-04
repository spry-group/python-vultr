'''Partial class to handle Vultr ISO API calls'''
from .utils import VultrBase, update_params


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

    def create_from_url(self, url, params=None):
        ''' /vi/iso/create_from_url
        POST - account
        Create a new ISO image on the current account.
        The ISO image will be downloaded from a given URL.
        Download status can be checked with the v1/iso/list call.

        Link: https://www.vultr.com/api/#iso_create_from_url
        '''
        params = update_params(params, {
            'url': url,
        })
        return self.request('/v1/iso/create_from_url', params, 'POST')

