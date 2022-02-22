from turtle import pen
import pandas as pd
import functools
import numpy
#Windows=========================================================================================================
df = pd.read_csv ('./static/assets/windows.csv', on_bad_lines='skip')
windowsEventIds = pd.read_csv ('./static/assets/windowsEventIds.csv', on_bad_lines='skip')
allColumns = df.columns.values
#allUniqEventIDs = sorted(df['EventID'].unique().tolist())

##Event IDs Against its frequency================================================================================
allUniqEventIDsFreq = df['EventID'].value_counts().to_dict()
#print(allUniqEventIDsFreq)
#=================================================================================================================

##Event IDs Against its frequency================================================================================
eventIDsBy = df.sort_values('EventID').drop(columns=['EventLog','RecordNumber','TimeWritten','EventType','EventTypeName','EventCategory','EventCategoryName','SourceName','SID','Message','Data'])
eventIDsBy["EventIdTitle"] = ""
eventIDsBy["EventIdDescription"] = ""
# for i in eventIDsBy.index:
#     eventId = eventIDsBy["EventID"][i]
#     title = windowsEventIds.loc[windowsEventIds['EventIDs'] == eventId, 'Title'].item()
#     Description = windowsEventIds.loc[windowsEventIds['EventIDs'] == eventId, 'Description'].item()
#     eventIDsBy.loc[i,'EventIdTitle'] = title
#     eventIDsBy.loc[i,'EventIdDescription'] = Description
#print(eventIDsBy)
#=================================================================================================================

##IP Addy AGAINST Count VS EventIDs================================================================================
ipAgainstEventIDs = df.drop(columns=['EventLog','RecordNumber','TimeGenerated','TimeWritten','EventType','EventTypeName','EventCategory','EventCategoryName','SourceName','Strings','ComputerName','SID','Message','Data']).dropna()
print(ipAgainstEventIDs)
counter = 1
ipList = []
MEGAipList = []
for i in ipAgainstEventIDs.index:
    currentIpAdd = ipAgainstEventIDs["Ip_Address"][i]
    ipList.append(currentIpAdd)
        
def FreqTableByNeeNFab(data):
    frequencytable = {}
    for key in data:
        if key in frequencytable:
            frequencytable[key] += 1
        else:
            frequencytable[key] = 1
    return frequencytable
ipCountDict = FreqTableByNeeNFab(ipList)
print(ipCountDict)

for i in ipAgainstEventIDs.index:
    currentIpAdd = ipAgainstEventIDs["Ip_Address"][i]
    ipList.append(currentIpAdd)
    singleIpList = []
    print(currentIpAdd)
    if i == 43910:
        MEGAipList.append(singleIpList)
        singleIpList = []
        break
    if currentIpAdd == ipAgainstEventIDs["Ip_Address"][i+1]:
        singleIpList.append(ipAgainstEventIDs["EventID"][i])
    else:
        MEGAipList.append(singleIpList)
        singleIpList = []
print(MEGAipList)
#=================================================================================================================

##Time AGAINST EventID Freq================================================================================
timeAgainstEventIds = df.drop(columns=['EventLog','RecordNumber','TimeWritten','EventType','EventTypeName','EventCategory','EventCategoryName','SourceName','SID','Message','Data'])
#=================================================================================================================