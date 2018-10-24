import requests
import json

url='https://api.github.com'

def build_url(endpoint):#拼接接口和地址
    return '/'.join([url, endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)#采用json里面提供的方法打印出来，格式更好看

def json_method():
    response=requests.patch(build_url('user'),auth=('1224169904@qq.com','030923bnm.'),json={'company':'haotest'})
    #response=requests.get(build_url('baiyali/030923bnm.'))
    print(better_output(response.text))

if __name__=='__main__':
    json_method()
    #request_method()
