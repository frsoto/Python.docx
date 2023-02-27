from pysnmp.hlapi import *
Lista=[]
Lista2=[]
Lista3=[]
Lista4=[]

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
            # print(varBind)
            # Lista.append((varBind[1]))
            Lista.append(varBind)

# print(Lista[1])
# print(type(Lista[1]))

# Paso la Lista ObjectType a lista de Tuplas. Cada tupla 2 elementos (elem1: ObjectIdentity, elem2: String)
for elem in Lista:
    Lista2.append(tuple(elem))
    # print(tuple(elem))

print()

for elem in Lista2:
    # print(elem[0])
    # print(elem[1])
    Lista3.append(str(elem[1]))

print(Lista3)

# for l in Lista3:
#     print(l)
#     print(str(l))
#     print(type(l))


