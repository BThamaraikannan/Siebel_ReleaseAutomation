import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


session = requests.Session()

headers = {'Content-Type': 'application/json'}

data = {
 "watermarkFilename": "UAT_WM_14Mar2023.txt",
 "packageFilename": "R23_3_14Mar2023.zip",

}


#response = session.post("https://100.100.176.126:8481/siebel/v1.0/migration/execution/export_incremental_runtime_repository", headers=headers, json=data, verify=False)
response = session.post("https://SADMIN:SADMIN2017@100.100.176.126:8481/siebel/v1.0/migration/execution/export_incremental_runtime_repository", headers=headers, json=data, verify=False)
print(response.status_code)

if response.status_code == 200:
    # Successfully logged in
    data = response.json()
    print("success")
else:
    # Error occurred
    print(response.text)
