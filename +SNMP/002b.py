from pysnmp.entity.rfc3413.oneliner import cmdgen
import datetime

cmdGen = cmdgen.CommandGenerator()

host= '192.168.39.21'
community='BBTBSASPOP39'
# OIDS
system_name = '1.3.6.1.2.1.1.5.0'   # Host ID
system_uptime = '1.3.6.1.2.1.1.3.0' # Uptime ID
v1020_status = '.1.3.6.1.2.1.2.2.1.7.8389628'   # Interfaz OID Vlan 1020

def snmp_query (host, community, oid):
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((host, 161)),
        oid
        # system_name,
        # system_uptime,
        # v1020_status
    )

    # Check for errors and print out results
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for name, val in varBinds:
                # print('%s = %s' % (name.prettyPrint(), str(val)))
                return (str(val))


result = {}
result['Time'] = datetime.datetime.utcnow().isoformat()

result['hostname'] = snmp_query(host, community, system_name)
result['Uptime'] = snmp_query(host, community, system_uptime)
result['Vlan1020'] = snmp_query(host, community, v1020_status)

print(result)