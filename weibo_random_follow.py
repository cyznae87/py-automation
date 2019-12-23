import tkinter as tk
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def execute_message():

    label1 = tk.Label(root, text= '自动关注200次....', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)

def weibo_login(username, password):
    #open weibo desktop page
    browser.get('https://www.weibo.com/')
    browser.implicitly_wait(5)
    


def random_follow():
    #for now follow 200 times
    for i in range(200):
        follow_button = browser.find_element_by_xpath('//a[@class="W_btn_b"]')
        follow_button.click()
        time.sleep(1)

def run():
    #start random following
    execute_message()
    random_follow()



button1 = tk.Button(text='开始自动关注',command=run, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()

#no username or password passed to weibo_login for now
weibo_login('', '')

