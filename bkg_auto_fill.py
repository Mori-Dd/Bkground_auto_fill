import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(10) #10秒
#浏览器最大化
driver.maximize_window()
wait = WebDriverWait(driver, 10)
def news_content():
    data = xlrd.open_workbook('账号密码.xlsx')
    content_table = data.sheet_by_name('手游新闻内容')
    newstitle = content_table.cell(0, 1).value
    game = content_table.cell(1, 1).value
    source = content_table.cell(2, 1).value
    content = content_table.cell(3, 1).value
    return newstitle,game,source,content
def read_excel():
    data = xlrd.open_workbook('账号密码.xlsx')
    table = data.sheet_by_name('特殊后台')
    #获取行数
    ws = table.nrows
    for i in range(2,ws):
        title = table.cell(i,0).value
        url = table.cell(i,1).value
        account = table.cell(i, 2).value
        password = table.cell(i, 3).value
        yield {
            'title':title,
            'url': url,
            'account': account,
            'password': password
        }

def get_page(title,url,ac,ps,newstitle,game,source,content):

    if 'bianwanjia' in url:
        print('正在打开 :' + title)
        bianwanjia(url,ac,ps,newstitle,game,source,content)
    elif 'diyiyou' in url:
        print('正在打开 :' + title)
        diyiyou(url,ac,ps,newstitle,game,source,content)
    elif 'kaifu' in url:
        print('正在打开 :' + title)
        kaifu(url,ac,ps,newstitle,game,source,content)
    elif 'hao76' in url:
        print('正在打开 :' + title)
        hao76(url,ac,ps,newstitle,game,source,content)
    elif '17huang' in url:
        print('正在打开 :' + title)
        huang17(url,ac,ps,newstitle,game,source,content)
def bianwanjia(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.wrap.clear > div.user_box.fr > table > tbody > tr:nth-child(5) > td:nth-child(2) > input[type="submit"]:nth-child(1)')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        skip = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > table > tbody > tr:nth-child(2) > td > div > a')))
        skip.click()
        publish = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#leftmenu > li:nth-child(8) > a')))
        publish.click()
        add = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#user_menu > li > a')))
        add.click()
        news = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.wrap.clear > div.user_box.fr > div.user_main > table > tbody > tr:nth-child(2) > td > select > option:nth-child(3)')))
        news.click()
        addnews = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.wrap.clear > div.user_box.fr > div.user_main > table > tbody > tr:nth-child(3) > td > input')))
        addnews.click()

        #新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.wrap.clear > div.user_box.fr > div.user_main > form > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        title.clear()
        title.send_keys(newstitle)
        # 新闻关键字
        keys = driver.find_element_by_name("keyboard")
        keys.send_keys(game)
        # 新闻内容
        keys = driver.find_element_by_name("smalltext")
        keys.send_keys(content)
        # 新闻作者
        keys = driver.find_element_by_name("writer")
        keys.send_keys(source)
        #新闻来源
        keys = driver.find_element_by_name("befrom")
        keys.send_keys(source)
        input('提交完按回车确认进入下一家'+'\n')
    except TimeoutException:
        return bianwanjia(url,ac,ps,newstitle,game,source,content)
def diyiyou(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.container2.clearfix > div > div > div.xz > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.container2.clearfix > div > div > div.xz > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.container2.clearfix > div > div > div.xz > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > input.fb_btn.xyb.normal_btn')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        addnews = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'body > div.container.clearfix > div.nav.clearfix > ol:nth-child(2) > li:nth-child(1) > a')))
        addnews.click()
        publish = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'body > div.container.clearfix > div.main.clearfix > div > div > div.tit > a')))
        publish.click()


        #新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#title')))
        title.clear()
        title.send_keys(newstitle)
        # 新闻关键字
        keys = driver.find_element_by_name("keyword")
        keys.send_keys(game)
        #选择新闻类别
        kind = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '#type > option:nth-child(3)')))
        kind.click()
        ios = driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[4]/td[2]/span/input[1]')
        android = driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[4]/td[2]/span/input[2]')
        ios.click()
        android.click()
        # 新闻游戏名
        keys = driver.find_element_by_name("gamename")
        keys.send_keys(game)
        # 新闻来源
        keys = driver.find_element_by_name("sources")
        keys.send_keys(source)
        # 新闻内容
        keys = driver.find_element_by_name("content_desc")
        keys.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')

    except TimeoutException:
        return diyiyou(url,ac,ps,newstitle,game,source,content)
def kaifu(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#user')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = driver.find_element_by_class_name('loginbut')
        act.send_keys(ac)
        psd.send_keys(ps)
        work = True
        while work == True:
            input('请输入验证码后再回车'+'\n')
            login.click()
            time.sleep(2)
            if EC.alert_is_present()(driver):
                driver.switch_to_alert().accept()
                print('验证码不正确，请重新输入')
                work = True
                continue
            work = False

        addnews = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'body > div.content.poublish > div.left-mune > div.mune-list.listblue > a')))
        addnews.click()
        #新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#title')))
        title.clear()
        title.send_keys(newstitle)
        # 新闻内容
        keys = driver.find_element_by_name("instructions")
        keys.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return kaifu(url,ac,ps,newstitle,game,source,content)
def hao76(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div > form > div.form-area > div:nth-child(1) > input')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div > form > div.form-area > div:nth-child(2) > input')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div > form > div.form-area > button')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        skit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#href')))
        skit.click()
        time.sleep(3)
        addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.content > div.page-header > div > div > a:nth-child(2)')))
        addnews.click()
        #新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#name')))
        title.clear()
        title.send_keys(newstitle)
        # 新闻内容
        keys = driver.find_element_by_name("info")
        keys.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return hao76(url,ac,ps,newstitle,game,source,content)
def huang17(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])

        work = True
        while work == True:
            act = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#login-box > div.login-main > form > dl > dd:nth-child(2) > input[type="text"]')))
            act.clear()
            psd = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#login-box > div.login-main > form > dl > dd:nth-child(4) > input')))
            psd.clear()
            login = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#login-box > div.login-main > form > dl > dd:nth-child(8) > button')))
            act.send_keys(ac)
            psd.send_keys(ps)
            input('请输入验证码后再回车' + '\n')
            login.click()
            time.sleep(2)
            if driver.current_url == 'http://www.17huang.com/dede/login.php':
                print('验证码不正确，请重新输入')
                work = True
                continue
            work = False
        time.sleep(4)
        driver.switch_to.frame("menu")

        addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#items2_1 > ul > li > div > div.fllct > a')))
        addnews.click()


        #新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#title')))
        title.clear()
        title.send_keys(newstitle)
        # 新闻简略标题
        keys = driver.find_element_by_name("shorttitle")
        keys.send_keys(game)
        # 新闻来源
        keys = driver.find_element_by_name("source")
        keys.send_keys(source)
        # 新闻作者
        keys = driver.find_element_by_name("writer")
        keys.send_keys(source)
        # 新闻主栏目
        keys = driver.find_element_by_class_name("option3")
        keys.click()
        # 新闻内容
        keys = driver.find_element_by_name("description")
        keys.send_keys(content)
        # 相关游戏
        keys = driver.find_element_by_name("game_name")
        keys.send_keys(game)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return huang17(url,ac,ps,newstitle,game,source,content)




def choose_num():
    print('*************** 欢迎进入媒体后台自助系统 ***************')
    print('—————  1. 手游媒体  —————'+'\n'+'—————  2. 页游媒体  —————')
    print('请选择要操作的媒体类型：')
    work = True
    while work == True:
        num = input()
        if num == '1':
            work = False
            return 1

        elif num == '2':
            work = False
            return 2
        else:
            print('请输入正确的选项')
            work = True




def main():
    newstitle, game, source, content = news_content()
    # num = choose_num()

    # if num == 1:
    for item in read_excel():
        get_page(item['title'],item['url'],item['account'],item['password'],newstitle,game,source,content)
    input('全部后台操作完毕，确认请按回车结束本程序'+'\n')
    # elif num == 2:
    #     print('2还没有写好')
    #     input('全部后台操作完毕，确认关闭本程序' + '\n')

# if __name__ == '__main__':
#     main()
main()
