import requests
from base64 import b64encode
import json

data_string ="""{
  "taxCalculationRequest": {
    "INDATA": {
      "@version": "G",
      "INVOICE": {
        "COMPANY_ROLE": "B",
        "EXTERNAL_COMPANY_ID": "GB50",
        "CALCULATION_DIRECTION": "F",
        "CURRENCY_CODE": "USD",
        "INVOICE_DATE": "2019-03-29",
        "INVOICE_NUMBER": 234,
        "VENDOR_NAME": "Grey Wolf Studios Limited C0000267",
        "POINT_OF_TITLE_TRANSFER": "",
        "TRANSACTION_TYPE": "GS",
        "REGISTRATIONS": {
          "SELLER_ROLE": "GB157546778",
          "BUYER_ROLE": "GB678124612"
        },
        "SHIP_FROM": {
          "COUNTRY": "GB",
          "STATE": "",
          "CITY": "London",
          "POSTCODE": "NW6 7SG"
        },
        "LINE": [
          {
            "@ID": 346,
            "SHIP_TO": {
              "COUNTRY": "GB",
              "POSTCODE": "N1 9JY",
              "STATE": ""
            },
            "SUPPLY": {
              "COUNTRY": "GB",
              "POSTCODE": "N1 9JY"
            },
            "DESCRIPTION": "DS",
            "GROSS_AMOUNT": "11000.00",
            "LINE_NUMBER": "1",
            "PRODUCT_CODE": "81112003",
            "USER_ELEMENT": [
              {
                "NAME": "ATTRIBUTE31",
                "VALUE": "DS"
              },
              {
                "NAME": "ATTRIBUTE40",
                "VALUE": true
              }
            ],
            "QUANTITIES": {
              "QUANTITY": {
                "AMOUNT": "11.0",
                "UOM": "EA"
              }
            }
          },
          {
            "@ID": 347,
            "SHIP_TO": {
              "COUNTRY": "GB",
              "POSTCODE": "N1 9JY",
              "STATE": ""
            },
            "SUPPLY": {
              "COUNTRY": "GB",
              "POSTCODE": "N1 9JY"
            },
            "DESCRIPTION": "PP",
            "GROSS_AMOUNT": "10000.00",
            "LINE_NUMBER": "2",
            "PRODUCT_CODE": "83111506",
            "USER_ELEMENT": [
              {
                "NAME": "ATTRIBUTE31",
                "VALUE": "PP"
              },
              {
                "NAME": "ATTRIBUTE40",
                "VALUE": true
              }
            ],
            "QUANTITIES": {
              "QUANTITY": {
                "AMOUNT": "10.0",
                "UOM": "EA"
              }
            }
          },
          {
            "@ID": 348,
            "SHIP_TO": {
              "COUNTRY": "",
              "POSTCODE": "",
              "STATE": ""
            },
            "SUPPLY": {
              "COUNTRY": "GB",
              "POSTCODE": "N1 9JY"
            },
            "DESCRIPTION": "GS",
            "GROSS_AMOUNT": "1000.00",
            "LINE_NUMBER": "3",
            "PRODUCT_CODE": "42203600",
            "USER_ELEMENT": [
              {
                "NAME": "ATTRIBUTE31",
                "VALUE": "PP"
              },
              {
                "NAME": "ATTRIBUTE40",
                "VALUE": true
              }
            ],
            "QUANTITIES": {
              "QUANTITY": {
                "AMOUNT": "",
                "UOM": ""
              }
            }
          }
        ]
      }
    }
  }
}"""
#data_string = json.dumps(data)

#print(data_string)

data_dict = json.loads(data_string)
print(data_dict)
url = "https://iqvia-rwts-thomsonreuters-sys-1-0-qa.us-e1.cloudhub.io/api/calculatetax"

userAndPass = b64encode(b"6b5f7a5714d3420fa1c9992c0bf7ce42:22A42a80587c4Bb59e69c3899efbBDE7").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass ,
            'Content-Type': 'application/json'}

response = requests.post(url, json=data_dict, headers=headers)

print(response.status_code)
# Inspect some attributes of the `requests` repository
json_response = response.json()

tax_1 = json_response["taxCalculationResponse"]["OUTDATA"]["INVOICE"]["LINE"][0]

tax_details = tax_1["TAX"]["TAX_AMOUNT"]
print(tax_details)
print(type(json_response))
#repository = json_response['items'][0]
#print(f'Repository name: {repository["name"]}')  # Python 3.6+
#print(f'Repository description: {repository["description"]}')  # Python 3.6+
