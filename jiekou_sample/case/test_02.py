# coding:utf-8
import unittest
import requests
from common.logger import Log

class Test(unittest.TestCase):
    u'''测试2'''
    log = Log()
    def setUp(self):
        pass
    def test_a(self):
        u'''判断 a in b'''
        self.log.info("------start!--------")
        self.log.info("测试hello 在hello world里")
        a='hello'
        b='hello world'
        self.assertIn(a,b)
        self.log.info("------end!--------")
    def test_true(self):
        u'''判断a is True ,失败案例'''
        self.log.info("------start!--------")
        self.log.info("测试a为False失败案例")
        a=True
        self.assertFalse(a)
        self.log.info("------end!--------")

if __name__ == "__main__":
   unittest.main()
