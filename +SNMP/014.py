from pysnmp.entity.rfc3413.oneliner import cmdgen

snmpCmdGen = cmdgen.CommandGenerator() # creamos obj clase CommandGenerator
snmpTransportData = cmdgen.UdpTransportTarget(('192.168.39.21', 161))
mib = cmdgen.MibVariable('SNMPv2-MIB', 'sysName', 0)

# error, errorStatus, errorIndex, binds = snmpCmdGen.getCmd(cmdgen.CommunityData('BBTBSASPOP39'), snmpTransportData, mib)
error, errorStatus, errorIndex, binds = snmpCmdGen.getCmd(cmdgen.CommunityData('BBTBSASPOP39'), snmpTransportData, ".1.3.6.1.2.1.1.1.0", ".1.3.6.1.2.1.1.3.0")


if error:
    print( "Error "+error)
else:
    if errorStatus:
        print('%s at %s'% (
            errorStatus.prettyPrint(),
            errorindex and binds[int(errorIndex) - 1] or '?'
            )
              )
    else:
        for name, val in binds:
            print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
            # print(name.prettyPrint())
            # print(val.prettyPrint())