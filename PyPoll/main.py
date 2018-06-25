
import csv
import math
voter_id=[]
candidate=[]
votes=0
k=[]
summary={}
with open('election_data.csv', mode='r') as infile:
    reader = csv.reader(infile)
    csv_header=next(reader)
    for row in reader:
        votes=votes+1
        voter_id.append(int(row[0]))
        candidate.append(row[2])
    for i in set(candidate):
        k.append(candidate.count(i))
    summary=dict(zip(set(candidate),k))
    sorted_summary=sorted(summary,key=summary.get,reverse=True)
    
    print("Election Results \n.........................\nTotal Vote : "+str(votes)+"\n.........................")
    for i in sorted_summary:
        print(i+":"+str(round((summary[i]/votes)*100,2))+"%"+"("+str(summary[i])+")")
    print("..........................\nWinner: "+sorted_summary[0]+"\n...........................")
    
    with open("outputfile.txt",'w') as op:
        op.write("Election Results \n.........................\nTotal Vote : "+str(votes)+"\n.........................\n")
        for i in sorted_summary:
            op.write(i+":"+str(round((summary[i]/votes)*100,2))+"%"+"("+str(summary[i])+")"+"\n")
        op.write("..........................\nWinner: "+sorted_summary[0]+"\n...........................")
    