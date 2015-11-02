'''Partial class to handle Vultr Startup Script API calls'''
from .utils import VultrBase, update_params


class VultrStartupScript(VultrBase):
    '''Handles Vultr Startup Script API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def create(self, name, script, params=None):
        ''' /v1/startupscript/create
        POST - account
        Create a startup script

        Link: https://www.vultr.com/api/#startupscript_create
        '''
        params = update_params(params, {
            'name': name,
            'script': script
        })
        return self.request('/v1/startupscript/create', params, 'POST')

    def destroy(self, scriptid, params=None):
        ''' /v1/startupscript/destroy
        POST - account
        Remove a startup script

        Link: https://www.vultr.com/api/#startupscript_destroy
        '''
        params = update_params(params, {'SCRIPTID': scriptid})
        return self.request('/v1/startupscript/destroy', params, 'POST')

    def list(self, params=None):
        ''' /v1/startupscript/list
        GET - account
        List all startup scripts on the current account. 'boot' type
        scripts are executed by the server's operating system on the
        first boot. 'pxe' type scripts are executed by iPXE when the
        server itself starts up.

        Link: https://www.vultr.com/api/#startupscript_list
        '''
        params = params if params else dict()
        return self.request('/v1/startupscript/list', params, 'GET')

    def update(self, scriptid, params=None):
        ''' /v1/startupscript/update
        POST - account
        Update an existing startup script

        Link: https://www.vultr.com/api/#startupscript_update
        '''
        params = update_params(params, {'SCRIPTID': scriptid})
        return self.request('/v1/startupscript/update', params, 'POST')
