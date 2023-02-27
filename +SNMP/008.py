"""
SNMPv1
++++++

Send SNMP GET request using the following options:

  * with SNMPv1, community 'public'
  * over IPv4/UDP
  * to an Agent at demo.snmplabs.com:161
  * for two instances of SNMPv2-MIB::sysDescr.0 MIB object,

Functionally similar to:

| $ snmpget -v1 -c public demo.snmplabs.com SNMPv2-MIB::sysDescr.0

"""#
from pysnmp.hlapi import *

host= '192.168.39.21'
community='BBTBSASPOP39'
# OIDS
system_name = '1.3.6.1.2.1.1.5.0'   # Host ID
system_uptime = '1.3.6.1.2.1.1.3.0' # Uptime ID
v1020_status = '.1.3.6.1.2.1.2.2.1.7.8389628'   # Interfaz OID Vlan 1020


iterator = getCmd(
    SnmpEngine(),
    CommunityData('comunity', mpModel=0),
    UdpTransportTarget(('host', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
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
