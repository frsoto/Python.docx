from pysnmp.hlapi import *

g = getCmd(SnmpEngine(),
            CommunityData('BBTBSASPOP39'),
            UdpTransportTarget(('192.168.39.21', 161)),
            ContextData(),
            # ObjectType(ObjectIdentity('IF-MIB', 'ifDescr', 6291456,8388808 )))
            ObjectType(ObjectIdentity('IF-MIB', 'ifDescr')))

print(next(g))

