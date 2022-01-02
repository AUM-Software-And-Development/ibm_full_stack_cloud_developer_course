import pandas as pd

url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'
df = pd.read_csv(url)

print(df)

#formats
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
print(df)

print(df["First Name"])

df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
print(df)

# To select the first row
df.loc[0]
# To select the 0th,1st and 2nd row of "First Name" column only
df.loc[[0,1,2], "First Name" ]

print("\ntransforms\n")

import numpy as np
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print(df)

df = df.transform(func = lambda x : x + 10)
print(df)

result = df.transform(func = ['sqrt'])
print(result)

#json
import json
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}
with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f) #dump will serialize

json_object = json.dumps(person, indent = 4) 
print(json_object)
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 
    print(outfile)

with open('sample.json', 'r') as openfile:
    json_object = json.load(openfile)
  
print(json_object)
print(type(json_object))

#xlsx
import urllib.request

urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")
df = pd.read_excel("sample.xlsx")
print(df)

#xml
import xml.etree.ElementTree as ET
import xml.etree.ElementTree as etree

# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

# create a new XML file with the results
mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)

#more xml..
tree = etree.parse("Sample-employee-XML-file.xml")

root = tree.getroot()
columns = ["firstname", "lastname", "title", "division", "building","room"]

datatframe = pd.DataFrame(columns = columns)

for node in root: 

    firstname = node.find("firstname").text

    lastname = node.find("lastname").text 

    title = node.find("title").text 
    
    division = node.find("division").text 
    
    building = node.find("building").text
    
    room = node.find("room").text
    
    datatframe = datatframe.append(pd.Series([firstname, lastname, title, division, building, room], index = columns), ignore_index = True)

print(datatframe)
#save as csv
datatframe.to_csv("employee.csv", index=False)

#images
from PIL import Image 
urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")
img = Image.open('dog.jpg')