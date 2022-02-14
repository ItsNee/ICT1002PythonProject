import pandas as pd

line_list = []

with open("godsavemypc3.txt", "r") as a_file:
  for line in a_file:
    line = line.split()
    line[8: len(line)] = [' '.join(line[8: len(line)])]
    line[8] = line[8].replace("â†’", "-")
    line.pop(4)
    line_list.append(line)

df = pd.DataFrame(data = line_list,columns=["ID", "Year/DOY", "Time", "Source_IP", "Dest_IP", "Protocols", "Length", "Info"])
df.to_csv('data.csv', index=False)