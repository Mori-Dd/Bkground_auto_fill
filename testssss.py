from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
import xlrd
import time
import traceback
driver = webdriver.Chrome()
driver.set_page_load_timeout(60) #60秒
#浏览器最大化
driver.maximize_window()
wait = WebDriverWait(driver, 60)
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
def read_web_excel():
    data = xlrd.open_workbook('账号密码.xlsx')
    table = data.sheet_by_name('页游后台')
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

def get_page_special(dict,title,url,ac,ps,newstitle,game,source,content):

    #手游特殊后台
    if 'bianwanjia' in url:
        print('正在打开 :' + title)
        bianwanjia(dict,title,url,ac,ps,newstitle,game,source,content)
    elif '11773' in url:
        print('正在打开 :' + title)
        bk11773(dict,title,url,ac,ps,newstitle,game,source,content)
    elif 'diyiyou' in url:
        print('正在打开 :' + title)
        diyiyou(dict,title,url,ac,ps,newstitle,game,source,content)
    elif 'hao76' in url:
        print('正在打开 :' + title)
        hao76(dict,title,url,ac,ps,newstitle,game,source,content)
    elif 'kaifu' in url:
        print('正在打开 :' + title)
        kaifu(dict,title,url,ac,ps,newstitle,game,source,content)
    elif '17huang' in url:
        print('正在打开 :' + title)
        huang17(dict,title,url,ac,ps,newstitle,game,source,content)
def get_page_part(dict_part,title,url,ac,ps,newstitle,game,source,content):
    #手游部分后台
    if 'kuhou' in url:
        print('正在打开 :' + title)
        kuhou(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif 'yyjia' in url:
        print('正在打开 :' + title)
        yyjia(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif 'thisisgame' in url:
        print('正在打开 :' + title)
        thisisgame(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif '1syou' in url:
        print('正在打开 :' + title)
        bk1syou(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif 'fahao' in url:
        print('正在打开 :' + title)
        fahao(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif 'ppswan' in url:
        print('正在打开 :' + title)
        ppswan(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif 'yxrb' in url:
        print('正在打开 :' + title)
        yxrb(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif 'youxiwangguo' in url:
        print('正在打开 :' + title)
        youxiwangguo(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif '40407' in url:
        print('正在打开 :' + title)
        bk40407(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif '4q5q' in url:
        print('正在打开 :' + title)
        bk4q5q(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif 'twan' in url:
        print('正在打开 :' + title)
        twan(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif 'youkelai' in url:
        print('正在打开 :' + title)
        youkelai(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif 'youxichanye' in url:
        print('正在打开 :' + title)
        youxichanye(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif 'gameres' in url:
        print('正在打开 :' + title)
        gameres(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif '119.23.135.10' in url:
        print('正在打开 :' + title)
        bk8477(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif 'gametanzi' in url:
        print('正在打开 :' + title)
        gametanzi(dict_part,title,url,ac,ps,newstitle,game,source,content)
    elif '1g31' in url:
        print('正在打开 :' + title)
        bk1g31(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif '77l' in url:
        print('正在打开 :' + title)
        bk77l(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif '07076' in url:
        print('正在打开 :' + title)
        bk07076(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'vshouyou' in url:
        print('正在打开 :' + title)
        vshouyou(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'newyx' in url:
        print('正在打开 :' + title)
        newyx(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'yeyun' in url:
        print('正在打开 :' + title)
        yeyun(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'mumayi' in url:
        print('正在打开 :' + title)
        mumayi(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif '3987' in url:
        print('正在打开 :' + title)
        bk3987(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'juxia' in url:
        print('正在打开 :' + title)
        juxia(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif '984g' in url:
        print('正在打开 :' + title)
        bk984g(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'fpwapadmin' in url:
        print('正在打开 :' + title)
        fpwapadmin(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif '13636' in url:
        print('正在打开 :' + title)
        bk13636(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'duowan' in url:
        print('正在打开 :' + title)
        duowan(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'sjyx' in url:
        print('正在打开 :' + title)
        sjyx(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif '87g' in url:
        print('正在打开 :' + title)
        bk87g(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'gk99' in url:
        print('正在打开 :' + title)
        gk99(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif '19yxw' in url:
        print('正在打开 :' + title)
        bk19yxw(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'doyo' in url:
        print('正在打开 :' + title)
        doyo(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'dunwan' in url:
        print('正在打开 :' + title)
        dunwan(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'gaoshouyou' in url:
        print('正在打开 :' + title)
        gaoshouyou(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'bbs.g.qq' in url:
        print('正在打开 :' + title)
        bbsgqq(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'xskhome' in url:
        print('正在打开 :' + title)
        xskhome(dict_part,title,url, ac, ps, newstitle, game, source, content)
    elif 'woyoo' in url:
        print('正在打开 :' + title)
        woyoo(dict_part,title,url, ac, ps, newstitle, game, source, content)
def get_page_web(dict,title,url,ac,ps,newstitle,game,source,content):

    #页游后台
    if '07073' in url:
        print('正在打开 :' + title)
        bk07073(dict,title,url,ac,ps,newstitle,game,source,content)
    elif '17566' in url:
        print('正在打开 :' + title)
        bk17566(dict,title,url,ac,ps,newstitle,game,source,content)
#手游特殊后台
def bianwanjia(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])
        cookies = [{'name': 'wwwwwmlrnd', 'value': 'SSSSSSSSSSSSSSSSSSSS'}, {'name': 'yunsuo_session_verify', 'value': '8aa60a7637ba07564e9ec3ee3380f840'}, {'name': 'wwwwwmlusername', 'value': '7road'}, {'name': 'wwwwwmluserid', 'value': '576'}, {'name': 'wwwwwmlauth', 'value': '2897537dad5340a9ea422f6c124f9f35'}, {'name': 'wwwwwqeditinfo', 'value': 'dgcms'}, {'name': 'wwwwwmlgroupid', 'value': '3'}, {'name': 'wwwwwqdelinfo', 'value': 'dgcms'}, {'name': 'Hm_lvt_a25e59663412e2d867322b75ce95f489', 'value': '1513408305'}, {'name': 'Hm_lpvt_a25e59663412e2d867322b75ce95f489', 'value': '1513408312'}]
        for i in range(0, len(cookies)):
            driver.add_cookie(cookies[i])
        urls = 'http://www.bianwanjia.com/e/DoInfo/AddInfo.php?mid=1&enews=MAddInfo&classid=70&Submit=%E6%B7%BB%E5%8A%A0%E4%BF%A1%E6%81%AF'
        driver.get(urls)
        while True:
            if driver.current_url == urls:
                break
        #新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.wrap.clear > div.user_box.fr > div.user_main > form > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        titles.send_keys(newstitle)
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
        # input('提交完按回车确认进入下一家'+'\n')
    except Exception:
        print(title+'出问题了，请记得回来手动操作')
        return None
def diyiyou(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])
        cookies = [{'name': 'jz_un', 'value': '7road777'}, {'name': 'jz_key', 'value': '2e35e05c2a5da5a1b0a6500b4da6f439'}]
        for i in range(0, len(cookies)):
            driver.add_cookie(cookies[i])
        urls = 'http://www.diyiyou.com/vendor.php?m=news_addNewsView'
        driver.get(urls)
        while True:
            if driver.current_url == urls:
                break
        #新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#title')))
        titles.send_keys(newstitle)
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
        # input('提交完按回车确认进入下一家' + '\n')

    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def hao76(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])
        cookies = [{'name': 'PHPSESSID', 'value': 'o8kj2srgm2tmdlgji37j841gp0'}]
        for i in range(0, len(cookies)):
            driver.add_cookie(cookies[i])
        urls = 'http://cp.hao76.com/index.php?m=cp&c=index&a=add'
        driver.get(urls)
        while True:
            if driver.current_url == urls:
                break
        #新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#name')))
        titles.send_keys(newstitle)
        # 新闻内容
        keys = driver.find_element_by_name("info")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bk11773(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])
        cookies = [{'name': 'aliyungf_tc', 'value': 'AQAAAM8bHjpM4Q0An+xZcTxdPaQvb+EF'}, {'name': 'PHPSESSID', 'value': '922j7mk3s4dvlc97s4bp0b4mk1'}, {'name': 'admin_auth', 'value': 'e1bbe5bb0813d991df05089bbd0ac91e13e5d4a6a%3A4%3A%7Bi%3A0%3Bs%3A2%3A%2249%22%3Bi%3A1%3Bs%3A4%3A%22cscs%22%3Bi%3A2%3Bi%3A43200%3Bi%3A3%3Ba%3A5%3A%7Bs%3A9%3A%22simplepwd%22%3Bi%3A0%3Bs%3A8%3A%22username%22%3Bs%3A4%3A%22cscs%22%3Bs%3A8%3A%22realname%22%3Bs%3A18%3A%22%E5%8E%82%E5%95%86%E6%B5%8B%E8%AF%95%E7%94%A8%E6%88%B7%22%3Bs%3A8%3A%22group_id%22%3Bs%3A1%3A%226%22%3Bs%3A12%3A%22adminuserkey%22%3Bs%3A26%3A%22username%2Crealname%2Cgroup_id%22%3B%7D%7D'}]
        for i in range(0, len(cookies)):
            driver.add_cookie(cookies[i])
        urls = 'http://admin.11773.com/admin/producer/add'
        driver.get(urls)
        while True:
            if driver.current_url == urls:
                break
        input('请上传完图片再按回车''\n')
        #新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#updateform > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > input')))
        titles.send_keys(newstitle)
        #新闻短标题
        shorttitle = driver.find_element_by_name("game[short_title]")
        shorttitle.send_keys(game)
        # 新闻关键字
        keys = driver.find_element_by_name("game[keyword]")
        keys.send_keys(game)
        # 新闻内容
        news = driver.find_element_by_name("game[description]")
        news.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def huang17(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])
        cookies = [{'name': 'menuitems', 'value': '1_1%2C2_1%2C3_1'}, {'name': 'PHPSESSID', 'value': 'hssngdmqek9lpeenrli2l0k9u3'}, {'name': 'DedeUserID', 'value': '314'}, {'name': 'DedeUserID__ckMd5', 'value': '0b7712449e641183'}, {'name': 'DedeLoginTime', 'value': '1513408370'}, {'name': 'DedeLoginTime__ckMd5', 'value': '3ba2d5939a6bf820'}]
        for i in range(0, len(cookies)):
            driver.add_cookie(cookies[i])
        urls = 'http://www.17huang.com/dede/index.php'
        driver.get(urls)
        while True:
            if driver.current_url == urls:
                break
        driver.switch_to.frame("menu")
        addnews = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#items2_1 > ul > li > div > div.flrct > a > img')))
        addnews.click()
        driver.switch_to.default_content()
        driver.switch_to.frame("main")
        #新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#title')))
        titles.send_keys(newstitle)
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
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def kaifu(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])
        cookies = [{'name': 'PHPSESSID', 'value': '7511295fdb968ceebc09f73fc99110dd'}, {'name': 'kaifu_pmuserInfo', 'value': '5589Vcj%2B9FvOF5cA2aVv5B8d%2FOEspuqQOm0JbgdqT0PMzZGdn7E6FLYEdfMta7mU1RstL1Bp82zrJqvo359AI9yrt3EH7VxXO%2B35zDDWZswdJRQ2gxxWAFG1xB3O4whApRa0LW0bB0pWxHEJqhfuwj4rQtWMq4ywMYI8%2BNAF8kOKmuu3J%2Bu06jm%2BMm49IoF%2BwAQ39ov3K%2BgsQYT12XrnMNBD5M3MqM5d9a8F6vXTPMhQITcGUgE%2FXnet73dWkcTp9Tn0Q0Xeq4nHwpbMxpoXXdQFiBGB2UNsCe%2FylWxi9WDSg1b%2BMyebUozcFsFpxlwtD3cAPBV8j4F6XNtHqnzTEm5gaY36W4067Xtkyy592pWPM0w%2BjVHVldOZfGCxnEuFrUxB0VEUz0yVnVuum%2Fc6AEGTWXAkqiN6tNJlHq2GDVusJCfgtN5B4w3K2hB63VVh9eDrJFkQUUHUygXfwFrmRmsE23P5jmcSJmkEGs4uNKHBVv%2Felv1pnhiKaOSJLa3F7%2BOzrjJZatvoKyxqMp9vFfLdUPAVi6kNzKdQEKNlz%2FZr0Ec9uJNsWvIDShy%2BFsc2yrrQvW%2BZPlcd%2FKYfcrtsg9rm1xX2fHh9ciCyvhtFrj6bFo4EQcDh0s1PW1%2FkMVzzCJRaKf%2BjwFH0OaHFFu2vHQJRb7L1GeDLa3NwiHWHUVYpbIFrfzi%2BpuV%2F40GA7sM3Qik3epckCs0AOxmYoJOzf%2B518x1wXA1hN3lf%2BIE0YoXJ96ZP7JuKXAL4'}]
        for i in range(0, len(cookies)):
            driver.add_cookie(cookies[i])
        urls = 'http://www.kaifu.com/pm/v2/article.php?action=articleadd'
        driver.get(urls)
        while True:
            if driver.current_url == urls:
                break
        #新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#title')))
        titles.send_keys(newstitle)
        # 新闻内容
        keys = driver.find_element_by_name("instructions")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None

#手游部分后台
def kuhou(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

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
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#title')))
        titles.send_keys(newstitle)

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
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def yyjia(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

        act = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#loginsubmit')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        time.sleep(2)
        driver.get('http://open.yyjia.com/index.php?ac=news')
        handle = driver.current_window_handle
        driver.switch_to_window(handle)
        #新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#news_title')))
        titles.send_keys(newstitle)
        # 新闻内容
        keys = driver.find_element_by_name("newsinfo[description]")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def thisisgame(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

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
        driver.get('http://www.thisisgame.com.cn/e/DoInfo/AddInfo.php?mid=1&enews=MAddInfo&classid=8')
        handle = driver.current_window_handle
        driver.switch_to_window(handle)
        while True:
            if driver.current_url == 'http://www.thisisgame.com.cn/e/DoInfo/AddInfo.php?mid=1&enews=MAddInfo&classid=8':
                break
        # addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#sy_box > div:nth-child(2) > a')))
        # addnews.click()
        # #选择新闻栏目
        # choose = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#changeclass > div > select > option:nth-child(2)')))
        # choose.click()
        # sure = wait.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#changeclass > button')))
        # sure.click()
        #新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div.main_box > div.right > form > div > div.manage_box > div:nth-child(1) > input[type="text"]')))
        titles.send_keys(newstitle)
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
        time.sleep(1)
        choosegame = driver.find_element_by_id('searchgame')
        choosegame.click()
        time.sleep(1)
        choosesure = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#gg > li > a')))
        choosesure.click()

        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bk1syou(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

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
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.table > div.t_middle > form > table.editinfo > tbody > tr > td > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        titles.send_keys(newstitle)
        #游戏名
        gamename = driver.find_element_by_name('keyboard')
        gamename.send_keys(game)
        # 新闻内容
        keys = driver.find_element_by_name("smalltext")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def fahao(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

        driver.set_page_load_timeout(60)  # 60秒
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
        titles = driver.find_element_by_name('info[title]')
        titles.send_keys(newstitle)
        # 新闻关键词
        keys = driver.find_element_by_name('info[keywords]')
        keys.send_keys(game)
        # 新闻关键词
        gamesource = driver.find_element_by_name('info[copyfrom]')
        gamesource.send_keys(source)
        # 新闻内容
        keys = driver.find_element_by_name("info[description]")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def ppswan(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

        driver.set_page_load_timeout(5)  # 10秒
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#myform > input.log-in.fl.tc')))
        act.send_keys(ac)
        psd.send_keys(ps)
        # try:
        login.click()
        time.sleep(2)
        # addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#show_userinfo > li:nth-child(2) > a')))
        # addnews.click()
        # time.sleep(2)
        # driver.switch_to_window(driver.window_handles[-1])
        driver.get('http://www.ppswan.com/e/member/tg/AddInfo.php?mid=1&enews=MAddInfo&classid=21')
        handle = driver.current_window_handle
        driver.switch_to_window(handle)
        work = True
        while work == True:
            if driver.current_url == 'http://www.ppswan.com/e/member/tg/AddInfo.php?mid=1&enews=MAddInfo&classid=21':
                break
        # publish = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.card > table > tbody > tr > td:nth-child(3) > div.info > div > table > tbody > tr:nth-child(5) > td > a:nth-child(2)')))
        # publish.click()
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.card > table > tbody > tr > td:nth-child(2) > div.info.ctable > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        titles.send_keys(newstitle)
        # 游戏名
        keys = driver.find_element_by_name("titlegame")
        keys.send_keys(game)
        # 关键字
        keys = driver.find_element_by_name("keyboard")
        keys.send_keys(game)
        # 新闻内容
        keys = driver.find_element_by_name("smalltext")
        keys.send_keys(content)
        # except Exception:
        #     driver.get('http://www.ppswan.com/e/member/tg/')
        #     time.sleep(2)
        #     publish = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        #                                                      'body > div.card > table > tbody > tr > td:nth-child(3) > div.info > div > table > tbody > tr:nth-child(5) > td > a:nth-child(2)')))
        #     publish.click()
        #     # 新闻标题
        #     titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
        #                                                        'body > div.card > table > tbody > tr > td:nth-child(2) > div.info.ctable > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        #     titles.send_keys(newstitle)
        #     # 游戏名
        #     keys = driver.find_element_by_name("titlegame")
        #     keys.send_keys(game)
        #     # 关键字
        #     keys = driver.find_element_by_name("keyboard")
        #     keys.send_keys(game)
        #     # 新闻内容
        #     keys = driver.find_element_by_name("smalltext")
        #     keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def yxrb(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

        time.sleep(2)
        addnews = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#newspecial')))
        addnews.click()
        print('\n'+'微信登录，手动填写'+'\n')
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def youxiwangguo(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

        while True:
            act = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#username')))
            act.clear()
            psd = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#password')))
            psd.clear()
            # login = wait.until(EC.element_to_be_clickable(
            #     (By.CSS_SELECTOR, '#myform > div.login_btn > button')))
            act.send_keys(ac)
            psd.send_keys(ps)
            break
        #     input('请输入验证码后再回车' + '\n')
        #     login.click()
        #     try:
        #         driver.set_page_load_timeout(3)
        #         skip = wait.until(EC.element_to_be_clickable(
        #             (By.CSS_SELECTOR, 'body > div.center_div.loading_block > div.loading_onclick > a')))
        #         skip.click()
        #         if driver.current_url == 'http://www.youxiwangguo.com/e/member/login/':
        #             print('验证码不正确，请重新输入')
        #             work = True
        #             continue
        #         else:
        #             time.sleep(1)
        #             js = 'window.open("http://www.youxiwangguo.com/e/member/tg/");'
        #             driver.execute_script(js)
        #             handles = driver.window_handles
        #             driver.switch_to_window(handles[-1])
        #             addnews = wait.until(EC.element_to_be_clickable(
        #                 (By.CSS_SELECTOR,
        #                  '#memberArea > div.col-auto > div > div.ctable > div > div > ul:nth-child(12) > li:nth-child(3) > a')))
        #             addnews.click()
        #             title = wait.until(EC.presence_of_element_located(
        #                 (By.CSS_SELECTOR, '#tab > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        #             title.clear()
        #             title.send_keys(newstitle)
        #             # 游戏名
        #             gamename = driver.find_element_by_name('keyboard')
        #             gamename.send_keys(game)
        #             # 新闻内容
        #             keys = driver.find_element_by_name("smalltext")
        #             keys.send_keys(content)
        #             work = False
        #     except Exception:
        #         time.sleep(2)
        #         js = 'window.open("http://www.youxiwangguo.com/e/member/tg/");'
        #         driver.execute_script(js)
        #         handles = driver.window_handles
        #         driver.switch_to_window(handles[-1])
        #         addnews = wait.until(EC.element_to_be_clickable(
        #             (By.CSS_SELECTOR, '#memberArea > div.col-auto > div > div.ctable > div > div > ul:nth-child(12) > li:nth-child(3) > a')))
        #         addnews.click()
        #         title = wait.until(EC.presence_of_element_located(
        #             (By.CSS_SELECTOR, '#tab > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        #         title.clear()
        #         title.send_keys(newstitle)
        #         # 游戏名
        #         gamename = driver.find_element_by_name('keyboard')
        #         gamename.send_keys(game)
        #         # 新闻内容
        #         keys = driver.find_element_by_name("smalltext")
        #         keys.send_keys(content)
        #         work = False
        # # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bk40407(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

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
        # #跳过
        # skit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#out > div.tanchu_tit_130624 > div')))
        # skit.click()
        # time.sleep(3)
        # addnews = wait.until(EC.element_to_be_clickable(
        #     (By.CSS_SELECTOR, 'body > div.left > div:nth-child(4) > div.kuang_center > ul > li:nth-child(2) > a')))
        # addnews.click()
        # publish = wait.until(EC.element_to_be_clickable(
        #     (By.CSS_SELECTOR, 'body > div.right_top > div.right_menu1 > a:nth-child(1) > img')))
        # publish.click()
        driver.get('http://zizhu.40407.com/arc/xwtg_add.php')
        handle = driver.current_window_handle
        driver.switch_to_window(handle)

        while 1:
            if driver.current_url == 'http://zizhu.40407.com/arc/xwtg_add.php':
                break
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#title')))
        titles.send_keys(newstitle)
        # 新闻关键字
        keys = driver.find_element_by_name("tags")
        keys.send_keys(game)
        # 新闻游戏名
        keys = driver.find_element_by_name("gamename")
        keys.send_keys(game)
        # 新闻作者
        author = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#writer')))
        author.send_keys(source)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def twan(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

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
        while 1:
            if driver.current_url == 'http://open.twan.cn/system.php?action=content&do=news_list':
                break
        time.sleep(2)
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > table > tbody > tr > td:nth-child(1) > dl > dd:nth-child(2) > a')))
        addnews.click()
        handle = driver.current_window_handle
        driver.switch_to_window(handle)
        # while 1:
        #     print('2')
        #     if driver.current_url == 'http://open.twan.cn/system.php?action=content&do=news_add':
        #         break
        # 新闻标题
        # titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > table > tbody > tr > td:nth-child(2) > div.item > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > input')))
        titles = driver.find_element_by_name('news_title')
        titles.send_keys(newstitle)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def youkelai(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

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
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.card > table > tbody > tr > td:nth-child(2) > div.info.ctable > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        titles.send_keys(newstitle)
        # 新闻游戏名
        keys = driver.find_element_by_name("titlegame")
        keys.send_keys(game)
        # 新闻关键字
        keys = driver.find_element_by_name("keyboard")
        keys.send_keys(game)
        # 新闻内容
        keys = driver.find_element_by_name("smalltext")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def youxichanye(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

        time.sleep(3)
        work = True
        while work == True:
            if driver.current_url == url:
                break
        # input('请点击一下QQ登录后按回车'+'\n')
        login = driver.find_element_by_xpath('//*[contains(@src, "static/image/common/qq_login.gif")]')
        login.click()
        time.sleep(1)
        driver.switch_to_frame('ptlogin_iframe')
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#switcher_plogin')))
        login.click()
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#u')))
        act.clear()
        act.send_keys(ac)
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#p')))
        psd.clear()
        psd.send_keys(ps)
        logins = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login_button')))
        logins.click()
        time.sleep(1)
        skip = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#messagetext > p.alert_btnleft > a')))
        skip.click()
        newtitle = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#subject')))
        newtitle.send_keys(newstitle)
        work = True
        while work == True:
            if driver.current_url == url:
                break

        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def gameres(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

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
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#subject')))
        titles.send_keys(newstitle)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bk77l(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

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
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#view > form > div.padding > div > div:nth-child(1) > div:nth-child(1) > div > div > input.form-control')))
        titles.send_keys(newstitle)
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
        time.sleep(1)
        keys = driver.find_element_by_name("so")
        keys.send_keys(game)
        time.sleep(1)
        choose = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#view > form > div.padding > div > div:nth-child(1) > div:nth-child(3) > div > div > div > div > p.input-group.m-t-sm.p-a-0.m-a-0 > i')))
        choose.click()
        time.sleep(1)
        sure = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#view > form > div.padding > div > div:nth-child(1) > div:nth-child(3) > div > div > div > div > div > ul > li')))
        sure.click()
        contentnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'body')))
        contentnews.click()
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bk07076(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        driver.set_page_load_timeout(60)  # 60秒
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
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        titles.send_keys(newstitle)
        # 游戏名
        games = driver.find_element_by_name("game")
        games.send_keys(game)
        # 新闻内容
        keys = driver.find_element_by_name("des")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def newyx(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

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
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#form-article > div:nth-child(1) > input')))
        titles.send_keys(newstitle)
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
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def yeyun(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

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

        # input('手动填写内容，提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def mumayi(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        work = True
        while work == True:
            if driver.current_url == url:
                break
        time.sleep(1)
        login = driver.find_element_by_xpath('//*[contains(@src, "template/dean_phone_140801/deancss/common/qq_login.gif")]')
        login.click()
        time.sleep(1)
        driver.switch_to_frame('ptlogin_iframe')
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#switcher_plogin')))
        login.click()
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#u')))
        act.clear()
        act.send_keys(ac)
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#p')))
        psd.clear()
        psd.send_keys(ps)
        logins = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login_button')))
        logins.click()
        skip = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#messagetext > p.alert_btnleft > a')))
        skip.click()
        time.sleep(1)
        work = True
        while work == True:
            if driver.current_url == url:
                break
        newtitle = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#subject')))
        newtitle.send_keys(newstitle)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bk984g(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        driver.set_page_load_timeout(60)  # 60秒
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div > div > div > div > form > fieldset > div.button-login > button')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()

        driver.get('http://tg.984g.com/article/add/')
        handle = driver.current_window_handle
        driver.switch_to_window(handle)

        while True:
            if driver.current_url == 'http://tg.984g.com/article/add/':
                break
        # addnews = wait.until(EC.element_to_be_clickable(
        #     (By.CSS_SELECTOR, '#sidebar-left > div > ul > li:nth-child(1) > a > span')))
        # addnews.click()
        # addnew = wait.until(EC.element_to_be_clickable(
        #     (By.CSS_SELECTOR, '#sidebar-left > div > ul > li:nth-child(1) > ul > li:nth-child(1) > a > span')))
        # addnew.click()
        # publish = wait.until(EC.element_to_be_clickable(
        #     (By.CSS_SELECTOR, '#content > div > div > div.box-content > div:nth-child(1) > div.span1 > a')))
        # publish.click()
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content > div > div > div.box-content > form > fieldset > div:nth-child(1) > div > input')))
        titles.send_keys(newstitle)
        # 关键字
        keyss = driver.find_element_by_name("post[keyword]")
        keyss.send_keys(game)
        # 新闻内容
        keys = driver.find_element_by_name("post[description]")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def fpwapadmin(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])
        print('wearefp' + '\n' + "baidu94sbi" + '\n' + '请进行身份验证')
        driver.set_page_load_timeout(60)  # 60秒
        driver.get(url)
        handle = driver.current_window_handle
        driver.switch_to_window(handle)

        while True:
            if driver.current_url == url:
                break
        work = True
        s = driver.find_elements_by_css_selector('body > table:nth-child(2) > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(7) > td:nth-child(2) > input[type="image"]')
        while len(s) != 0 and work == True:
            if driver.current_url != 'https://fpwapadmin.xmwan.com/e/adminfpapk/admin.php':
                while len(s) != 0:
                    act = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR,
                         'body > table:nth-child(2) > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > input')))
                    act.clear()
                    psd = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR,
                         'body > table:nth-child(2) > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > input')))
                    psd.clear()
                    act.send_keys(ac)
                    psd.send_keys(ps)
                    wait.until(EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, 'body > table > tbody > tr:nth-child(2) > td > div > a'))).click()
                    break
            else:
                break
        while work == True:
            if driver.current_url == 'https://fpwapadmin.xmwan.com/e/adminfpapk/admin.php':
                break
        driver.switch_to_frame('left')
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#pr1 > a')))
        addnews.click()
        addnew = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#pr277 > a')))
        addnew.click()
        driver.switch_to_default_content()
        driver.switch_to_frame('main')
        publish = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > table.tableborder > tbody > tr > td:nth-child(1) > table > tbody > tr > td:nth-child(1) > div > input[type="button"]')))
        publish.click()
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#baseinfo > table:nth-child(3) > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > input[type="text"]:nth-child(1)')))
        titles.send_keys(newstitle)
        # 新闻副标题
        keys = driver.find_element_by_name("ftitle")
        keys.send_keys(game)
        # 新闻内容
        keys = driver.find_element_by_name("smalltext")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bk13636(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > table:nth-child(4) > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(2) > input[type="submit"]:nth-child(1)')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        # 跳过
        work = True
        while work == True:
            if driver.current_url == 'http://www.13636.com/e/member/doaction.php':
                break
        skit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div > div.message > a')))
        skit.click()
        work = True
        while work == True:
            if driver.current_url == 'http://www.13636.com/e/member/cp/':
                break
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#domenuinfo > tr > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > a')))
        addnews.click()
        addnew = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > table:nth-child(4) > tbody > tr > td:nth-child(2) > table.tableborder > tbody > tr:nth-child(2) > td > select > option:nth-child(3)')))
        addnew.click()
        sure = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'body > table:nth-child(4) > tbody > tr > td:nth-child(2) > table.tableborder > tbody > tr:nth-child(3) > td > input[type="submit"]')))
        sure.click()
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > table:nth-child(4) > tbody > tr > td:nth-child(2) > form > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2) > input[type="text"]')))
        titles.send_keys(newstitle)
        # 游戏名
        games = driver.find_element_by_name("yxname")
        games.send_keys(game)
        # 作者
        games = driver.find_element_by_name("writer")
        games.send_keys(source)
        # 来源
        games = driver.find_element_by_name("befrom")
        games.send_keys(source)
        # 新闻内容
        keys = driver.find_element_by_name("smalltext")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def duowan(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#txtUserName')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#txtPassword')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btnLogin')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        work = True
        while work == True:
            if driver.current_url == 'http://tougao.duowan.com/page/index.jsp':
                break
        driver.switch_to_frame('leftFrame')
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#nav > li:nth-child(1) > a:nth-child(2)')))
        addnews.click()
        driver.switch_to_default_content()
        driver.switch_to_frame('main')
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#title')))
        titles.send_keys(newstitle)
        # 相关游戏
        keys = driver.find_element_by_name("relateGame")
        keys.send_keys(game)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def sjyx(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        driver.set_page_load_timeout(120)  # 120秒
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#user_login')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#user_pass')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#wp-submit')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        work = True
        while work == True:
            if driver.current_url == 'http://www.sjyx.com/wp-admin/post-new.php':
                break
        #标题
        titles = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#title')))
        titles.send_keys(newstitle)
        #选择栏目
        choose = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#in-category-1')))
        choose.click()
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def gk99(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > form > div.container > div:nth-child(3) > div > input')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > form > div.container > div:nth-child(4) > div > input')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > form > div.container > div:nth-child(6) > button')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        work = True
        while work == True:
            if driver.current_url == 'http://tg.gk99.com/':
                break
        time.sleep(1)
        addnew = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/ul/li[1]/dl/dd[1]/a')
        addnew.click()
        time.sleep(1)
        driver.switch_to_frame('view')
        time.sleep(1)
        publish = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'body > div.toolbar.layui-form > form > span.layui-btn-group > button:nth-child(1) > i')))
        publish.click()
        time.sleep(1)
        driver.switch_to_frame('layui-layer-iframe1')
        time.sleep(1)
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > form > div.content-container > div.content-container-l > div.content-title > input')))
        titles.send_keys(newstitle)
        # 新闻内容
        keys = driver.find_element_by_name("desc")
        keys.send_keys(content)
        games = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'body > form > div.content-container > div.content-container-r > div:nth-child(1) > div:nth-child(2) > input')))
        games.click()
        time.sleep(2)
        #选择游戏
        driver.switch_to_default_content()
        driver.switch_to_frame('view')
        driver.switch_to_frame('layui-layer-iframe2')
        choose = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                           '#keywords')))
        choose.send_keys(game)
        serach = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'body > div.toolbar.layui-form > form > span > span:nth-child(4) > button')))
        serach.click()
        serachgame = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'body > div:nth-child(3) > table > tbody > tr > td:nth-child(2) > div')))
        serachgame.click()
        sure = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'body > div.dialog-box-bottom > div.dialog-box-btn > button:nth-child(1)')))
        sure.click()
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bk19yxw(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#form1 > li:nth-child(2) > input')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#form1 > li:nth-child(3) > input[type="password"]')))
        psd.clear()
        act.send_keys(ac)
        psd.send_keys(ps)
        s = driver.find_elements_by_css_selector('#form1 > li:nth-child(5) > a')
        t = ''
        while len(s) != 0 and len(t) == 0:
            try:
                if EC.alert_is_present()(driver):
                    driver.switch_to_alert().accept()
                    act = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '#form1 > li:nth-child(2) > input')))
                    act.clear()
                    psd = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '#form1 > li:nth-child(3) > input[type="password"]')))
                    psd.clear()
                    act.send_keys(ac)
                    psd.send_keys(ps)
                    continue
                t = driver.find_elements_by_css_selector(
                    'body > div > div > div.rgrinfo > div > ul > li:nth-child(8) > a')
            except UnexpectedAlertPresentException:
                continue

        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div > div > div.rgrinfo > div > ul > li:nth-child(5) > a:nth-child(3)')))
        addnews.click()
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#title')))
        titles.send_keys(newstitle)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def doyo(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.area > div.msg_list.msg_list_simple > form > div > div.c_left.c_left_big.game_upload > input[type="text"]:nth-child(6)')))
        titles.send_keys(newstitle)
        # 选择分类
        kinds = driver.find_element_by_xpath("/html/body/div[4]/div[3]/form/div/div[1]/span[5]/input[5]")
        kinds.click()
        # 选择内容
        kindgame = driver.find_element_by_xpath("/html/body/div[4]/div[3]/form/div/div[1]/span[8]/input[1]")
        kindgame.click()
        # 厂商
        sources = driver.find_element_by_name("source")
        sources.send_keys(source)
        # 作者
        autuor = driver.find_element_by_name("author")
        autuor.send_keys(source)
        # 新闻内容
        keys = driver.find_element_by_name("summary")
        keys.send_keys(content)
        # # 关联游戏
        # choosegame = driver.find_element_by_id("select_game")
        # choosegame.click()
        # time.sleep(1)
        # game = driver.find_element_by_name('game_keyword')
        # game.send_keys('弹弹堂')
        # time.sleep(3)
        # chooses = driver.find_element_by_xpath('//*[@id="game_list_select"]/span[7]')
        # chooses.click()
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def dunwan(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#form1 > div > ul > li:nth-child(1) > span > input')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#form1 > div > ul > li:nth-child(2) > span > input')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form1 > div > ul > li:nth-child(3) > span > a.denglu')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        # 跳过
        work = True
        while work == True:
            if driver.current_url == 'http://tougao.dunwan.com/index.php?tp=article&status=-1':
                break
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#box4 > span:nth-child(1) > a')))
        addnews.click()
        work = True
        while work == True:
            if driver.current_url == 'http://tougao.dunwan.com/index.php?tp=article&op=add':
                break
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#title')))
        titles.send_keys(newstitle)
        # 新闻内容
        keys = driver.find_element_by_name("description")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bbsgqq(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        logins = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.gb-top-nav > div > div > a')))
        logins.click()
        time.sleep(1)
        driver.switch_to_frame('ptlogin_frame')
        aclogins = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#switcher_plogin')))
        aclogins.click()
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#u')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#p')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login_button')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        # time.sleep(2)
        # driver.switch_to_default_content()
        # time.sleep(1)
        # publish = wait.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#newTopicBtn')))
        # publish.click()
        # # 新闻标题
        # titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#newTopicTitle')))
        # titles.send_keys(newstitle)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        traceback.print_exc()
        print(title + '出问题了，请记得回来手动操作')
        return None
def xskhome(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        time.sleep(2)
        work = True
        while work == True:
            if driver.current_url == url:
                break
        driver.switch_to_frame(0)
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        md5 = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#captcha')))
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#submit-btn')))
        act.send_keys(ac)
        psd.send_keys(ps)
        md5.send_keys('1234')
        login.click()
        driver.switch_to_default_content()
        time.sleep(2)
        js = 'document.getElementsByClassName("navbox")[0].style.display="block";'
        driver.execute_script(js)
        time.sleep(1)
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#memu > div > ul.nav > li:nth-child(2) > div > a:nth-child(3)')))
        addnews.click()
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#title')))
        titles.send_keys(newstitle)
        #选择游戏
        choose = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#channel-type > input.value.ajax')))
        choose.send_keys(game)
        choose1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#channel-type > input.value.ajax')))
        choose1.click()
        choosegame = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#channel-type > div > ul > li')))
        choosegame.click()
        # 新闻内容
        keys = driver.find_element_by_name("Points")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def woyoo(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        driver.set_page_load_timeout(60)  # 60秒
        logins = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#login_bar > a')))
        logins.click()
        time.sleep(1)
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#uname')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#pwd')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginBtn')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        time.sleep(1)
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#login_bar > a:nth-child(1)')))
        addnews.click()
        work = True
        while work == True:
            if driver.current_url == 'https://www.woyoo.com/huiyuan/main.php':
                break
        user = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#myArticle')))
        user.click()
        work = True
        while work == True:
            if driver.current_url == 'https://www.woyoo.com/huiyuan/myArticle.php':
                break
        publish = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#woyaofatie')))
        publish.click()
        work = True
        while work == True:
            if driver.current_url == 'https://www.woyoo.com/huiyuan/fatie.php':
                break
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#title')))
        titles.send_keys(newstitle)
        # 新闻来源
        gamesource = driver.find_element_by_name("source")
        gamesource.send_keys(source)
        # 新闻关键字
        key = driver.find_element_by_name("keywords")
        key.send_keys(game)
        # 新闻内容
        keys = driver.find_element_by_name("description")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
#验证码
def juxia(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        psd.clear()
        act.send_keys(ac)
        psd.send_keys(ps)
        work = True
        s = driver.find_elements_by_css_selector('body > div.mainbody > div > form > dl > dd.tc > input')
        while len(s) != 0 and work == True:
            if driver.current_url != 'https://i.juxia.com/':
                while len(s) != 0:
                    act = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '#username')))
                    act.clear()
                    psd = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '#password')))
                    psd.clear()
                    act.send_keys(ac)
                    psd.send_keys(ps)

                    wait1 = WebDriverWait(driver, 6000)
                    wait1.until(EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, '#href'))).click()
                    time.sleep(1)
                    break
            else:
                break
            time.sleep(1)
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.mainbody > div.topnav > div > a:nth-child(6)')))
        addnews.click()
        #投放平台
        addnew = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#formid > div > div.contribute > div:nth-child(1) > div:nth-child(1) > div > a:nth-child(3)')))
        addnew.click()
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#title')))
        titles.send_keys(newstitle)
        # 新闻关键字
        keys = driver.find_element_by_name("keyword")
        keys.send_keys(game)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bk4q5q(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        psd.clear()
        act.send_keys(ac)
        psd.send_keys(ps)
        while True:
            if driver.current_url == 'http://admin.4q5q.com/company/index.html':
                break
        driver.get('http://admin.4q5q.com/company/newsAdd.html')
        while True:
            if driver.current_url == 'http://admin.4q5q.com/company/newsAdd.html':
                break
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#artiletitle')))
        titles.send_keys(newstitle)
        #选择游戏类别
        choosegame = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#content > div > div > div.t_middle > div:nth-child(3) > div:nth-child(1) > select > option:nth-child(4)')))
        choosegame.click()
        # #选择游戏名
        # gamename = wait.until(EC.element_to_be_clickable(
        #     (By.CSS_SELECTOR, '#ddlgameName_chzn > a > span')))
        # gamename.click()
        # name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#ddlgameName_chzn > div > div > input[type="text"]')))
        # name.clear()
        # name.send_keys(game)
        # time.sleep(1)
        # sure = driver.find_element_by_xpath('//*[@id="ddlgameName_chzn_o_259"]')
        # sure.click()
        # 新闻内容
        keys = driver.find_element_by_name("Zhaiyao")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def vshouyou(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#userpwd')))
        psd.clear()
        act.send_keys(ac)
        psd.send_keys(ps)
        while True:
            try:
                if EC.alert_is_present()(driver):
                    driver.switch_to_alert().accept()
                    continue
                elif driver.current_url == 'http://www.vshouyou.com/':
                    break
            except UnexpectedAlertPresentException:
                continue

        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#topUserBox > span > a:nth-child(3)')))
        addnews.click()
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#theme')))
        titles.send_keys(newstitle)
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
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bk1g31(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        act = driver.find_element_by_name('username')
        psd = driver.find_element_by_name('password')
        act.send_keys(ac)
        psd.send_keys(ps)
        while True:
            if driver.current_url == 'http://bbs.1g31.com/':
                break
        driver.get('http://bbs.1g31.com/forum.php?mod=post&action=newthread&fid=56')
        handle = driver.current_window_handle
        driver.switch_to_window(handle)
        while True:
            if driver.current_url == 'http://bbs.1g31.com/forum.php?mod=post&action=newthread&fid=56':
                break
        time.sleep(1)
        # 新闻标题
        titles = driver.find_element_by_name('subject')
        titles.send_keys(newstitle)
        #选择新闻类别
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#postbox > div.pbt.cl > div.ftid')))
        addnews.click()
        addnew = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#typeid_ctrl_menu > ul > li:nth-child(2)')))
        addnew.click()
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bk3987(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#phone')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#password')))
        psd.clear()
        act.send_keys(ac)
        psd.send_keys(ps)
        while True:
            if driver.current_url == 'https://open.3987.com/':
                break

        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.banner > div > div > a.wztj')))
        addnews.click()
        while True:
            if driver.current_url == 'https://open.3987.com/article.html':
                break
        addnew = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.main.clearfix > div > div > div.m-1000.fr > div.sub_soft > div.soft_tit > a')))
        addnew.click()
        while True:
            if driver.current_url == 'https://open.3987.com/fabu.html':
                break
        time.sleep(1)
        #选择动态
        activit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.main.clearfix > div > div > div.m-1000.fr > div.fb_soft > div.soft_gui > ul > li:nth-child(1) > div > input[type="text"]:nth-child(1)')))
        activit.click()
        activity = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.main.clearfix > div > div > div.m-1000.fr > div.fb_soft > div.soft_gui > ul > li:nth-child(1) > div > ul > li:nth-child(1)')))
        activity.click()
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.main.clearfix > div > div > div.m-1000.fr > div.fb_soft > div.soft_gui > ul > li:nth-child(3) > input')))
        titles.send_keys(newstitle)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bk8477(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

        work = True
        s = driver.find_elements_by_css_selector('body > div.content > form > div.form-actions > label > button')
        while len(s) != 0 and work == True:
            if 'http://119.23.135.10/index.php?m=admin&c=index&pc_hash' not in driver.current_url:
                while len(s) != 0:
                    act = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'body > div.content > form > div:nth-child(3) > div > input')))
                    act.clear()
                    psd = wait.until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'body > div.content > form > div:nth-child(4) > div > input')))
                    psd.clear()
                    act.send_keys(ac)
                    psd.send_keys(ps)
                    wait1 = WebDriverWait(driver, 6000)
                    wait1.until(EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, 'body > div > div.bottom > a'))).click()
                    time.sleep(1)
                    break
            else:
                break
        while True:
            if 'http://119.23.135.10/index.php?m=admin&c=index&pc_hash' in driver.current_url:
                break
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
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#title')))
        titles.send_keys(newstitle)
        # 新闻关键字
        keys = driver.find_element_by_name("info[keywords]")
        keys.send_keys(game)
        # 新闻来源
        keys = driver.find_element_by_name("info[copyfrom]")
        keys.send_keys(source)
        # 新闻内容
        keys = driver.find_element_by_name("info[description]")
        keys.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def gametanzi(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])

        driver.set_page_load_timeout(60)  # 60秒
        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#J_admin_name')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#admin_pwd')))
        psd.clear()
        act.send_keys(ac)
        psd.send_keys(ps)
        while True:
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
        # 关联栏目
        linkgame = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#myform > div.col-auto > div > table > tbody > tr:nth-child(2) > td > select > option:nth-child(1)')))
        linkgame.click()
        # 新闻标题
        titles = driver.find_element_by_name('post[post_title]')
        titles.send_keys(newstitle)
        # 新闻关键词
        keys = driver.find_element_by_name('post[post_keywords]')
        keys.send_keys(game)
        # 新闻来源
        gamesoure = driver.find_element_by_name("post[post_source]")
        gamesoure.send_keys(source)
        # 新闻内容
        keys = driver.find_element_by_name("post[post_excerpt]")
        keys.send_keys(content)
        # # 关联游戏
        # time.sleep(1)
        # gamess = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
        #                                                     '#myform > div.col-auto > div > table > tbody > tr:nth-child(1) > td > span > input.textbox-text.validatebox-text.textbox-prompt')))
        # gamess.send_keys(game)
        # time.sleep(2)
        # linkgame = wait.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#datagrid-row-r2-2-266 > td:nth-child(2) > div')))
        # linkgame.click()
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def gaoshouyou(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > div.login-box > form > fieldset > ul > li:nth-child(1) > div > input')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > div.login-box > form > fieldset > ul > li:nth-child(2) > div > input')))
        psd.clear()
        act.send_keys(ac)
        psd.send_keys(ps)
        while True:
            try:
                if EC.alert_is_present()(driver):
                    driver.switch_to_alert().accept()
                    continue
                elif driver.current_url == 'http://www.gaoshouyou.com/cstougao':
                    break
            except UnexpectedAlertPresentException:
                continue

        while True:
            if driver.current_url == 'http://www.gaoshouyou.com/cstougao':
                break
        addnews = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'body > div.count > div.menu > div > ul > li:nth-child(1) > ul > li:nth-child(2) > a')))
        addnews.click()
        while True:
            if driver.current_url == 'http://www.gaoshouyou.com/cstougao/add?type=5':
                break
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.count > div.wrap > div > div.box > form > ul > li:nth-child(2) > div > input')))
        titles.send_keys(newstitle)
        #短标题
        ftitle = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.count > div.wrap > div > div.box > form > ul > li:nth-child(3) > div > input')))
        ftitle.send_keys(game)
        # 新闻内容
        keys = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                            'body > div.count > div.wrap > div > div.box > form > ul > li:nth-child(5) > div > textarea')))
        keys.send_keys(content)
        # 绑定专区
        bind = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          'body > div.count > div.wrap > div > div.box > form > ul > li:nth-child(1) > div > input.form-text.form-text-tip-input')))
        bind.clear()
        bind.send_keys(game)
        time.sleep(1)
        choosegame = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                            'body > div.count > div.wrap > div > div.box > form > ul > li:nth-child(1) > div > div > ul')))
        choosegame.click()
        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
def bk87g(dict,title,url, ac, ps, newstitle, game, source, content):
    try:
        driver.switch_to_window(dict[title])

        act = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#admin_username')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#admin_password')))
        psd.clear()
        act.send_keys(ac)
        psd.send_keys(ps)
        print('请手动划动验证码登录，然后手动发布稿件,关闭帮助视频')
        input('如果有视频请关闭视频再按回车，无的话直接按回车' + '\n')
        while True:
            if driver.current_url == 'http://cp.87g.com/index.php?m=cp&c=content&a=add':
                break

        driver.switch_to_frame('test')
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#title')))
        titles.send_keys(newstitle)
        # #选择游戏
        # games = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#game_name')))
        # games.click()
        # time.sleep(1)
        # choose = driver.find_element_by_xpath('//*[@id="ajaxgame"]')
        # choose.send_keys(game)
        # choosegam = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#searchgame')))
        # choosegam.click()
        # time.sleep(1)
        # choosegame = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#gg > li > a')))
        # choosegame.click()

        # input('提交完按回车确认进入下一家' + '\n')
    except Exception:
        print(title + '出问题了，请记得回来手动操作')
        return None
#页游后台
def bk07073(dict,title,url,ac,ps,newstitle,game,source,content):
    try:
        driver.switch_to_window(dict[title])
        act = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.regWrapper > div.thisLogTable > form > table > tbody > tr:nth-child(1) > td > input')))
        act.clear()
        psd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.regWrapper > div.thisLogTable > form > table > tbody > tr:nth-child(2) > td > input')))
        psd.clear()
        login = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'body > div.regWrapper > div.thisLogTable > form > table > tbody > tr:nth-child(4) > td > span > input[type="submit"]')))
        act.send_keys(ac)
        psd.send_keys(ps)
        login.click()
        addnews = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#wrapper > div.f24 > span > a')))
        addnews.click()
        # 新闻标题
        titles = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#updateform > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > input')))
        titles.send_keys(newstitle)
        # 新闻短标题
        shorttitle = driver.find_element_by_name("game[short_title]")
        shorttitle.send_keys(game)
        # 新闻关键字
        keys = driver.find_element_by_name("game[keyword]")
        keys.send_keys(game)
        # 新闻内容
        news = driver.find_element_by_name("game[description]")
        news.send_keys(content)
        # input('提交完按回车确认进入下一家' + '\n')
    except TimeoutException:
        return bk07073(dict,title,url,ac,ps,newstitle,game,source,content)
def choose_num():
    print('*************** 欢迎进入媒体后台自助系统 ***************')
    print('—————  1. 手游特殊媒体  —————'+'\n'+'—————  2. 手游部分媒体  —————'+'\n'
          +'—————  3. 页游媒体  —————'+'\n'+'—————  4. 退出  —————')
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
        elif num == '4':
            work = False
            return 4
        else:
            print('请输入正确的选项')
            work = True

def main():
    newstitle, game, source, content = news_content()
    work = True
    while work == True:
        num = choose_num()
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        dict = {}
        if num == 1:
            print('进入手游特殊媒体...')
            for item in read_special_excel():
                try:
                    driver.set_page_load_timeout(20)  # 20秒
                    js = 'window.open("' + item['url'] + '");'
                    driver.execute_script(js)
                    handles = driver.window_handles
                    driver.switch_to_window(handles[-1])
                    handle = driver.current_window_handle
                    dict[item['title']] = handle
                except Exception:
                    print('打开网站：' + item['title'] + '出错了')
                    continue
            for item in read_special_excel():
                get_page_special(dict,item['title'],item['url'],item['account'],item['password'],newstitle,game,source,content)
            driver.switch_to_window(dict['便玩家'])
            print('全部后台操作完毕，请手动提交，完成后请重新选择'+'\n')
            time.sleep(2)
            continue
        elif num == 2:
            print('进入手游部分媒体...')
            handles = driver.window_handles
            driver.switch_to_window(handles[-1])
            dict_part = {}
            for item in read_part_excel():
                try:
                    driver.set_page_load_timeout(20)  # 20秒
                    js = 'window.open("' + item['url'] + '");'
                    driver.execute_script(js)
                    handles = driver.window_handles
                    driver.switch_to_window(handles[-1])
                    handle = driver.current_window_handle
                    dict_part[item['title']] = handle
                except Exception:
                    print('打开网站：'+item['title']+'出错了')
                    continue
            for item in read_part_excel():
                get_page_part(dict_part,item['title'], item['url'], item['account'], item['password'], newstitle, game, source, content)
            driver.switch_to_window(dict_part['应用加'])
            print('全部后台操作完毕，请手动提交，完成后请重新选择' + '\n')
            time.sleep(2)
            continue
        elif num == 3:
            print('进入页游媒体...')
            handles = driver.window_handles
            driver.switch_to_window(handles[-1])
            dict_web = {}
            for item in read_web_excel():
                try:
                    driver.set_page_load_timeout(20)  # 20秒
                    js = 'window.open("' + item['url'] + '");'
                    driver.execute_script(js)
                    handles = driver.window_handles
                    driver.switch_to_window(handles[-1])
                    handle = driver.current_window_handle
                    dict_web[item['title']] = handle
                except Exception:
                    print('打开网站：' + item['title'] + '出错了')
                    continue
            for item in read_web_excel():
                get_page_web(dict_web, item['title'], item['url'], item['account'], item['password'], newstitle, game,
                              source, content)
            driver.switch_to_window(dict_web['07073'])
            print('全部后台操作完毕，请手动提交，完成后请重新选择' + '\n')
            time.sleep(2)
            continue
        elif num == 4:
            print('正在退出程序')
            time.sleep(2)
            driver.quit()
            continue


# if __name__ == '__main__':
#     main()
main()
