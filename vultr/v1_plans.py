'''Partial class to handle Vultr Plans API calls'''
from .utils import VultrBase


class VultrPlans(VultrBase):
    '''Handles Vultr Plans API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)

    def list(self, params=None):
        ''' /v1/plans/list
        GET - public
        Retrieve a list of all active plans. Plans that are
        no longer available will not be shown. The 'windows'
        field is no longer in use, and will always be false.
        Windows licenses will be automatically added to any
        plan as necessary. If your account has special plans
        available, you will need to pass your api_key in in
        order to see them. For all other accounts, the API
        key is not optional.

        Link: https://www.vultr.com/api/#plans_plan_list
        '''
        params = params if params else dict()
        return self.request('/v1/plans/list', params, 'GET')
