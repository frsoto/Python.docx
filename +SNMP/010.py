from pysnmp.hlapi import *

iterator = getCmd(
    SnmpEngine(),
    CommunityData('BBTBSASPOP39'),
    UdpTransportTarget(('192.168.39.21', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('IF-MIB', 'ifInOctets', 234954816)),
    ObjectType(ObjectIdentity('IF-MIB', 'ifOutOctets', 234954816))
)

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:
    print(errorIndication)

elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))