'''Partial class to handle Vultr Regions API calls'''
from .utils import VultrBase, update_params


class VultrRegions(VultrBase):
    '''Handles Vultr Regions API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def availability(self, dcid, params=None):
        ''' /v1/regions/availability
        GET - public
        Retrieve a list of the VPSPLANIDs currently available
        in this location. If your account has special plans available,
        you will need to pass your api_key in in order to see them.
        For all other accounts, the API key is not optional.

        Link: https://www.vultr.com/api/#regions_region_available
        '''
        params = update_params(params, {'DCID': dcid})
        return self.request('/v1/regions/availability', params, 'GET')

    def list(self, params=None):
        ''' /v1/regions/list
        GET - public
        Retrieve a list of all active regions. Note that just
        because a region is listed here, does not mean that
        there is room for new servers.

        Link: https://www.vultr.com/api/#regions_region_list
        '''
        params = params if params else dict()
        return self.request('/v1/regions/list', params, 'GET')
