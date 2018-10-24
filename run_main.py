import unittest
import os
import time
import HTMLTestRunner

'''优化后执行所有用例并发送报告
  1.加载用例
  2.执行用例
  3。获取最新测试报告
  4.发送邮箱
  '''

#当前脚本所在文件的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))

def add_case(caseName='case',rule='test*.py'):
    #用例文件夹
    case_path = os.path.join(cur_path,caseName)
    #如果case文件夹不存在就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print('test case path:%s'%case_path)
    #定义方法的参数 discover发现某一个路径下面符合所有条件的内容
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    print(discover)
    return discover

def run_case(all_case,reportName='report'):
    #执行所有的用例，并把所有的结果写入HTML测试报告
    #now = time.strftime('%Y-%m-%d-%H-%M-%S')
    #用例文件夹
    report_path = os.path.join(cur_path,reportName)
    #如果不存在就自动创建一个
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path,'result.html')#+now
    print('report path:%s'%report_abspath)
    fp = open(report_abspath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告，测试结果如下：',description=u'用例执行情况')

    #调用add_case函数返回值
    runner.run(all_case)
    fp.close()

if __name__=='__main__':
    #加载用例
    all_case = add_case()
    #生成测试报告路径  执行用例
    run_case(all_case)