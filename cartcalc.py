import requests
import json
import pprint


url = "https://lt-support.revelup.com/specialresources/cart/calculate/"


headers = {
      "content-type": "application/json",
    "accept": "application/json",
    "API-AUTHENTICATION":"secre:secret"
   
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



