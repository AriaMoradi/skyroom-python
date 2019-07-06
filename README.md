# skyroom-python

A library to ease skyroom api usage.

Link to api documentation: <a href="https://data.skyroom.online/help/webservice.html">Skyroom RESTful API Documention</a>


## Installation
<p> You can install this SDK from pypi through below command </p>


```
pip install skyroom
```
You can download the Python SDK <a href="https://github.com/KaveNegar/kavenegar-python/blob/master/kavenegar.py">Here</a> too
<p>
Then ,You need to make crate an account on Skyroom from <a href="https://www.skyroom.online/signup">Here</a>
</p>
<p>
After that you just need to ask for API-KEY from skyroom support.

## Usage

Here are some examples for api usage.

### getRooms
```python
from skyroom import *
try:
    api = SkyroomAPI('Your APIKey') # Example: apikey-71-819540-0f178abb0c712c4cfd5ae13e4c54687a
    response = api.getRooms()
    print(response)
except APIException as e: 
    print(e)
except HTTPException as e: 
    print(e)
```
### getRoom
```python
from skyroom import *
try:
    api = SkyroomAPI('Your APIKey') # Example: apikey-71-819540-0f178abb0c712c4cfd5ae13e4c54687a
    params = {
        'room_id': 1
    }
    response = api.getRoom(params)
    print(response)
except APIException as e: 
    print(e)
except HTTPException as e: 
    print(e)
```
### getRoomUrl
```python
from skyroom import *
try:
    api = SkyroomAPI('Your APIKey') # Example: apikey-71-819540-0f178abb0c712c4cfd5ae13e4c54687a
    params = {
        "room_id": 1,
        "language": "fa"
    }
    response = api.getRoom(params)
    print(response)
except APIException as e: 
    print(e)
except HTTPException as e: 
    print(e)
```

# Contribution
Bug fixes, docs, and enhancements are welcome! please open an issue.




