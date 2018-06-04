'''Partial class to handle Vultr Snapshot API calls'''
from .utils import VultrBase, update_params


class VultrSnapshot(VultrBase):
    '''Handles Vultr Snapshot API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def create(self, subid, params=None):
        ''' /v1/snapshot/create
        POST - account
        Create a snapshot from an existing virtual machine.
        The virtual machine does not need to be stopped.

        Link: https://www.vultr.com/api/#snapshot_create
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/snapshot/create', params, 'POST')

    def destroy(self, snapshotid, params=None):
        ''' /v1/snapshot/destroy
        POST - account
        Destroy (delete) a snapshot. There is no going
        back from this call.

        Link: https://www.vultr.com/api/#snapshot_destroy
        '''
        params = update_params(params, {'SNAPSHOTID': snapshotid})
        return self.request('/v1/snapshot/destroy', params, 'POST')

    def list(self, params=None):
        ''' /v1/snapshot/list
        GET - account
        List all snapshots on the current account

        Link: https://www.vultr.com/api/#snapshot_snapshot_list
        '''
        params = params if params else dict()
        return self.request('/v1/snapshot/list', params, 'GET')
