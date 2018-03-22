import json
import os

import bottle
import extruct


HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', 4001))
DEBUG = bool(os.environ.get('DEBUG', True))


def parse_microformats(message):
    parsed_microdata = extruct.extract(message)
    parsed_microdata = (
        parsed_microdata['microdata'] +
        parsed_microdata['json-ld']
    )
    return parsed_microdata


@bottle.post('/parse')
def parse():
    body = bottle.request.json
    results = parse_microformats(body['message'])
    print(results)
    results = []
    return json.dumps(results)


if __name__ == '__main__':
    bottle.run(host=HOST, port=PORT, debug=DEBUG)
