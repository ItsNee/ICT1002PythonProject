from subprocess import check_output
import os
def convertEvtx2Csv():
    
    directory = os.fsencode("C:\\Users\\Neeranjan\\Desktop\\testingLogs\\")
        
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        filenameCSV = filename.replace(".evtx", ".csv")
        print(filename)
        print(filenameCSV)
        print(check_output('"C:\\Program Files (x86)\\Log Parser 2.2\\LogParser.exe" "Select * into '+str(directory.decode("utf-8"))+str(filenameCSV)+' from '+str(directory.decode("utf-8"))+str(filename)+'" -i:evt -o:csv', shell=True).decode())
convertEvtx2Csv()