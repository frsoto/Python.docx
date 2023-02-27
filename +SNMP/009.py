from pysnmp.hlapi import *

iterator = nextCmd(SnmpEngine(),
            CommunityData('BBTBSASPOP39'),
            UdpTransportTarget(('192.168.39.21', 161)),
            ContextData(),
            ObjectType(ObjectIdentity('IF-MIB', 'ifDescr')))

for errorIndication, errorStatus, errorIndex, varBinds in iterator:

    if errorIndication:
        print(errorIndication)
        break

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        break

    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))


