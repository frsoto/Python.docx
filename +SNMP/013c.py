from pysnmp.hlapi import *
Lista=[]

iterator = nextCmd(
    SnmpEngine(),
    CommunityData('BBTBSASPOP39'),
    UdpTransportTarget(('192.168.39.21', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('IF-MIB', 'ifDescr')),
    # ObjectType(ObjectIdentity('IF-MIB', 'ifType')),
    # ObjectType(ObjectIdentity('IF-MIB', 'ifMtu')),
    # ObjectType(ObjectIdentity('IF-MIB', 'ifSpeed')),
    # ObjectType(ObjectIdentity('IF-MIB', 'ifPhysAddress')),
    # ObjectType(ObjectIdentity('IF-MIB', 'ifType')),
    lexicographicMode=False

)

for errorIndication, errorStatus, errorIndex, varBinds in iterator:
    if errorIndication:
        print(errorIndication)
        break

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
        break

    else:
        for varBind in varBinds:
            Lista.append(str(tuple(varBind)[1]))

print(Lista)



