from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen

import time

t = time.time()

iterator = getCmd(SnmpEngine(),
                  CommunityData('public'),
                  UdpTransportTarget(('127.0.0.1', 161)),
                  ContextData(),
                  ObjectType(ObjectIdentity("1.3.6.1.2.1.7.1.0")))

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:  # SNMP engine errors
    print(errorIndication)
else:
    if errorStatus:  # SNMP  agent errors
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            varBinds[int(errorIndex) - 1] if errorIndex else '?'))
    else:
        for varBind in varBinds:  # SNMP response contents
            print(' = '.join([x.prettyPrint() for x in varBind]))

print(time.time() - t, 's')

g = setCmd(SnmpEngine(),
           CommunityData('public'),
           UdpTransportTarget(('127.0.0.1', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysContact', 0), 'hi'))
next(g)
print(g);

time.sleep(300)


def cbFun(sendRequestHandle, errorIndication, errorStatus, errorIndex,
          varBindTable, cbCtx):
    if errorIndication:
        print(errorIndication)
        return 1
    if errorStatus:
        print(errorStatus.prettyPrint())
        return 1
    for varBindRow in varBindTable:
        for oid, val in varBindRow:
            print('%s = %s' % (oid.prettyPrint(),
                               val and val.prettyPrint() or '?'))


cmdGen = cmdgen.AsynCommandGenerator()

cmdGen.nextCmd(
    cmdgen.CommunityData('public'),
    cmdgen.UdpTransportTarget(('127.0.0.1', 161)),
    ((1, 3, 6, 1, 2, 1, 1),), (cbFun, None)

)

cmdGen.snmpEngine.transportDispatcher.runDispatcher()

time.sleep(300)