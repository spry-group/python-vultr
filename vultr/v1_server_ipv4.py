'''Partial class to handle Vultr Server (IPv4) API calls'''
from .utils import VultrBase, update_params


class VultrServerIPv4(VultrBase):
    '''Handles Vultr Server (IPv4) API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def create(self, subid, params=None):
        ''' /v1/server/create_ipv4
        POST - account
        Add a new IPv4 address to a server. You will start being billed for
        this immediately. The server will be rebooted unless you specify
        otherwise. You must reboot the server before the IPv4 address can be
        configured.

        Link: https://www.vultr.com/api/#server_create_ipv4
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/create_ipv4', params, 'POST')

    def destroy(self, subid, ipaddr, params=None):
        ''' /v1/server/destroy_ipv4
        POST - account
        Removes a secondary IPv4 address from a server. Your server will be
        hard-restarted. We suggest halting the machine gracefully before
        removing IPs.

        Link: https://www.vultr.com/api/#server_destroy_ipv4
        '''
        params = update_params(params, {
            'SUBID': subid,
            'ip': ipaddr
        })
        return self.request('/v1/server/destroy_ipv4', params, 'POST')

    def list(self, subid, params=None):
        ''' /v1/server/list_ipv4
        GET - account
        List the IPv4 information of a virtual machine. IP information is only
        available for virtual machines in the "active" state.

        Link: https://www.vultr.com/api/#server_list_ipv4
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/list_ipv4', params, 'GET')

    def reverse_default(self, subid, ipaddr, params=None):
        ''' /v1/server/reverse_default_ipv4
        POST - account
        Set a reverse DNS entry for an IPv4 address of a virtual
        machine to the original setting. Upon success, DNS changes
        may take 6-12 hours to become active.

        Link: https://www.vultr.com/api/#server_reverse_default_ipv4
        '''
        params = update_params(params, {
            'SUBID': subid,
            'ip': ipaddr
        })
        return self.request('/v1/server/reverse_default_ipv4', params, 'POST')

    def reverse_set(self, subid, ipaddr, entry, params=None):
        ''' /v1/server/reverse_set_ipv4
        POST - account
        Set a reverse DNS entry for an IPv4 address of a virtual machine. Upon
        success, DNS changes may take 6-12 hours to become active.

        Link: https://www.vultr.com/api/#server_reverse_set_ipv4
        '''
        params = update_params(params, {
            'SUBID': subid,
            'ip': ipaddr,
            'entry': entry
        })
        return self.request('/v1/server/reverse_set_ipv4', params, 'POST')
