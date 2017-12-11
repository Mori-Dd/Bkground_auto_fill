from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd
import time
driver = webdriver.Chrome()
driver.set_page_load_timeout(20) #10秒
#浏览器最大化
# driver.maximize_window()
wait = WebDriverWait(driver, 20)
def news_content():
    data = xlrd.open_workbook('账号密码.xlsx')
    content_table = data.sheet_by_name('手游新闻内容')
    newstitle = content_table.cell(0, 1).value
    game = content_table.cell(1, 1).value
    source = content_table.cell(2, 1).value
    content = content_table.cell(3, 1).value
    return newstitle,game,source,content
def read_special_excel():
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
def read_part_excel():
    data = xlrd.open_workbook('账号密码.xlsx')
    table = data.sheet_by_name('部分后台')
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
    #手游特殊后台
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
    elif '11773' in url:
        print('正在打开 :' + title)
        bk11773(url,ac,ps,newstitle,game,source,content)
    #手游部分后台
    elif 'kuhou' in url:
        print('正在打开 :' + title)
        kuhou(url,ac,ps,newstitle,game,source,content)
    elif 'yyjia' in url:
        print('正在打开 :' + title)
        yyjia(url,ac,ps,newstitle,game,source,content)
    elif 'thisisgame' in url:
        print('正在打开 :' + title)
        thisisgame(url,ac,ps,newstitle,game,source,content)
    elif '1syou' in url:
        print('正在打开 :' + title)
        bk1syou(url,ac,ps,newstitle,game,source,content)
    elif 'fahao' in url:
        print('正在打开 :' + title)
        fahao(url,ac,ps,newstitle,game,source,content)
    elif 'ppswan' in url:
        print('正在打开 :' + title)
        ppswan(url,ac,ps,newstitle,game,source,content)
    elif 'yxrb' in url:
        print('正在打开 :' + title)
        yxrb(url,ac,ps,newstitle,game,source,content)
    elif 'youxiwangguo' in url:
        print('正在打开 :' + title)
        youxiwangguo(url,ac,ps,newstitle,game,source,content)
    elif '40407' in url:
        print('正在打开 :' + title)
        bk40407(url,ac,ps,newstitle,game,source,content)
    elif '4q5q' in url:
        print('正在打开 :' + title)
        bk4q5q(url,ac,ps,newstitle,game,source,content)
    elif 'twan' in url:
        print('正在打开 :' + title)
        twan(url,ac,ps,newstitle,game,source,content)
    elif 'youkelai' in url:
        print('正在打开 :' + title)
        youkelai(url,ac,ps,newstitle,game,source,content)
    elif 'youxichanye' in url:
        print('正在打开 :' + title)
        youxichanye(url,ac,ps,newstitle,game,source,content)
    elif 'gameres' in url:
        print('正在打开 :' + title)
        gameres(url,ac,ps,newstitle,game,source,content)
    elif '119.23.135.10' in url:
        print('正在打开 :' + title)
        bk8477(url,ac,ps,newstitle,game,source,content)
    elif 'gametanzi' in url:
        print('正在打开 :' + title)
        gametanzi(url,ac,ps,newstitle,game,source,content)
    elif '1g31' in url:
        print('正在打开 :' + title)
        bk1g31(url, ac, ps, newstitle, game, source, content)
    elif '77l' in url:
        print('正在打开 :' + title)
        bk77l(url, ac, ps, newstitle, game, source, content)
    elif '07076' in url:
        print('正在打开 :' + title)
        bk07076(url, ac, ps, newstitle, game, source, content)
    elif 'vshouyou' in url:
        print('正在打开 :' + title)
        vshouyou(url, ac, ps, newstitle, game, source, content)
    elif 'newyx' in url:
        print('正在打开 :' + title)
        newyx(url, ac, ps, newstitle, game, source, content)
    elif 'yeyun' in url:
        print('正在打开 :' + title)
        yeyun(url, ac, ps, newstitle, game, source, content)
    elif 'mumayi' in url:
        print('正在打开 :' + title)
        mumayi(url, ac, ps, newstitle, game, source, content)
    elif '3987' in url:
        print('正在打开 :' + title)
        bk3987(url, ac, ps, newstitle, game, source, content)
    elif 'juxia' in url:
        print('正在打开 :' + title)
        juxia(url, ac, ps, newstitle, game, source, content)
#手游特殊后台
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
        driver.switch_to.frame("menu")
        addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#items2_1 > ul > li > div > div.flrct > a > img')))
        addnews.click()
        driver.switch_to.default_content()
        driver.switch_to.frame("main")
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
def bk11773(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#AdminLogin_username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#AdminLogin_password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#city-form > table > tbody > tr.row.buttons > td:nth-child(2) > p > input[type="submit"]')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#wrapper > div.f24 > span > a')))
        addnews.click()
        #新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#updateform > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > input')))
        title.clear()
        title.send_keys(newstitle)
        #新闻短标题
        shorttitle = driver.find_element_by_name("game[short_title]")
        shorttitle.send_keys(game)
        # 新闻关键字
        keys = driver.find_element_by_name("game[keyword]")
        keys.send_keys(game)
        # 新闻内容
        news = driver.find_element_by_name("game[description]")
        news.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return bk11773(url,ac,ps,newstitle,game,source,content)
#手游部分后台
def kuhou(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pwd')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#gtco-header > div.gtco-container > div > div > div > div > div > div > div > div > form > div:nth-child(7) > div > a')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        skip = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div > div.bottom > a')))
        skip.click()

        addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#sideNav > li:nth-child(2) > a')))
        addnews.click()
        #新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#title')))
        title.clear()
        title.send_keys(newstitle)

        #选择游戏
        newsgame = driver.find_element_by_name("game_title")
        newsgame.click()
        newsgame = driver.find_element_by_name("searchword")
        newsgame.send_keys(game)

        choose = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#searchgamediv > button:nth-child(2)')))
        choose.click()
        time.sleep(1)
        choosegame = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#searchgamediv > p:nth-child(4) > a')))
        choosegame.click()
        # 新闻来源
        sourcegame = driver.find_element_by_name("copyfrom")
        sourcegame.send_keys(source)

        # 新闻内容
        news = driver.find_element_by_name("description")
        news.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return kuhou(url,ac,ps,newstitle,game,source,content)
def yyjia(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#loginsubmit')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        # skit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#href')))
        # skit.click()
        time.sleep(2)
        addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#main > ul > li:nth-child(2) > a > img')))
        addnews.click()
        #新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#news_title')))
        title.clear()
        title.send_keys(newstitle)
        # 新闻内容
        keys = driver.find_element_by_name("newsinfo[description]")
        keys.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return yyjia(url,ac,ps,newstitle,game,source,content)
def thisisgame(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#login > div > div.box > div.div1 > form > p.bnt > button.submit')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()

        skit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > table > tbody > tr:nth-child(2) > td > div > a')))
        skit.click()

        addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#sy_box > div:nth-child(2) > a')))
        addnews.click()
        #选择新闻栏目
        choose = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#changeclass > div > select > option:nth-child(2)')))
        choose.click()
        sure = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#changeclass > button')))
        sure.click()

        #新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div.main_box > div.right > form > div > div.manage_box > div:nth-child(1) > input[type="text"]')))
        title.clear()
        title.send_keys(newstitle)
        # 新闻内容
        keys = driver.find_element_by_name("smalltext")
        keys.send_keys(content)
        # 新闻来源
        keys = driver.find_element_by_name("befrom")
        keys.send_keys(source)
        # 新闻作者
        keys = driver.find_element_by_name("writer")
        keys.send_keys(source)
        #所属游戏
        games = driver.find_element_by_id('show')
        games.click()
        inputgame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#ajaxgame')))
        inputgame.clear()
        inputgame.send_keys('永恒之源')
        choosegame = driver.find_element_by_id('searchgame')
        choosegame.click()
        choosesure = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#gg > li > a')))
        choosesure.click()

        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return thisisgame(url,ac,ps,newstitle,game,source,content)
def bk1syou(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div > div.login_right > form > div > span.btn > input:nth-child(1)')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        skit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > table > tbody > tr:nth-child(2) > td > div > a')))
        skit.click()

        addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > table > tbody > tr > td:nth-child(1) > div > div:nth-child(5) > div.i_b_b_bottom > span:nth-child(3) > a:nth-child(2)')))
        addnews.click()
        #进入frame
        driver.switch_to_frame('ifm')
        #选择栏目
        choose = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div > div.t_middle > table > tbody > tr:nth-child(1) > td > select > option:nth-child(3)')))
        choose.click()
        choosegame = driver.find_element_by_name('Submit')
        choosegame.click()
        #新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.table > div.t_middle > form > table.editinfo > tbody > tr > td > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        title.clear()
        title.send_keys(newstitle)
        #游戏名
        gamename = driver.find_element_by_name('keyboard')
        gamename.send_keys(game)
        # 新闻内容
        keys = driver.find_element_by_name("smalltext")
        keys.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return bk1syou(url,ac,ps,newstitle,game,source,content)
def fahao(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#dosubmit')))
        md = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#code')))
        act.send_keys(ac)
        psd.send_keys(ps)
        md.send_keys('')
        time.sleep(1)
        login.click()
        skit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div > div.bottom > a')))
        skit.click()
        #发布新闻
        addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#memberArea > div.col-left.col-1.left-memu > ul:nth-child(2) > li:nth-child(1) > a')))
        addnews.click()
        #选择栏目
        column = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#catid > option:nth-child(4)')))
        column.click()
        time.sleep(1)
        #选择游戏
        column = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#myform > table > tbody > tr:nth-child(2) > td > input.button')))
        column.click()
        time.sleep(1)
        driver.switch_to_frame('atrDialogIframe_selectgid')
        inputgame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.pad-10 > form > table > tbody > tr > td > div > input.input-text')))
        inputgame.send_keys('弹弹堂')
        search = driver.find_element_by_name('dosubmit')
        search.click()
        choose = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.pad-10 > div > table > tbody > tr:nth-child(2) > td:nth-child(2)')))
        choose.click()
        time.sleep(1)
        #新闻标题
        title = driver.find_element_by_name('info[title]')
        title.send_keys(newstitle)
        # 新闻关键词
        keys = driver.find_element_by_name('info[keywords]')
        keys.send_keys(game)
        # 新闻关键词
        gamesource = driver.find_element_by_name('info[copyfrom]')
        gamesource.send_keys(source)
        # 新闻内容
        keys = driver.find_element_by_name("info[description]")
        keys.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return fahao(url,ac,ps,newstitle,game,source,content)
def ppswan(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#myform > input.log-in.fl.tc')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        time.sleep(4)
        addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#show_userinfo > li:nth-child(2) > a')))
        addnews.click()
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[-1])
        publish = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.card > table > tbody > tr > td:nth-child(3) > div.info > div > table > tbody > tr:nth-child(5) > td > a:nth-child(2)')))
        publish.click()
        # 新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.card > table > tbody > tr > td:nth-child(2) > div.info.ctable > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        title.clear()
        title.send_keys(newstitle)
        # 游戏名
        keys = driver.find_element_by_name("titlegame")
        keys.send_keys(game)
        # 关键字
        keys = driver.find_element_by_name("keyboard")
        keys.send_keys(game)
        # 新闻内容
        keys = driver.find_element_by_name("smalltext")
        keys.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return ppswan(url,ac,ps,newstitle,game,source,content)
def yxrb(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        time.sleep(2)
        addnews = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#newspecial')))
        addnews.click()
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return yxrb(url,ac,ps,newstitle,game,source,content)
def youxiwangguo(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        work = True
        while work == True:
            print('进入了')
            act = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#username')))
            act.clear()
            psd = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#password')))
            psd.clear()
            login = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#myform > div.login_btn > button')))
            act.send_keys(ac)
            psd.send_keys(ps)
            input('请输入验证码后再回车' + '\n')
            login.click()
            time.sleep(4)
            try:
                driver.set_page_load_timeout(2)
                if driver.current_url == 'http://www.youxiwangguo.com/e/member/login/':
                    print(driver.current_url)
                    print('验证码不正确，请重新输入')
                    work = True
                    continue
                elif driver.current_url == 'http://www.youxiwangguo.com/':
                    time.sleep(1)
                    js = 'window.open("http://www.youxiwangguo.com/e/member/tg/");'
                    driver.execute_script(js)
                    handles = driver.window_handles
                    driver.switch_to_window(handles[-1])
                    addnews = wait.until(EC.element_to_be_clickable(
                        (By.CSS_SELECTOR,
                         '#memberArea > div.col-auto > div > div.ctable > div > div > ul:nth-child(12) > li:nth-child(3) > a')))
                    addnews.click()
                    title = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '#tab > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
                    title.clear()
                    title.send_keys(newstitle)
                    # 游戏名
                    gamename = driver.find_element_by_name('keyboard')
                    gamename.send_keys(game)
                    # 新闻内容
                    keys = driver.find_element_by_name("smalltext")
                    keys.send_keys(content)
                    work = False
            except TimeoutException:
                time.sleep(1)
                js = 'window.open("http://www.youxiwangguo.com/e/member/tg/");'
                driver.execute_script(js)
                handles = driver.window_handles
                driver.switch_to_window(handles[-1])
                addnews = wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '#memberArea > div.col-auto > div > div.ctable > div > div > ul:nth-child(12) > li:nth-child(3) > a')))
                addnews.click()
                title = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '#tab > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
                title.clear()
                title.send_keys(newstitle)
                # 游戏名
                gamename = driver.find_element_by_name('keyboard')
                gamename.send_keys(game)
                # 新闻内容
                keys = driver.find_element_by_name("smalltext")
                keys.send_keys(content)
                work = False

        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return youxiwangguo(url,ac,ps,newstitle,game,source,content)
def bk40407(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#uname')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#pwd')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#imageField')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        #跳过
        skit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#out > div.tanchu_tit_130624 > div')))
        skit.click()
        time.sleep(3)
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.left > div:nth-child(4) > div.kuang_center > ul > li:nth-child(2) > a')))
        addnews.click()
        publish = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.right_top > div.right_menu1 > a:nth-child(1) > img')))
        publish.click()
        # 新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#title')))
        title.clear()
        title.send_keys(newstitle)
        # 新闻关键字
        keys = driver.find_element_by_name("tags")
        keys.send_keys(game)
        # 新闻游戏名
        keys = driver.find_element_by_name("gamename")
        keys.send_keys(game)
        # 新闻作者
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#writer')))
        title.clear()
        title.send_keys(source)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return bk40407(url,ac,ps,newstitle,game,source,content)
def bk4q5q(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btnlogin')))
        act.send_keys(ac)
        psd.send_keys(ps)
        work = True
        while work == True:
            input('请输入验证码后再回车' + '\n')
            login.click()
            if '成功' not in driver.find_element_by_id('error').text:
                print('验证码不正确，请重新输入')
                work = True
                continue
            work = False
        text = True
        while text == True:
            if driver.current_url == 'http://admin.4q5q.com/company/index.html':
                break
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.img_box > div:nth-child(4) > div.i_b_b_bottom > span:nth-child(3) > a')))
        addnews.click()
        # 新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#artiletitle')))
        title.clear()
        title.send_keys(newstitle)
        #选择游戏类别
        choosegame = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#content > div > div > div.t_middle > div:nth-child(3) > div:nth-child(1) > select > option:nth-child(4)')))
        choosegame.click()
        #选择游戏名
        gamename = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#ddlgameName_chzn > a > span')))
        gamename.click()
        name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#ddlgameName_chzn > div > div > input[type="text"]')))
        name.clear()
        name.send_keys(game)
        sure = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#ddlgameName_chzn_o_255')))
        sure.click()
        # 新闻内容
        keys = driver.find_element_by_name("Zhaiyao")
        keys.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return bk4q5q(url,ac,ps,newstitle,game,source,content)
def twan(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > form > input[type="text"]:nth-child(2)')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > form > input[type="password"]:nth-child(4)')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > form > input[type="submit"]:nth-child(6)')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        work = True
        while work == True:
            if driver.current_url == 'http://open.twan.cn/system.php?action=content&do=news_list':
                break
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > table > tbody > tr > td:nth-child(1) > dl > dd:nth-child(2) > a')))
        addnews.click()
        # 新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > table > tbody > tr > td:nth-child(2) > div.item > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > input')))
        title.clear()
        title.send_keys(newstitle)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return twan(url,ac,ps,newstitle,game,source,content)
def youkelai(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#myform > input.log-in.fl.tc')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        time.sleep(1)
        driver.get('http://sj.youkelai.com/e/member/tg/AddInfo.php?mid=1&enews=MAddInfo&classid=21')
        work = True
        while work == True:
            if driver.current_url == 'http://sj.youkelai.com/e/member/tg/AddInfo.php?mid=1&enews=MAddInfo&classid=21':
                break
        # 新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.card > table > tbody > tr > td:nth-child(2) > div.info.ctable > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        title.clear()
        title.send_keys(newstitle)
        # 新闻游戏名
        keys = driver.find_element_by_name("titlegame")
        keys.send_keys(game)
        # 新闻关键字
        keys = driver.find_element_by_name("keyboard")
        keys.send_keys(game)
        # 新闻内容
        keys = driver.find_element_by_name("smalltext")
        keys.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return youkelai(url,ac,ps,newstitle,game,source,content)
def youxichanye(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return youxichanye(url,ac,ps,newstitle,game,source,content)
def gameres(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        time.sleep(2)
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#ls_username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#ls_password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#lsform > div > div > table > tbody > tr:nth-child(2) > td.fastlg_l > button > em')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        # 新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#subject')))
        title.clear()
        title.send_keys(newstitle)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return gameres(url,ac,ps,newstitle,game,source,content)
def bk8477(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        work = True
        while work == True:
            act = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'body > div.content > form > div:nth-child(3) > div > input')))
            act.clear()
            psd = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'body > div.content > form > div:nth-child(4) > div > input')))
            psd.clear()
            login = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'body > div.content > form > div.form-actions > label > button')))
            act.send_keys(ac)
            psd.send_keys(ps)
            input('请输入验证码后再回车' + '\n')
            login.click()
            skit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div > div.bottom > a')))
            skit.click()
            time.sleep(2)
            if 'login' in driver.current_url:
                print('验证码不正确，请重新输入')
                work = True
                continue
            work = False
        # 内容
        con = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#_M4 > a')))
        con.click()
        #管理内容
        massge = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#_MP822 > a')))
        massge.click()
        driver.switch_to_frame('center_frame')
        #游戏攻略
        time.sleep(1)
        gong = driver.find_element_by_xpath('//*[@id="2"]/span/a[2]')
        gong.click()
        driver.switch_to.parent_frame()
        driver.switch_to_frame('rightMain')
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.pad-10 > div.content-menu.ib-a.blue.line-x > a.add.fb > em')))
        addnews.click()
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        # 新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#title')))
        title.clear()
        title.send_keys(newstitle)
        # 新闻关键字
        keys = driver.find_element_by_name("info[keywords]")
        keys.send_keys(game)
        # 新闻来源
        keys = driver.find_element_by_name("info[copyfrom]")
        keys.send_keys(source)
        # 新闻内容
        keys = driver.find_element_by_name("info[description]")
        keys.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return bk8477(url,ac,ps,newstitle,game,source,content)
def gametanzi(url,ac,ps,newstitle,game,source,content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#J_admin_name')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#admin_pwd')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login_btn_wraper > button')))
        act.send_keys(ac)
        psd.send_keys(ps)
        work = True
        while work == True:
            input('请输入验证码后再回车' + '\n')
            login.click()
            time.sleep(2)
            if driver.current_url != 'http://www.gametanzi.com/Admin/Index/index.html':
                if '验证码错误' in driver.find_element_by_xpath('//*[@id="login_btn_wraper"]/span').text:
                    print('验证码不正确，请重新输入')
                    work = True
                    continue
            work = False
        work = True
        while work == True:
            if driver.current_url == 'http://www.gametanzi.com/Admin/Index/index.html':
                break
        contentnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#nav_wraper > ul > li:nth-child(4) > a > span.menu-text.normal')))
        contentnews.click()
        publish = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#nav_wraper > ul > li.open > ul > li > a > span')))
        publish.click()
        work = True
        while work == True:
            if '正在加载' not in driver.find_element_by_xpath('//*[@id="loading"]/span').text:
                break
        driver.switch_to_frame('appiframe-7Portal')
        addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.wrap.J_check_wrap > ul > li:nth-child(2) > a')))
        addnews.click()
        #关联游戏
        # 新闻标题
        games = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#myform > div.col-auto > div > table > tbody > tr:nth-child(1) > td > span > input.textbox-text.validatebox-text.textbox-prompt')))
        games.send_keys(game)
        linkgame = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#datagrid-row-r2-2-225 > td:nth-child(2) > div')))
        linkgame.click()
        # 关联栏目
        linkgame = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#myform > div.col-auto > div > table > tbody > tr:nth-child(2) > td > select > option:nth-child(1)')))
        linkgame.click()
        # 新闻标题
        title = driver.find_element_by_name('post[post_title]')
        title.send_keys(game)
        # 新闻关键词
        keys = driver.find_element_by_name('post[post_keywords]')
        keys.send_keys(newstitle)
        # 新闻来源
        gamesoure = driver.find_element_by_name("post[post_source]")
        gamesoure.send_keys(source)
        # 新闻内容
        keys = driver.find_element_by_name("post[post_excerpt]")
        keys.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return gametanzi(url,ac,ps,newstitle,game,source,content)
def bk1g31(url, ac, ps, newstitle, game, source, content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = driver.find_element_by_name('username')
        psd = driver.find_element_by_name('password')
        login = driver.find_element_by_name('loginsubmit')
        act.send_keys(ac)
        psd.send_keys(ps)
        work = True
        while work == True:
            input('请输入验证码后再回车' + '\n')
            login.click()
            time.sleep(3)
            if driver.current_url == url:
                print('验证码不正确，请重新输入')
                work = True
                continue
            work = False
        # 跳过
        js = 'window.open("http://bbs.1g31.com/forum.php?mod=post&action=newthread&fid=56");'
        driver.execute_script(js)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        # 新闻标题
        title = driver.find_element_by_name('subject')
        title.send_keys(newstitle)
        #选择新闻类别
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#postbox > div.pbt.cl > div.ftid')))
        addnews.click()
        addnew = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#typeid_ctrl_menu > ul > li:nth-child(2)')))
        addnew.click()
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return bk1g31(url, ac, ps, newstitle, game, source, content)
def bk77l(url, ac, ps, newstitle, game, source, content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > div:nth-child(3) > div.center-block.w-xxx.w-auto-xs.p-y-md.pull-right.m-t-lg > div > form > div:nth-child(1) > input')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > div:nth-child(3) > div.center-block.w-xxx.w-auto-xs.p-y-md.pull-right.m-t-lg > div > form > div:nth-child(2) > input')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div:nth-child(3) > div.center-block.w-xxx.w-auto-xs.p-y-md.pull-right.m-t-lg > div > form > button.btn.info.btn-block.p-x-md.m-t')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        work = True
        while work == True:
            if driver.current_url == 'http://open.77l.com/dev#/dev/whole/':
                break
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#aside > div > div.hide-scroll.nav-stacked.nav-active-primary > nav > ul > li:nth-child(4) > a > span.nav-text')))
        addnews.click()
        publish = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#view > div.p-a.white.lt.box-shadow > div > div:nth-child(2) > a')))
        publish.click()
        # 新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#view > form > div.padding > div > div:nth-child(1) > div:nth-child(1) > div > div > input.form-control')))
        title.clear()
        title.send_keys(newstitle)
        #文章分类
        article = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#view > form > div.padding > div > div:nth-child(1) > div:nth-child(2) > div > div > select > option:nth-child(2)')))
        article.click()
        # 相关游戏
        games = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#view > form > div.padding > div > div:nth-child(1) > div:nth-child(3) > div > div > div > div > p')))
        games.click()
        # 搜索游戏名
        keys = driver.find_element_by_name("so")
        keys.send_keys(game)
        choose = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#view > form > div.padding > div > div:nth-child(1) > div:nth-child(3) > div > div > div > div > p.input-group.m-t-sm.p-a-0.m-a-0 > i')))
        choose.click()
        sure = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#view > form > div.padding > div > div:nth-child(1) > div:nth-child(3) > div > div > div > div > div > ul > li')))
        sure.click()
        contentnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'body')))
        contentnews.click()
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return bk77l(url, ac, ps, newstitle, game, source, content)
def bk07076(url, ac, ps, newstitle, game, source, content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > div > div > form > div:nth-child(1) > input')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > div > div > form > div:nth-child(2) > input')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div > div > form > button')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        work = True
        while work == True:
            if driver.current_url == 'http://www.07076.cn/mem/index.html':
                break
        addnews = driver.find_element_by_xpath('//*[@id="side-menu"]/li[3]/ul/li[2]/a')
        addnews.click()
        addnew = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#main > div.row > div.col-sm-5.m-b-xs.addcz > button')))
        addnew.click()
        # 新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        title.clear()
        title.send_keys(newstitle)
        # 游戏名
        games = driver.find_element_by_name("game")
        games.send_keys(game)
        # 新闻内容
        keys = driver.find_element_by_name("des")
        keys.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return bk07076(url, ac, ps, newstitle, game, source, content)
def vshouyou(url, ac, ps, newstitle, game, source, content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#userpwd')))
        psd.clear()
        loginmd = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#popVerCodeStr')))
        loginmd.click()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginForm > center > input.button1')))
        act.send_keys(ac)
        psd.send_keys(ps)
        work = True
        while work == True:
            input('请输入验证码后再回车' + '\n')
            login.click()
            time.sleep(2)
            if EC.alert_is_present()(driver):
                driver.switch_to_alert().accept()
                print('验证码不正确，请重新输入')
                work = True
                continue
            else:
                work = False

        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#topUserBox > span > a:nth-child(3)')))
        addnews.click()
        # 新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#theme')))
        title.clear()
        title.send_keys(newstitle)
        #新闻栏目
        news = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#typeStr > option:nth-child(3)')))
        news.click()
        # 新闻关键词
        keys = driver.find_element_by_name("themeKey")
        keys.send_keys(game)
        # 新闻内容
        newcontent = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#contentKey')))
        newcontent.send_keys(content)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return vshouyou(url, ac, ps, newstitle, game, source, content)
def newyx(url, ac, ps, newstitle, game, source, content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div > div > div > form > ul > li.long > span > input[type="submit"]')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()

        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div > div.sidebar > ul > li.message > dl > dd > a')))
        addnews.click()
        # 新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#form-article > div:nth-child(1) > input')))
        title.clear()
        title.send_keys(newstitle)
        #分类
        choosenews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#form-article > div:nth-child(2) > select:nth-child(2) > option:nth-child(2)')))
        choosenews.click()
        choosenew = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#form-article > div:nth-child(2) > select:nth-child(3) > option:nth-child(2)')))
        choosenew.click()
        # 游戏名
        keys = driver.find_element_by_name("game_name")
        keys.send_keys(game)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return newyx(url, ac, ps, newstitle, game, source, content)
def yeyun(url, ac, ps, newstitle, game, source, content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#login-form-login')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#login-form-password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginBtn')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        # 我的主页
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#cmListBox > div:nth-child(3) > div.editor-tools.tPum > span.ml20.articlebtn')))
        addnews.click()
        work = True
        while work == True:
            if driver.current_url == 'https://shouyou.yeyun.com/u/main/243':
                break
        # 新闻标题
        # title = wait.until(EC.presence_of_element_located(
        #     (By.CSS_SELECTOR, 'div.ctls ::before')))
        # title.send_keys(newstitle)
        # #类型
        # print('3')
        # kind = wait.until(EC.element_to_be_clickable(
        #     (By.CSS_SELECTOR, 'body > div.tMsg > div:nth-child(2) > div > a.curr')))
        # kind.click()

        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return yeyun(url, ac, ps, newstitle, game, source, content)
def mumayi(url, ac, ps, newstitle, game, source, content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        print('请用QQ登录，自己填完内容')
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return mumayi(url, ac, ps, newstitle, game, source, content)
def bk3987(url, ac, ps, newstitle, game, source, content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#phone')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#logBtn')))
        act.send_keys(ac)
        psd.send_keys(ps)
        input('请手动划动验证码后再按回车'+'\n')
        login.click()
        work = True
        while work == True:
            if driver.current_url == 'https://open.3987.com/':
                break
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.banner > div > div > a.wztj')))
        addnews.click()
        addnew = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.main.clearfix > div > div > div.m-1000.fr > div.sub_soft > div.soft_tit > a')))
        addnew.click()
        #选择动态
        activit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.main.clearfix > div > div > div.m-1000.fr > div.fb_soft > div.soft_gui > ul > li:nth-child(1) > div > input[type="text"]:nth-child(1)')))
        activit.click()
        activity = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.main.clearfix > div > div > div.m-1000.fr > div.fb_soft > div.soft_gui > ul > li:nth-child(1) > div > ul > li:nth-child(1)')))
        activity.click()
        # 新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.main.clearfix > div > div > div.m-1000.fr > div.fb_soft > div.soft_gui > ul > li:nth-child(3) > input')))
        title.clear()
        title.send_keys(newstitle)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return bk3987(url, ac, ps, newstitle, game, source, content)
def juxia(url, ac, ps, newstitle, game, source, content):
    try:
        newwindow = "window.open('" + url + "');"
        driver.execute_script(newwindow)
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.mainbody > div > form > dl > dd.tc > input')))
        act.send_keys(ac)
        psd.send_keys(ps)
        work = True
        while work == True:
            act = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#username')))
            act.clear()
            psd = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#password')))
            psd.clear()
            login = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.mainbody > div > form > dl > dd.tc > input')))
            act.send_keys(ac)
            psd.send_keys(ps)
            input('请输入验证码后再回车' + '\n')
            login.click()
            work = True
            while work == True:
                if driver.current_url == 'https://i.juxia.com/member/login':
                    break
            # 跳过
            skit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#href')))
            skit.click()
            time.sleep(1)#body > div > div > div.content > p > span
            if driver.current_url == 'https://i.juxia.com/member/login.html':
                print('验证码不正确，请重新输入')
                work = True
                continue
            work = False
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.mainbody > div.topnav > div > a:nth-child(6)')))
        addnews.click()
        #投放平台
        addnew = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#formid > div > div.contribute > div:nth-child(1) > div:nth-child(1) > div > a:nth-child(3)')))
        addnew.click()
        # 新闻标题
        title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#title')))
        title.clear()
        title.send_keys(newstitle)
        # 新闻关键字
        keys = driver.find_element_by_name("keyword")
        keys.send_keys(game)
        input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return juxia(url, ac, ps, newstitle, game, source, content)



def choose_num():
    print('*************** 欢迎进入媒体后台自助系统 ***************')
    print('—————  1. 手游特殊媒体  —————'+'\n'+'—————  2. 手游部分媒体  —————'+'\n'+'—————  3. 页游媒体  —————')
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
        elif num == '3':
            work = False
            return 3
        else:
            print('请输入正确的选项')
            work = True

def main():
    newstitle, game, source, content = news_content()
    # num = choose_num()

    # if num == 1:
    #     print('进入手游特殊媒体...')
    #     for item in read_special_excel():
    #         get_page(item['title'],item['url'],item['account'],item['password'],newstitle,game,source,content)
    #     input('全部后台操作完毕，请关闭本程序'+'\n')
    # elif num == 2:
    print('进入手游部分媒体...')
    for item in read_part_excel():
        get_page(item['title'], item['url'], item['account'], item['password'], newstitle, game, source, content)
    input('全部后台操作完毕，请关闭本程序' + '\n')
    # elif num == 3:
    #     print('3还没有写好')
    #     input('全部后台操作完毕，请关闭本程序' + '\n')

# if __name__ == '__main__':
#     main()
main()
