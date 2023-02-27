from pysnmp.hlapi import *

N, R = 0, 5

g = bulkCmd(SnmpEngine(),
            CommunityData('BBTBSASPOP39'),
            UdpTransportTarget(('192.168.39.21', 161)),
            ContextData(),
            N,R,
            ObjectType(ObjectIdentity('IF-MIB', 'ifDescr')))



