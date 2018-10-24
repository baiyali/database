import requests
import unittest

class Test_login(unittest.TestCase):
    url='https://passport.womai.com/login/login.do'

    headers={
            'Accept':'application/json,text/javascript,*/*',
            'Accept-Encoding':'gzip,deflate,br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive',
            'Content-Length':'170',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'passport.womai.com',
            'User-Agent':'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,like Gecko)Chrome/67.0.3396.99 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
    }
    payload={
            'serverPath':'http://www.womai.com/',
            'loginId':'baiyali_wmw',
            'password':'030923bnm.',
            'validateCode':'',
            'tempcode':'',
            'mid':'0',
            'returnUrl':'http://www.womai.com/index-31000-0.htm'
    }

    def test_login(self):
        response=requests.post(self.url,headers=self.headers,data=self.payload)
        json_data=response.json()
        print(json_data)

        # 断言：测试结果与期望结果对比
        self.assertEqual('2',json_data['msg'])#'msg':'2'

if __name__=='__main__':
    unittest.main()