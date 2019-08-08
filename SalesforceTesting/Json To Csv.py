import json
import csv

class JsonToCsv:
    pstr_filepath = "F:\\PythonPractice\\SalesforceTesting\\testdata\\sf_accounts_demo.json"
    with open(pstr_filepath, 'r') as config_json:
        dataJson = json.load(config_json)
    mydict = [dataJson['create_account_data']['Account Information']]
    print(mydict)
    fieldnames = []
    print(type(fieldnames))
    for x in dataJson['create_account_data']['Account Information'].keys():
        fieldnames.append(x)
    print(fieldnames)
    fieldnames1 =[dataJson['create_account_data']['Account Information'].keys()]
    print(fieldnames1)
    with open('names.csv', 'w', newline='') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(mydict)


    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # writer.writeheader()
    # writer.writerows(mydict)










