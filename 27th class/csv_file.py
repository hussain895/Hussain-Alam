import csv
# fields=['NAME','BRANCH','YEAR' ,  'CGPA']
# rows=[['Nikhil', 'COE' , '2'   ,  '9.0' ],
#       ['Sanchit', 'COE', '2'   ,  '9.1' ],
#       ['Aditya',  'IT' , '2'   ,  '9.3' ],
#       ['Sagar',   'SE' , '1'   ,  '9.5' ],
#       ['Prateek','MCE' , '3'   ,  '7.8' ],
#       ['Sahil',   'EP',  '2'   ,  '9.1']]

filename="student.csv"

# with open(filename,'w') as csvfile:
#     csvwriter=csv.writer(csvfile)
#     csvwriter.writerow(fields)
#     csvwriter.writerows(rows)


# convert this into dictionary format

# import csv
# fields=['NAME','BRANCH','YEAR' ,  'CGPA']
# rows=[{'NAME':'Nikhil', 'BRANCH':'COE' , 'YEAR':'2'   ,  'CGPA':'9.0' },
#       {'NAME':'Sanchit', 'BRANCH':'COE', 'YEAR':'2'   ,  'CGPA':'9.1' },
#       {'NAME':'Aditya',  'BRANCH':'IT' , 'YEAR':'2'   ,  'CGPA':'9.3' },    
#         {'NAME':'Sagar',   'BRANCH':'SE' , 'YEAR':'1'   ,  'CGPA':'9.5' },
#         {'NAME':'Prateek','BRANCH':'MCE' , 'YEAR':'3'   ,  'CGPA':'7.8' },
#         {'NAME':'Sahil',   'BRANCH':'EP',  'YEAR':'2'   ,  'CGPA':'9.1'}]

# filename="student_dict.csv"
# with open(filename,'w') as csvfile:
#     csvwriter=csv.DictWriter(csvfile,fieldnames=fields)
#     csvwriter.writeheader()
#     csvwriter.writerows(rows)

with open(filename,'r') as csvfile:
    csvreader=csv.DictReader(csvfile)
    header=next(csvreader)
    print(header)
    for row in csvreader:
        print(row)