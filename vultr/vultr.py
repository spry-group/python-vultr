'''Python library for the Vultr cloud API'''
from .utils import VultrBase
from .v1_account import VultrAccount
from .v1_app import VultrApp
from .v1_backup import VultrBackup
from .v1_dns import VultrDNS
from .v1_firewall import VultrFirewall
from .v1_iso import VultrISO
from .v1_os import VultrOS
from .v1_plans import VultrPlans
from .v1_regions import VultrRegions
from .v1_reservedip import VultrReservedIP
from .v1_server import VultrServer
from .v1_snapshot import VultrSnapshot
from .v1_sshkey import VultrSSHKey
from .v1_startupscript import VultrStartupScript


class Vultr(VultrBase):
    '''Public Vultr interface'''

    # pylint: disable=too-many-instance-attributes
    # The interface is large, but built correctly
    def __init__(self, api_key):
        VultrBase.__init__(self, api_key)
        self.account = VultrAccount(api_key)
        self.app = VultrApp(api_key)
        self.backup = VultrBackup(api_key)
        self.dns = VultrDNS(api_key)
        self.firewall = VultrFirewall(api_key)
        self.iso = VultrISO(api_key)
        # pylint: disable=invalid-name
        # OS is the Vultr API namespace name
        self.os = VultrOS(api_key)
        self.plans = VultrPlans(api_key)
        self.regions = VultrRegions(api_key)
        self.reservedip = VultrReservedIP(api_key)
        self.server = VultrServer(api_key)
        self.snapshot = VultrSnapshot(api_key)
        self.sshkey = VultrSSHKey(api_key)
        self.startupscript = VultrStartupScript(api_key)
