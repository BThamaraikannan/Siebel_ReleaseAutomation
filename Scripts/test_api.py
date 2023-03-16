#!/usr/bin/env python

import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

response  = requests.get("https://jsonplaceholder.typicode.com/todos/1")
#response = requests.get("http://api.open-notify.org/astros.json", verify=False)

#response = requests.get("https://100.100.181.24:8481/siebel/migration/login.html", verify=False)
print(response.json())
