def get_cookies(dr,urls):

    cookies = []
    for item in dr.get_cookies():
        cookies.append({'name':item['name'],'value':item['value']})
    with open('cookie.txt','a') as f:
        f.write(urls+'\n'+str(cookies)+'\n'+'\n')
        f.close()