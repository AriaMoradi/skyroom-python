# skyroom-python

A library to ease skyroom api usage.

Link to api documentation: [Skyroom RESTful API Documention](https://data.skyroom.online/help/webservice.html) 


## Installation
You can install this SDK from pypi through the command below

```
pip install skyroom
```

In order to use the api you need an API key. To obtain one you need to create an account on [Skyroom](https://www.skyroom.online/signup) and ask for your API key from the skyroom support.

## Usage

Here are some examples for api usage(all methods use the same signature).

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
I no longer use this library in my code. If there are any updates on the upstream from skyroom you can add support for it by opening a pull request.

Anyways, Bug fixes, docs, and enhancements are allways welcome! just open an issue.



