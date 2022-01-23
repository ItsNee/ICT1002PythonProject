from subprocess import check_output
import os
import pandas as pd

def getip(x):
    x = x.split('-')
    for i in range(len(x)-1):
        x.pop(0)
    x = x[0].split('.')
    x.pop()
    x = '.'.join(x)
    return x

directory = os.fsencode("C:\\Users\\Neeranjan\\Desktop\\testingLogs\\")
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    filenameCSV = filename.replace(".evtx", ".csv")
    ip = getip(filenameCSV)
    #print(filename)
    #print(filenameCSV)
    #print(ip)
    print(check_output('"C:\\Program Files (x86)\\Log Parser 2.2\\LogParser.exe" "Select * into '+str(directory.decode("utf-8"))+str(filenameCSV)+' from '+str(directory.decode("utf-8"))+str(filename)+'" -i:evt -o:csv', shell=True).decode())
    df = pd.read_csv(directory.decode("utf-8") + filenameCSV) # create temp pandas dataframe
    df["Ip_Address"] = ip
    print(df["TimeGenerated"])
    df.to_csv(directory.decode("utf-8") + filenameCSV, index=False)