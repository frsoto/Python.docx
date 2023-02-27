from pysnmp.hlapi import *
from pysnmp.smi.view import *
from pysnmp.smi import builder, view, compiler, rfc1902
# mibViewController = pysnmp.smi.view()

v = ObjectIdentity('SNMPv2-MIB', 'system')
w = ObjectIdentity((1, 3, 6, 1, 2, 1, 1, 1, 0))
x = ObjectIdentity('iso.org.dod.internet.mgmt.mib-2.system.sysDescr.0')
y = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
z = ObjectIdentity('IP-MIB', 'ipAdEntAddr', '127.0.0.1', 123)



