'''Partial class to handle Vultr DNS API calls'''
from .utils import VultrBase, update_params


class VultrDNS(VultrBase):
    '''Handles Vultr DNS API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def create_domain(self, domain, ipaddr, params=None):
        ''' /v1/dns/create_domain
        POST - account
        Create a domain name in DNS

        Link: https://www.vultr.com/api/#dns_create_domain
        '''
        params = update_params(params, {
            'domain': domain,
            'ip': ipaddr
        })
        return self.request('/v1/dns/create_domain', params, 'POST')

    def create_record(self, domain, name, _type, data, params=None):
        ''' /v1/dns/create_domain
        POST - account
        Add a DNS record

        Link: https://www.vultr.com/api/#dns_create_record
        '''
        params = update_params(params, {
            'domain': domain,
            'name': name,
            'type': _type,
            'data': data
        })
        return self.request('/v1/dns/create_record', params, 'POST')

    def delete_domain(self, domain, params=None):
        ''' /v1/dns/delete_domain
        POST - account
        Delete a domain name (and all associated records)

        Link: https://www.vultr.com/api/#dns_delete_domain
        '''
        params = update_params(params, {'domain': domain})
        return self.request('/v1/dns/delete_domain', params, 'POST')

    def delete_record(self, domain, recordid, params=None):
        ''' /v1/dns/delete_record
        POST - account
        Deletes an individual DNS record

        Link: https://www.vultr.com/api/#dns_delete_record
        '''
        params = update_params(params, {
            'domain': domain,
            'RECORDID': recordid
        })
        return self.request('/v1/dns/delete_record', params, 'POST')

    def list(self, params=None):
        ''' /v1/dns/list
        GET - account
        List all domains associated with the current account

        Link: https://www.vultr.com/api/#dns_dns_list
        '''
        params = params if params else dict()
        return self.request('/v1/dns/list', params, 'GET')

    def records(self, domain, params=None):
        ''' /v1/dns/records
        GET - account
        List all the records associated with a particular domain

        Link: https://www.vultr.com/api/#dns_records
        '''
        params = update_params(params, {'domain': domain})
        return self.request('/v1/dns/records', params, 'GET')

    def update_record(self, domain, recordid, params=None):
        ''' /v1/dns/update_record
        POST - account
        Update a DNS record

        Link: https://www.vultr.com/api/#dns_update_record
        '''
        params = update_params(params, {
            'domain': domain,
            'RECORDID': recordid
        })
        return self.request('/v1/dns/update_record', params, 'POST')
