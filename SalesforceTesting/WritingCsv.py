


# writing to csv file
import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


# name of csv file
filename = "university_records.csv"
with open(filename, 'w', newline='') as csvfile:
    fields = ['name', 'branch', 'year', 'cgpa']
    mydict = [{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
              {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
              {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
              {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
              {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
              {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    writer.writeheader()
    writer.writerows(mydict)
