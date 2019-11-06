All responses will have the form of
 '''json
 {
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"

 }

 Subsequent respones definitions will only detail the expected value of 'data fields'

 **Definition**
 'Get /devices'

 **Response**
 -  '200 OK' on success

 '''json
 [
    {
            "identifier": "floor-lamp"
            "name": "Floor Lamp",
            "device_type": "switch",
            "controller_gateway": "192.150.1.1"
    }

 '''

 **Definition**
 'POST /devices'

**Arguments**
- '"identifier":string' a globally unique identifier for the device
- '"name":string' a friendly device
- '"device_type'
...
