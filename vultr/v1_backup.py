'''Partial class to handle Vultr Backup API calls'''
from .utils import VultrBase


class VultrBackup(VultrBase):
    '''Handles Vultr Backup API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def list(self, params=None):
        ''' /v1/backup/list
        GET - account
        List all backups on the current account

        Link: https://www.vultr.com/api/#backup_backup_list
        '''
        params = params if params else dict()
        return self.request('/v1/backup/list', params, 'GET')
