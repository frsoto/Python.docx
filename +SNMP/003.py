from pysnmp.hlapi import *
# print([x for x in dir() if 'Cmd' in x])
# CommunityData('BBTBSASPOP39', mpModel=1)  # SNMPv2c

host= '192.168.39.21'
community='BBTBSASPOP39'

g = getCmd(SnmpEngine(),
           CommunityData(comunity),
           UdpTransportTarget((host, 161))