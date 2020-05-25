# coding:utf-8
import unittest
import requests
from common.logger import Log
class Test_num(unittest.TestCase):
    u'''测试1'''
    log = Log()
    def setUp(self):
        pass

    def test_add(self):
        u'''测试加法'''
        self.log.info("测试加法")
        self.log.info("测试6+5与11比较")
        result=6+5
        hope=11
        # 断言：测试结果与期望结果对比
        self.assertEqual(result, hope)
    def test_divide(self):
        u'''测试除法'''
        self.log.info("----------start!-------")
        self.log.info("测试7/2与3.5比较")
        result=7/2
        hope=3.5
        self.assertEqual(result,hope)
        self.log.info("----------pass!-------")

if __name__ == "__main__":
    unittest.main()