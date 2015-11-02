'''Partial class to handle Vultr SSH Key API calls'''
from .utils import VultrBase, update_params


class VultrSSHKey(VultrBase):
    '''Handles Vultr SSH Key API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def create(self, name, ssh_key, params=None):
        ''' /v1/sshkey/create
        POST - account
        Create a new SSH Key

        Link: https://www.vultr.com/api/#sshkey_create
        '''
        params = update_params(params, {
            'name': name,
            'ssh_key': ssh_key
        })
        return self.request('/v1/sshkey/create', params, 'POST')

    def destroy(self, sshkeyid, params=None):
        ''' /v1/sshkey/destroy
        POST - account
        Remove a SSH key. Note that this will not remove
        the key from any machines that already have it.

        Link: https://www.vultr.com/api/#sshkey_destroy
        '''
        params = update_params(params, {'SSHKEYID': sshkeyid})
        return self.request('/v1/sshkey/destroy', params, 'POST')

    def list(self, params=None):
        ''' /v1/sshkey/list
        GET - account
        List all the SSH keys on the current account

        Link: https://www.vultr.com/api/#sshkey_list
        '''
        params = params if params else dict()
        return self.request('/v1/sshkey/list', params, 'GET')

    def update(self, sshkeyid, params=None):
        ''' /v1/sshkey/update
        POST - account
        Update an existing SSH Key. Note that this will only
        update newly installed machines. The key will not be
        updated on any existing machines.

        Link: https://www.vultr.com/api/#sshkey_update
        '''
        params = update_params(params, {'SSHKEYID': sshkeyid})
        return self.request('/v1/sshkey/update', params, 'POST')
