#Read the arp Table
import os
import datetime
newDict = {}
storedmac = []
duplicates = []
def readArpTable():
    table = os.popen("arp -a").read()
    tableSplit = table.splitlines()
    for line in tableSplit:
        #print(line)
        if len(line.split()) != 3:
            continue
        ip,mac,_type = line.split()
        newDict[ip] = mac
    return newDict
readArpTable()

#Function reads through arp table ips and macs
def arpScan():
    for key in newDict:
        print(key + " " + newDict[key])
    #variable to store mac addresses
        storedmac.append(newDict[key])
    print(storedmac)
    print(len(storedmac))
    #if number of ip addresses in macs are more than 0 throw alert
    macset = set(storedmac)
    print(macset)
    if len(storedmac) != len(macset):
        print(len(macset))
        #gather duplicates
        for key in storedmac:
            if storedmac.count(key) > 1:
                alrt = "\nASDetective: There are duplicate mac addresses on the network."
                if key not in duplicates:
                    duplicates.append(key)
            """(for upgrades or diff versions)if key not in duplicates:
                duplicates.append(key)"""
            print("\n ASDetective: There are duplicate mac addresses on the network.")
        else:
            print("     ")


        print("Duplicates: " + str(duplicates))
        return alrt
arpScan()
msg = arpScan()
# ..................:::::::::::Logger!:::::::::::....................
# Creates Log file and writes data given, to newfile.
def logPost(msg):
    myLog = open("myLog.txt", "a")
    myLog.write(str(datetime.datetime.now()) + msg + "\nArp Table: \n" + str(newDict) + "\n" + "Mac List:\n" + str(storedmac) + "\n" +"Duplicates Found: \n" + str(duplicates))
    myLog.close()

logPost(msg)
