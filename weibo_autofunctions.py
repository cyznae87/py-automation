from selenium import webdriver
import time

browser = webdriver.Chrome()


# function of auto login weibo
def weibo_login(username, password):
  # open weibo login page
  browser.get('https://passport.weibo.cn/signin/login')
  browser.implicitly_wait(5)
  time.sleep(1)
  # input username and password
  browser.find_element_by_id("loginName").send_keys(username)
  browser.find_element_by_id("loginPassword").send_keys(password)
  time.sleep(1)
  # click login 
  browser.find_element_by_id("loginAction").click()
  time.sleep(1)


# set username and password
username = '13190331226'
password = "cyzn631218"
weibo_login(username, password)



# follow a specific user
def add_follow(uid):
  browser.get('https://m.weibo.com/u/' + str(uid))
  time.sleep(1)
  follow_button = browser.find_element_by_xpath('//div[@class="m-add-box m-followBtn"]')
  follow_button.click()
  time.sleep(1)
  # select the first group for now
  group_ckb = browser.find_element_by_xpath('//label[@class="m-checkbox"]')
  group_ckb.click()
  time.sleep(1)
  # confirm
  confirm_button = browser.find_element_by_link_text("确定")
  print('conbtn', confirm_button)
  confirm_button.click()
  time.sleep(1)


# 每天学点心理学 UID
uid = '1890826225'
add_follow(uid)


# 给指定某条微博添加内容
def add_comment(weibo_url, content):
  browser.get(weibo_url)
  browser.implicitly_wait(5)
  content_textarea = browser.find_element_by_css_selector("textarea.W_input").clear()
  content_textarea = browser.find_element_by_css_selector("textarea.W_input").send_keys(content)
  time.sleep(2)
  comment_button = browser.find_element_by_css_selector(".W_btn_a").click()
  time.sleep(1)


# 发文字微博
def post_weibo(content):
  # 跳转到用户的首页
  browser.get('https://weibo.com')
  browser.implicitly_wait(5)
  # 点击右上角的发布按钮
  post_button = browser.find_element_by_css_selector("[node-type='publish']").click()
  # 在弹出的文本框中输入内容
  content_textarea = browser.find_element_by_css_selector("textarea.W_input").send_keys(content)
  time.sleep(2)
  # 点击发布按钮
  post_button = browser.find_element_by_css_selector("[node-type='submit']").click()
  time.sleep(1)


# 给指定的微博写评论
weibo_url = 'https://weibo.com/1890826225/HjjqSahwl'
content = 'Gook Luck! 好运已上路！'
# 自动发微博
content = '每天学点心理学'
post_weibo(content)