import csv
from datetime import datetime
with open ('employee_data.csv','r')as file:
     reader=csv.reader(file)
     csv_header=next(reader) #CSV file has header in the first row.
     
     emp_id=[]
     emp_name=[]
     emp_DOB=[]
     new_DOB=[]
     emp_ssn=[]
     new_ssn=[]
     emp_state=[]
     new_state=[]
     f_n=[]
     l_n=[]

     for row in reader:
         emp_id.append(row[0])
         emp_name.append(row[1])
         emp_DOB.append(row[2])
         emp_ssn.append(row[3])
         emp_state.append(row[4])
     for i in emp_name:
         f_n.append(i.split()[0])
         l_n.append(i.split()[1])
     for i in emp_DOB:
        n=datetime.strptime(i,'%Y-%m-%d').strftime('%m/%d/%Y')
        new_DOB.append(n)
     for i in emp_ssn:
         i='***-**-'+i[7:]
         new_ssn.append(i)
     abbr = {'District of Columbia': 'DC',
    'Alabama': 'AL',
    'Montana': 'MT',
    'Alaska': 'AK',
    'Nebraska': 'NE',
    'Arizona': 'AZ',
    'Nevada': 'NV',
    'Arkansas': 'AR',
    'New Hampshire': 'NH',
    'California': 'CA',
    'New Jersey': 'NJ',
    'Colorado': 'CO',
    'New Mexico': 'NM',
    'Connecticut': 'CT',
    'New York': 'NY',
    'Delaware': 'DE',
    'North Carolina': 'NC',
    'Florida': 'FL',
    'North Dakota': 'ND',
    'Georgia': 'GA',
    'Ohio': 'OH',
    'Hawaii': 'HI',
    'Oklahoma': 'OK',
    'Idaho': 'ID',
    'Oregon': 'OR',
    'Illinois': 'IL',
    'Pennsylvania': 'PA',
    'Indiana': 'IN',
    'Rhode Island': 'RI',
    'Iowa': 'IA',
    'South Carolina': 'SC',
    'Kansas': 'KS',
    'South Dakota': 'SD',
    'Kentucky': 'KY',
    'Tennessee': 'TN',
    'Louisiana': 'LA',
    'Texas': 'TX',
    'Maine': 'ME',
    'Utah': 'UT',
    'Maryland': 'MD',
    'Vermont': 'VT',
    'Massachusetts': 'MA',
    'Virginia': 'VA',
    'Michigan': 'MI',
    'Washington': 'WA',
    'Minnesota': 'MN',
    'West Virginia': 'WV',
    'Mississippi': 'MS',
    'Wisconsin': 'WI',
    'Missouri': 'MO',
    'Wyoming': 'WY'}
     for i in emp_state:
         if i in abbr.keys():
             i=abbr[i]
             new_state.append(i)
     
     rows=zip(emp_id,f_n,l_n,new_DOB,new_ssn,new_state)
     with open('employee_data2.csv', 'w', newline='') as csvfile:
     

    # Initialize csv.writer
            csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
            csvwriter.writerow(['Emp ID','First Name', 'Last Name','DOB','SSN','State'])
            csvwriter.writerows(list(rows))
