from pysnmp.entity.rfc3413.oneliner import cmdgen
import datetime

cmdGen = cmdgen.CommandGenerator()

host= '192.168.39.21'
community='BBTBSASPOP39'
N, R = 0, 10

ifdescr = '.1.3.6.1.2.1.2.2.1.2' # Uptime ID

errorIndication, errorStatus, errorIndex, varBinds = cmdGen.bulkCmd(
    cmdgen.CommunityData(community),
    cmdgen.UdpTransportTarget((host, 161)),
    N,R,
    ifdescr
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
            print()
            # print('%s = %s' % (name.prettyPrint(), str(val)))

