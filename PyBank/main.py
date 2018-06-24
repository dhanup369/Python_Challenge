import csv
#Reading from the CSV file
with open ('budget_data.csv','r')as file:
     reader=csv.reader(file)
     csv_header=next(reader) #CSV file has header in the first row.
     
     #Initializing all the variables
     month_count=0
     total=0
     profit=[]
     diff=0
     month=[]
     
     
     for row in reader:
         month_count=month_count+1    #Counting the number of rows for counting the number of months
         total=total+int(row[1])      #Finding the total profits
         profit.append(int(row[1]))   #Converting the profit column into a list 
         month.append(row[0])         #Converting the month column into a list
         
     for i in range(len(profit)-1):
         diff=diff+(profit[i+1]-profit[i])   #Calculating the change of profit between months over the entire period
     average_diff=diff/(len(profit)-1)       #Calculating the average change of profit
     max=max(profit)                         #Finding the maximum value of Profit
     x=profit.index(max)                     #Finding the index of maximum Profit
     min=min(profit)                         #Finding the minimum value of Profit
     y=profit.index(min)                     #Finding the index of minimum Profit
     

     #Printing the analysis to the Terminal 
     print("Financial Analysis: \n......................................")
     print("Total Months: ",month_count)
     print("Total: $"+str(total))
     print("Average Change: $"+str(average_diff))
     print("Greatest increase in profits: ",month[x],"($"+str(max)+")")
     print("Greatest decrease in profits: ",month[y],"($"+str(min)+")")
     

     #Writing the results into a text file to export.
     with open("outputfile.txt",'w') as op:
         op.write("Financial Analysis:\n")
         op.write("...........................\n")
         op.write("Total Months: "+str(month_count)+"\n")
         op.write("Total: $"+str(total)+"\n")
         op.write("Average Change: $"+str(average_diff)+"\n")
         op.write("Greatest increase in profits: "+str(month[x])+"($"+str(max)+")"+"\n")
         op.write("Greatest decrease in profits: "+str(month[y])+"($"+str(min)+")"+"\n")
