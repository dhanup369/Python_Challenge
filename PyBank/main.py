import csv
with open ('budget_data.csv','r')as file:
     reader=csv.reader(file)
     csv_header=next(reader)
     month_count=0
     total=0
     profit=[]
     diff=0
     month=[]
     
     for row in reader:
         month_count=month_count+1
         total=total+int(row[1])
         profit.append(int(row[1]))
         month.append(row[0])
         
     for i in range(len(profit)-1):
         diff=diff+(profit[i+1]-profit[i])   
     average_diff=diff/(len(profit)-1)
     max=max(profit)
     x=profit.index(max)
     min=min(profit)
     y=profit.index(min)
     
     print("Financial Analysis: \n......................................")
     print("Total Months: ",month_count)
     print("Total: $"+str(total))
     print("Average Change: $"+str(average_diff))
     print("Greatest increase in profits: ",month[x],"($"+str(max)+")")
     print("Greatest decrease in profits: ",month[y],"($"+str(min)+")")
     
     with open("outputfile.txt",'w') as op:
         op.write("Financial Analysis:\n")
         op.write("...........................\n")
         op.write("Total Months: "+str(month_count)+"\n")
         op.write("Total: $"+str(total)+"\n")
         op.write("Average Change: $"+str(average_diff)+"\n")
         op.write("Greatest increase in profits: "+str(month[x])+"($"+str(max)+")"+"\n")
         op.write("Greatest decrease in profits: "+str(month[y])+"($"+str(min)+")"+"\n")
