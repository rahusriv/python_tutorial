import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver("127.0.0.1",'rahul','rahul12')
iosvl2.open()

ios_output = iosvl2.get_facts()

print(json.dumps(ios_output))