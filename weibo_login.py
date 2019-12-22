from selenium import webdriver
import time
browser = webdriver.Chrome()

# 登陆微博
def weibo_login(username, password):
    # 打开微博登陆界面
    browser.get('https://passport.weibo.cn/signin/login')
    # 隐性等待。隐形等待是设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止。
    # 隐性等待对整个driver的周期都起作用，所以只要设置一次即可。
    browser.implicitly_wait(5)
    time.sleep(1)
    # 填写登陆信息：用户名，密码
    browser.find_element_by_id('loginName').send_keys(username)
    browser.find_element_by_id('loginPassword').send_keys(password)
    time.sleep(1)
    # 点击登陆
    browser.find_element_by_id('loginAction').click()
    time.sleep(1)

# test
# 自己微博的账号密码
username = '13190331226'
password = 'cyzn631218'
weibo_login(username,password)