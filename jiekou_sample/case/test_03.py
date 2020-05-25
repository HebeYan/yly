import requests
import unittest
from common.logger import Log
from lxml import etree
class Test(unittest.TestCase):
    '''sdk'''
    log=Log()

    def login(self):
        url1 = 'https://cas.zuoyebang.cc/login?service=http://qa-adx2.suanshubang.com/adx-admin/auth-callback'
        url2 = 'https://cas.zuoyebang.cc/login'
        r1 = requests.get(url1, verify=False)
        demo = etree.HTML(r1.content)
        nodes = demo.xpath("//input[@id='lt']")
        lt = nodes[0].get('value')
        nodes2 = demo.xpath('//input[@id="service"]')
        service = nodes2[0].get('value')
        body = {
            'username': 'yanlingyu',
            'password': 'Yanly6900-',
            'lt': lt,
            'service': service,
            'from': ''
        }
        r = requests.post(url2, data=body, allow_redirects=False, verify=False)
        location = r.headers['Location']
        print(location)
        r2 = requests.get(location, allow_redirects=False)
        return r2.cookies['sid']
    def setUp(self):
        sid=self.login()
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
            'cookie': 'sid=%s'%sid
        }
    def test_modify(self):
        '''sdk修改,修改编号1048的sdk'''
        self.url='http://qa-adx2.suanshubang.com/adx-resource/sdk/position/update'
        self.log.info("测试的url地址：%s"%self.url)
        body = {
            "adxPositionId": "",
            "app": "",
            "system": "",
            "type": 0,
            "requestCount": '-1',
            "status": 1,
            "remark": "1",
            "priority": 1,
            "sdkPositionId": "6040440949805533",
            "id": "1048"
        }
        r=requests.post(self.url,headers=self.headers,json=body)
        result=r.json()
        self.log.info("获取请求结果 %s"%result)
        data=result['data']
        self.log.info("获取%s值与1进行比较" % data)
        self.assertTrue(data,1)

if __name__=='__main__':
    unittest.main()
