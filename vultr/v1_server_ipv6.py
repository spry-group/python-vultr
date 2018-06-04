'''Partial class to handle Vultr Server (IPv6) API calls'''
from .utils import VultrBase, update_params


class VultrServerIPv6(VultrBase):
    '''Handles Vultr Server (IPv6) API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def list_ipv6(self, subid, params=None):
        ''' /v1/server/list_ipv6
        GET - account
        List the IPv6 information of a virtual machine. IP information is only
        available for virtual machines in the "active" state. If the virtual
        machine does not have IPv6 enabled, then an empty array is returned.

        Link: https://www.vultr.com/api/#server_list_ipv6
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/list_ipv6', params, 'GET')

    def reverse_delete_ipv6(self, subid, ipaddr, params=None):
        ''' /v1/server/reverse_delete_ipv6
        POST - account
        Remove a reverse DNS entry for an IPv6 address of a virtual machine.
        Upon success, DNS changes may take 6-12 hours to become active.

        Link: https://www.vultr.com/api/#server_reverse_delete_ipv6
        '''
        params = update_params(params, {
            'SUBID': subid,
            'ip': ipaddr
        })
        return self.request('/v1/server/reverse_delete_ipv6', params, 'POST')

    def reverse_list_ipv6(self, subid, params=None):
        ''' /v1/server/reverse_list_ipv6
        GET - account
        List the IPv6 reverse DNS entries of a virtual machine. Reverse DNS
        entries are only available for virtual machines in the "active" state.
        If the virtual machine does not have IPv6 enabled, then an empty array
        is returned.

        Link: https://www.vultr.com/api/#server_reverse_list_ipv6
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/reverse_list_ipv6', params, 'GET')

    def reverse_set_ipv6(self, subid, ipaddr, entry, params=None):
        ''' /v1/server/reverse_set_ipv6
        POST - account
        Set a reverse DNS entry for an IPv6 address of a virtual machine. Upon
        success, DNS changes may take 6-12 hours to become active.

        Link: https://www.vultr.com/api/#server_reverse_set_ipv6
        '''
        params = update_params(params, {
            'SUBID': subid,
            'ip': ipaddr,
            'entry': entry
        })
        return self.request('/v1/server/reverse_set_ipv6', params, 'POST')
