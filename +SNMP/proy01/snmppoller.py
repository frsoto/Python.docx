import schedule, csv, time
from easysnmp import Session
from datetime import datetime

def poll(host, com, ver, mib):
    session = Session(hostname=host, community=com, version=ver)
    output = session.get(mib)
    # print (output)
    with open('results.csv','a') as results:
        resultscsv = csv.writer(results)
        resultscsv.writerow([datetime.now(), host, mib, output.value])


# El archivo .csv tiene este formato:
# hostname, cada cuanto segundo se hace el poleo, comunidad, version de nsmp, oid
with open('inventory.csv') as inventory:
    invcsv = csv.reader(inventory) # creamos un obj reader? python hace el parceo automaticamente.
    for row in invcsv:
        host = row[0]
        freq = int(row[1])
        com = row[2]
        ver = int(row[3])
        for mib in row[4:]: # con los : le decimos q lea hasta el final
            schedule.every(freq).seconds.do(poll, host, com, ver, mib) # los arg se pasan asi con schedule

# este es para q corra el schedule q creamos.
while True:
    schedule.run_pending()
    time.sleep(1)