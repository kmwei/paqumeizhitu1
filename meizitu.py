import requests
import re
from selenium import webdriver
import re
def findurl(b):
    url = 'http://jandan.net/ooxx/page-5068935{}#comments'.format(b)
    browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    browser.get(url)  # 这个就是chrome浏览器中的element的内容了
    source_code = browser.page_source
    # print(source_code)
    targets = re.findall('<p><a href="(.*?)" target=', source_code)
    return targets

def geturl(each):
    headers = {'Referer': 'http://jandan.net/ooxx','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    url1 = 'http:'+each
    return requests.get(url1,headers=headers)


#
#
#
def main():
    a = 0
    for b in range(10):
        a = a + 1

        targets = findurl(b)
        c = 0
        for each in targets:
            c = c+1

            geturl(each)
            res = geturl(each)
            code = res.status_code
            print(code)
        #print(res.text)
       # print(res.content)
            with open('./picture/{}{}.jpg'.format(a,c),'wb') as f:
                f.write(res.content)
if __name__ == '__main__':
    main()