import requests
import json
import pprint


url = "https://lt-support.revelup.com/specialresources/cart/calculate/"


headers = {
      "content-type": "application/json",
    "accept": "application/json",
    "API-AUTHENTICATION":"0113cbd5267847c49fab01658e8c81cb:cb4e9fcf0a154a5fbfb70eb42c2bc4d1549aed0a50da47b7b42c2379d0c158c7"
   
}

payload = {
    "items": [
        {
            "modifieritems": [
                {
                   
                    "qty": 1,       
                    "modifier": 2709,
                    "modifier_price": 7
                   
        
                   
                }
            ],
                "barcode": 100023,
            "product": 8805,
           "product_name_override": "Chicken Cordon Bleu",
             "quantity": 1,
         
        }
    ],
    "establishmentId": 101,
    "skin": "weborder"
}


response = requests.post(url, json=payload, headers=headers)

print(response.text)



