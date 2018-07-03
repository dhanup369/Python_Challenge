import csv
#Reading from the CSV file
with open ('budget_data.csv','r')as file:
     reader=csv.reader(file)
     csv_header=next(reader) #CSV file has header in the first row.
     
     #Initializing all the variables
     month_count=0
     total=0
     profit=[]
     aver=0
     month=[]
     change=[]
     
     for row in reader:
         month_count=month_count+1    #Counting the number of rows for counting the number of months
         total=total+int(row[1])      #Finding the total profits
         profit.append(int(row[1]))   #Converting the profit column into a list 
         month.append(row[0])         #Converting the month column into a list
         
     for i in range(len(profit)-1):
         diff=(profit[i+1]-profit[i])   #Calculating the change of profit between months over the entire period
         aver=aver+diff                 #Recursive addition of the differences to find the average  
         change.append(diff)            #Adding the differnces in a list 
     average_diff=aver/(len(profit)-1)       #Calculating the average change of profit
     maxi=max(change)                         #Finding the maximum value of the difference
     x=change.index(maxi)                     #Finding the index of maximum difference 
     mini=min(change)                         #Finding the minimum value of difference
     y=change.index(mini)                     #Finding the index of minimum difference
     
     
     #Printing the analysis to the Terminal 
     print("Financial Analysis: \n......................................")
     print("Total Months: ",month_count)
     print("Total: $"+str(total))
     print("Average Change: $"+str(average_diff))
     print("Greatest increase in profits: ",month[x+1],"($"+str(maxi)+")")
     print("Greatest decrease in profits: ",month[y+1],"($"+str(mini)+")")
     

     #Writing the results into a text file to export.
     with open("outputfile.txt",'w') as op:
         op.write("Financial Analysis:\n..............................\n")
         op.write("Total Months: "+str(month_count)+"\n")
         op.write("Total: $"+str(total)+"\n")
         op.write("Average Change: $"+str(average_diff)+"\n")
         op.write("Greatest increase in profits: "+str(month[x+1])+"($"+str(maxi)+")"+"\n")
         op.write("Greatest decrease in profits: "+str(month[y+1])+"($"+str(mini)+")"+"\n")
    