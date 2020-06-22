import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)

        r.raise_for_status()
        r.encoding = 'utf-8'# 字符编码格式改成 utf-8
        return r.text
    except:# 异常处理
        return " error "

url = "https://www.baidu.com"
print(getHTMLText(url))