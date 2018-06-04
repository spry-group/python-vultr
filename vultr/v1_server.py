'''Partial class to handle Vultr Server API calls'''
from .utils import VultrBase, update_params
from .v1_server_ipv4 import VultrServerIPv4
from .v1_server_ipv6 import VultrServerIPv6


class VultrServer(VultrBase):
    '''Handles Vultr Server API calls'''
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)
        self.ipv4 = VultrServerIPv4(api_key)
        self.ipv6 = VultrServerIPv6(api_key)

    def bandwidth(self, subid, params=None):
        ''' /v1/server/bandwidth
        GET - account
        Get the bandwidth used by a virtual machine

        Link: https://www.vultr.com/api/#server_bandwidth
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/bandwidth', params, 'GET')

    def create(self, dcid, vpsplanid, osid, params=None):
        ''' /v1/server/create
        POST - account
        Create a new virtual machine. You will start being billed for this
        immediately. The response only contains the SUBID for the new machine.
        You should use v1/server/list to poll and wait for the machine to be
        created (as this does not happen instantly).

        Link: https://www.vultr.com/api/#server_create
        '''
        params = update_params(params, {
            'DCID': dcid,
            'VPSPLANID': vpsplanid,
            'OSID': osid
        })
        return self.request('/v1/server/create', params, 'POST')

    def destroy(self, subid, params=None):
        ''' /v1/server/destroy
        POST - account
        Destroy (delete) a virtual machine. All data will be permanently lost,
        and the IP address will be released. There is no going back from this
        call.

        Link: https://www.vultr.com/api/#server_destroy
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/destroy', params, 'POST')

    def get_user_data(self, subid, params=None):
        ''' /v1/server/get_user_data
        GET - account
        Retrieves the (base64 encoded) user-data for this subscription.

        Link: https://www.vultr.com/api/#server_get_user_data
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/get_user_data', params, 'GET')

    def halt(self, subid, params=None):
        ''' /v1/server/halt
        POST - account
        Halt a virtual machine. This is a hard power off (basically, unplugging
        the machine). The data on the machine will not be modified, and you
        will still be billed for the machine. To completely delete a
        machine, see v1/server/destroy

        Link: https://www.vultr.com/api/#server_halt
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/halt', params, 'POST')

    def label_set(self, subid, label, params=None):
        ''' /v1/server/label_set
        POST - account
        Set the label of a virtual machine.

        Link: https://www.vultr.com/api/#server_label_set
        '''
        params = update_params(params, {
            'SUBID': subid,
            'label': label
        })
        return self.request('/v1/server/label_set', params, 'POST')

    def list(self, subid=None, params=None):
        ''' /v1/server/list
        GET - account
        List all active or pending virtual machines on the current account. The
        'status' field represents the status of the subscription and will be
        one of pending|active|suspended|closed. If the status is 'active', you
        can check 'power_status' to determine if the VPS is powered on or not.
        The API does not provide any way to determine if the initial
        installation has completed or not.

        Link: https://www.vultr.com/api/#server_server_list
        '''
        params = update_params(
            params,
            {'SUBID': subid} if subid else dict()
        )
        return self.request('/v1/server/list', params, 'GET')

    def neighbors(self, subid, params=None):
        ''' v1/server/neighbors
        GET - account
        Determine what other subscriptions are hosted on the same physical
        host as a given subscription.

        Link: https://www.vultr.com/api/#server_neighbors
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/neighbors', params, 'GET')

    def os_change(self, subid, osid, params=None):
        ''' /v1/server/os_change
        POST - account
        Changes the operating system of a virtual machine. All data will be
        permanently lost.

        Link: https://www.vultr.com/api/#server_os_change
        '''
        params = update_params(params, {
            'SUBID': subid,
            'OSID': osid
        })
        return self.request('/v1/server/os_change', params, 'POST')

    def os_change_list(self, subid, params=None):
        ''' /v1/server/os_change_list
        GET - account
        Retrieves a list of operating systems to which this server can be
        changed.

        Link: https://www.vultr.com/api/#server_os_change_list
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/os_change_list', params, 'GET')

    def reboot(self, subid, params=None):
        ''' /v1/server/reboot
        POST - account
        Reboot a virtual machine. This is a hard reboot
        (basically, unplugging the machine).

        Link: https://www.vultr.com/api/#server_reboot
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/reboot', params, 'POST')

    def reinstall(self, subid, params=None):
        ''' /v1/server/reinstall
        POST - account
        Reinstall the operating system on a virtual machine. All data
        will be permanently lost, but the IP address will remain the
        same There is no going back from this call.

        Link: https://www.vultr.com/api/#server_reinstall
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/reinstall', params, 'POST')

    def restore_backup(self, subid, backupid, params=None):
        ''' /v1/server/restore_backup
        POST - account
        Restore the specified backup to the virtual machine. Any data
        already on the virtual machine will be lost.

        Link: https://www.vultr.com/api/#server_restore_backup
        '''
        params = update_params(params, {
            'SUBID': subid,
            'BACKUPID': backupid
        })
        return self.request('/v1/server/restore_backup', params, 'POST')

    def restore_snapshot(self, subid, snapshotid, params=None):
        ''' /v1/server/restore_snapshot
        POST - account
        Restore the specificed snapshot to the virtual machine.
        Any data already on the virtual machine will be lost.

        Link: https://www.vultr.com/api/#server_restore_snapshot
        '''
        params = update_params(params, {
            'SUBID': subid,
            'SNAPSHOTID': snapshotid
        })
        return self.request('/v1/server/restore_snapshot', params, 'POST')

    def set_user_data(self, subid, userdata, params=None):
        ''' /v1/server/set_user_data
        POST - account
        Sets the cloud-init user-data (base64) for this subscription.
        Note that user-data is not supported on every operating
        system, and is generally only provided on instance startup.

        Link: https://www.vultr.com/api/#server_set_user_data
        '''
        params = update_params(params, {
            'SUBID': subid,
            'userdata': userdata
        })
        return self.request('/v1/server/set_user_data', params, 'POST')

    def start(self, subid, params=None):
        ''' /v1/server/start
        POST - account
        Start a virtual machine. If the machine is already
        running, it will be restarted.

        Link: https://www.vultr.com/api/#server_start
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/start', params, 'POST')

    def upgrade_plan(self, subid, vpsplanid, params=None):
        ''' /v1/server/upgrade_plan
        POST - account
        Upgrade the plan of a virtual machine. The virtual machine will be
        rebooted upon a successful upgrade.

        Link: https://www.vultr.com/api/#server_upgrade_plan
        '''
        params = update_params(params, {
            'SUBID': subid,
            'VPSPLANID': vpsplanid
        })
        return self.request('/v1/server/upgrade_plan', params, 'POST')

    def upgrade_plan_list(self, subid, params=None):
        ''' /v1/server/upgrade_plan_list
        GET - account
        Retrieve a list of the VPSPLANIDs for which a virtual machine
        can be upgraded. An empty response array means that there are
        currently no upgrades available.

        Link: https://www.vultr.com/api/#server_upgrade_plan_list
        '''
        params = update_params(params, {'SUBID': subid})
        return self.request('/v1/server/upgrade_plan_list', params, 'GET')
