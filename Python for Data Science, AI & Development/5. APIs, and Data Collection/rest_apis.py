import requests
import os 
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)
print(r.status_code)
print(r.request.headers)
print("request body:", r.request.body)
header = r.headers
print(header['date'])
print(header['Content-Type'])
print(r.encoding)
print(r.text[0:100])

url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'
r=requests.get(url)
print(r.headers)
print(r.headers['Content-Type'])
path=os.path.join(os.getcwd(),'image.png')
print(path)
with open(path,'wb') as f:
    f.write(r.content)

#Image.open(path)

print("\nget\n")

url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)
print(r.url)
print("\nbody:\n\n",r.request.body)
print(r.status_code)
print(r.text)
print(r.headers['Content-Type'])
print(r.json())
print(r.json()['args'])

print("\npost\n")

url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)
print("POST url:",r_post.url)
print("GET url:",r.url)

print("POST body:",r_post.request.body)
print("GET body:",r.request.body)
#quick access to form
r_post.json()['form']