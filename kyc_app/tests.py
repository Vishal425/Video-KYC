
import json
def test():
    
    import requests

    BASE_URL = 'http://192.168.1.61//VGDocverify/VGKVerify.asmx'

    new_product = {
        "UserId": "3",
        "VerificationKey": "KARZA123",
        "Longitude": "21",
        "Latitude": "77",
        "Accuracy": "85",
        "App_Mode": "a",
        "Request From": "Mob",
        "Device_Id": "456",
        "DeviceInfo": "",
        "APICode": "aadhaar-consent",
        "Name": "Vishal"

    }

    response = requests.post(f"{BASE_URL}/Aadhaar", json=new_product)
    print(response.json())
    # return render(req,'nam.html')
    # return render(req,'nam.html')
