from pysnmp.hlapi import *
Lista=[]
Lista2=[]
Lista3=[]

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
            # print(' = '.join([x.prettyPrint() for x in varBind]))
            print([x for x in varBind])
            print([x[0] for x in varBind])
            print([x[1] for x in varBind])
            print([x[2] for x in varBind])
            print([x[3] for x in varBind])
            print([x[4] for x in varBind])
            # print([x[5] for x in varBind])
            # print([x.prettyPrint() for x in varBind])








