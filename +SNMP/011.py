from pysnmp.hlapi import *

iterator = getCmd(
    SnmpEngine(),
    CommunityData('BBTBSASPOP39'),
    UdpTransportTarget(('192.168.39.21', 161)),
    ContextData(),
    ObjectType(
        ObjectIdentity(
            'TCP-MIB',
            'tcpConnLocalAddress',
            '0.0.0.0', 23,
            '0.0.0.0', 0
        )
    ).addAsn1MibSource('http://mibs.snmplabs.com/asn1/@mib@')
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
