import json
import os

import requests



def build_family_tree(json_file_location, api_post_endpoint):
    for root, directories, files in os.walk(json_file_location):
        for f in files:
            pathname = os.path.join(root, f)
            with open(pathname, 'r') as json_file:
                json_dict = json.loads(json_file.read())
            resp = requests.post(api_post_endpoint, json=json_dict)
            assert resp.status_code == 200



if __name__ == '__main__':
    json_file_location = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                  'json_files')
    endpoint = 'http://localhost:5000/person/crud'
    build_family_tree(json_file_location, endpoint)
