import csv
with open ('budget_data.csv','r')as file:
     reader=csv.reader(file)
     csv_header=next(reader)
     month_count=0
     total=0
     profit=[]
     diff=0
     
     
     for row in reader:
         month_count=month_count+1
         total=total+int(row[1])
         profit.append(int(row[1]))
         
     for i in range(len(profit)-1):
         diff=diff+(profit[i+1]-profit[i])   
     average_diff=diff/(len(profit)-1)
     max=max(profit)
     print(max)
     min=min(profit)
     print(min) 
     print("Total Months: ",month_count)
     print("Total: $"+str(total))
     print("Average Change: $"+str(average_diff))