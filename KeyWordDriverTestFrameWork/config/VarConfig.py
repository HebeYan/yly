

# 存储全局的变量
import os

# 项目根目录
projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 截图目录
exceptionPath = projectPath + r'/exceptionpictures'

# 驱动存放路径， 需要自己根据自己电脑的驱动为止修改
iePath = ''
chromePath = '/usr/bin/chromedriver.exe'
fireFox = ''

# excel文件存放路径
excelPath = projectPath + r'/testData/126mailSend.xlsx'
# loh文件存放路径
logPath = projectPath + '/log/'
# 测试用例部分列对应的列号
testCase_testCaseName = 2
testCase_testStepName = 4
testCase_testIsExecute = 5
testCase_testRunEndTime = 6
testCase_testResult = 7

# 用例步骤对应的列号
testStep_testNum = 1
testStep_testStepDescribe = 2
testStep_keyWord = 3
testStep_elementBy = 4
testStep_elementLocator = 5
testStep_operateValue = 6
testStep_testRunTime = 7
testStep_testResult = 8
testStep_testErrorInfo = 9
testStep_testErrorPic = 10
#邮件
smtp_server = 'smtp.qq.com'
port = 465
sender = '1023278689@qq.com'
#;psw是QQ邮箱的授权码
psw = 'tiukknlergcgbede'

#收件人多个时，中间用逗号隔开,如'a@xx.com,b@xx.com'
receiver = 'yanlingyu@51talk.com'

if __name__ == '__main__':
    print(projectPath)
    print(exceptionPath)
