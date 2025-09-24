from selenium import webdriver  #用于操作浏览器
from selenium.webdriver.chrome.options import Options  #用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
  #设置浏览器，启动浏览器
def she():

    q1 = Options()
    #禁用沙盒模式
    q1.add_argument('--no-sandbox')
    #保持浏览器打开状态
    q1.add_experimental_option('detach', True)
    #创建并启动浏览器
    a1  = webdriver.Chrome(service=Service('chromedriver.exe'), options=q1)


    return a1
  #获取用户输入的关键词
def get_user_input():
    # 提示用户输入，并返回输入的内容
    keyword = input("请输入：")
    # 简单验证，确保用户输入不为空
    while not keyword.strip():
        print("输入不能为空，请重新输入！")
        keyword = input("请输入：")
    return keyword
  #搜索
def search_key():
    #定位一个元素，定位多个elements,清空元素,元素输入,使用用户输入的值
    a2 = a1.find_element(By.ID, 'search-input')
    a2.clear()
    a2.send_keys(search_keyword)
    #点击
    a1.find_element(By.CLASS_NAME,'search-icon').click()
    time.sleep(2)
  #点赞
def xhs_like():
    like_buttons = a1.find_elements(By.CLASS_NAME, 'like-lottie')
    print(f"实际找到的点赞按钮数量：{len(like_buttons)}")  # 打印数量，方便排查

    # 关键修复2：按“实际元素数量”和“计划数量9”取较小值遍历，避免越界
    max_click = min(15, len(like_buttons))  # 最多点击9个，若不足则按实际数量
    for i in range(max_click):
        like_buttons[i].click()
        time.sleep(1)
  #评论
def discuss():
    # 自动评论
    a1.find_element(By.XPATH, '//*[@id="noteContainer"]/div[4]/div[3]/div/div/div[1]/div[1]/div/div/span').click()
    time.sleep(1)
    a1.find_element(By.ID, 'content-textarea').send_keys(content_textarea)
    time.sleep(1)
    # 使用按钮的完整XPath路径定位
    send_btn = a1.find_element(
        By.XPATH,
        '//*[@id="noteContainer"]/div[4]/div[3]/div/div/div[2]/div/div[2]/button[1]'
    )
    # 检查按钮是否可用
    if send_btn.is_enabled():
        send_btn.click()
        print("发送按钮点击成功")
    else:
        print("发送按钮当前不可用（disabled状态）")
    time.sleep(1)
  #关注
def at():
    # 先定位到文本元素
    text_span = a1.find_element(By.XPATH, '//*[@id="noteContainer"]/div[4]/div[1]/div/div[2]/button')
    # 获取文本内容并去除前后空格
    button_text = text_span.text.strip()

    # 判断文本是否为'关注'
    time.sleep(1)

    # 判断文本是否为'关注'
    if button_text == '关注':
        time.sleep(1)
        # 定位按钮并点击
        follow_btn = a1.find_element(By.CSS_SELECTOR, 'button.follow-button.large.primary')
        a1.execute_script("arguments[0].click();", follow_btn)
        print("已点击关注按钮")
    else:
        print(f"按钮文本为'{button_text}'，不执行点击")
    time.sleep(1)
  #详情页,关注，评论
def xhs_deli_at():
    #详情页元素
    deli = a1.find_elements(By.CSS_SELECTOR, 'a.cover.mask.ld')
    print(len(deli))
    for i in range(len(deli)):
        deli[i].click()
        time.sleep(4)
        print(f'点击{i}')
        # 点击关注
        at()
        #自动评论
        discuss()
        #使用esc按键
        a1.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        time.sleep(1)

  #调用方法获取用户输入的关键词
print("搜索内容")
search_keyword = get_user_input()
print("评论内容")
content_textarea = get_user_input()
  #创建浏览器实例
a1 = she()
  #色力你嗯
  #打开指定网址
a1.get('https://www.xiaohongshu.com/explore')
time.sleep(15)
  #首页搜索
search_key()
  #详情页关注，评论
xhs_deli_at()
  #点赞
xhs_like()



