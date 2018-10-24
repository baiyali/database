import requests
import json

url = 'https://api.gitthub.com'

def build_url(endpoint):
    return '/'.join([url,endpoint])

def better_output(json_str):
    return json.dump(json.loads(json_str),indent=4)

def request_method():
    response = requests.get(build_url('users'))
    print(better_output(response.text))

if __name__=='__main__':
    request_method()