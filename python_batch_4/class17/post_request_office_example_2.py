import requests
from base64 import b64encode
import json

data_string =  """"{"integration-run": {"integration": {"code": "outbound.coupa.api.invoiceautomation"}}}"""


#data_string = json.dumps(data)

#print(data_string)

dict_temp = {
    'integration-run': {
        'integration': {
            'code': 'outbound.coupa.api.invoiceautomation'
        }
    }
}


#data_dict = json.loads(data_string)
#print(data_dict)
url = "https://iqvia-rwts-coupa-sys-1-0-qa.us-e1.cloudhub.io/api/integrationrun"

userAndPass = b64encode(b"3093f49d46dc46c28f0bb2edb251b247:fcFC99E274EF4Df99062dB346E2a3A1C").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass,
            'Content-Type': 'application/json'}

response = requests.post(url, json=dict_temp, headers=headers)

print(response.status_code)
# Inspect some attributes of the `requests` repository
json_response = response.json()

print(json_response)
#repository = json_response['items'][0]
#print(f'Repository name: {repository["name"]}')  # Python 3.6+
#print(f'Repository description: {repository["description"]}')  # Python 3.6+
