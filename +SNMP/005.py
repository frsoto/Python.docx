from pysnmp.hlapi import *

system_name = '1.3.6.1.2.1.1.5.0'   # Host ID
system_uptime = '1.3.6.1.2.1.1.3.0' # Uptime ID
v1020_status = '.1.3.6.1.2.1.2.2.1.7.8389628'   # Interfaz OID Vlan 1020


g = nextCmd(SnmpEngine(),
            CommunityData('BBTBSASPOP39'),
            UdpTransportTarget(('192.168.39.21', 161)),
            ContextData(),
            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr'))
            # ObjectType(ObjectIdentity('IF-MIB', 'ifDescr', 6291456))
            )



errorIndication, errorStatus, errorIndex, varBinds = next(g)

if errorIndication:
    print(errorIndication)

elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
        print(varBind)
        print(varBind[0])
        print(varBind[1])
