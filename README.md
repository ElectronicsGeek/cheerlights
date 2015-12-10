cheerlights
---
Python wrapper for accessing the cheerlights API.

### Dependencies:
- requests

### Usage:
You can create an instance of the cheerlights API like so:

    cl = Cheerlights()
You can then:

- Get the last colour's name as a string:

        cl.last_color_name
- Get the last colour as a hex string:

        cl.last_color_hex
- Get the last colour as a list containing its red, green and blue components:

        cl.last_color_rgb
        
