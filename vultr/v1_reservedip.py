'''Partial class to handle Vultr ReservedIP API calls'''
from .utils import VultrBase, update_params


class VultrReservedIP(VultrBase):
    '''Handles Vultr ReservedIP API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def create(self, dcid, ip_type, params=None):
        ''' /v1/reservedip/create
        POST - account
        Create a new reserved IP. Reserved IPs can only be used within the
        same datacenter for which they were created.

        Link: https://www.vultr.com/api/#reservedip_create
        '''
        params = update_params(params, {
            'DCID': dcid,
            'ip_type': ip_type
        })
        return self.request('/v1/reservedip/create', params, 'POST')
    
    def convert(self, subid, ip_address, params=None):
        ''' /v1/reservedip/convert
        POST - account
        Convert an existing IP on a subscription to a reserved IP. 
        Returns the SUBID of the newly created reserved IP.

        Link: https://www.vultr.com/api/#reservedip_convert
        '''
        params = update_params(params, {
            'SUBID': subid,
            'ip_address': ip_address
        })
        return self.request('/v1/reservedip/convert', params, 'POST')
