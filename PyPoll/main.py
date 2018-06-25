#Importing the necessary modules
import csv
import math

#Initialising the variables
voter_id=[]
candidate=[]
votes=0
k=[]
summary={}

#Reading the csv file 
with open('election_data.csv', mode='r') as infile:
    reader = csv.reader(infile)
    csv_header=next(reader)             #CSV file has header in the first row
    for row in reader:
        votes=votes+1                   #Counting the rows to count the total number of votes
        voter_id.append(int(row[0]))    #Converting Voters_id column into a list 
        candidate.append(row[2])        #Converting candidate column into a list
    for i in set(candidate):            #Finding the unique candidate names
        k.append(candidate.count(i))    #Finding the uniques candidates's number of accourance in the candidate list
    summary=dict(zip(set(candidate),k)) #Creating a Summary dictionary to hold unique candidate names and their number of accourance
    sorted_summary=sorted(summary,key=summary.get,reverse=True) #Sorting the summary dictionary in decending order
    


    #Printing the results to the terminal
    print("Election Results \n.........................\nTotal Vote : "+str(votes)+"\n.........................")
    for i in sorted_summary:
        print(i+":"+str(round((summary[i]/votes)*100,2))+"%"+"("+str(summary[i])+")")
    print("..........................\nWinner: "+sorted_summary[0]+"\n...........................")
    
    #Writing the results into a text file to export.
    with open("outputfile.txt",'w') as op:
        op.write("Election Results \n.........................\nTotal Vote : "+str(votes)+"\n.........................\n")
        for i in sorted_summary:
            op.write(i+":"+str(round((summary[i]/votes)*100,2))+"%"+"("+str(summary[i])+")"+"\n")
        op.write("..........................\nWinner: "+sorted_summary[0]+"\n...........................")
    