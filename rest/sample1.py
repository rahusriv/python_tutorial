import requests
import json
resp = requests.get('https://www.google.com/search?source=hp&ei=NI-wW-GVItm4rQHrv5C4DA&q=abc&oq=abc&gs_l=psy-ab.3..0i67k1l5j0i131i67k1j0i67k1j0i131k1l2j0i67k1.1114.1688.0.1912.4.3.0.0.0.0.179.425.0j3.3.0....0...1.1.64.psy-ab..1.3.424.0..0j35i39k1.0.VlvWcH3pMAU')
if resp.status_code != 200:
    # This means something went wrong.
    raise BaseException()#ApiError('GET /tasks/ {}'.format(resp.status_code))
#for todo_item in resp.json():
#    print('{} {}'.format(todo_item['id'], todo_item['summary']))

print(resp.__dict__)
