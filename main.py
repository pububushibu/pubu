import json
import urllib.request
import urllib.parse
from HandleJs import Py4Js


def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    return data


def buildUrl(content, tk, tl):
    baseUrl = 'http://translate.google.cn/translate_a/single'
    baseUrl += '?client=t&'
    baseUrl += 'sl=auto&'
    baseUrl += 'tl=' + str(tl) + '&'
    baseUrl += 'hl=zh-CN&'
    baseUrl += 'dt=at&'
    baseUrl += 'dt=bd&'
    baseUrl += 'dt=ex&'
    baseUrl += 'dt=ld&'
    baseUrl += 'dt=md&'
    baseUrl += 'dt=qca&'
    baseUrl += 'dt=rw&'
    baseUrl += 'dt=rm&'
    baseUrl += 'dt=ss&'
    baseUrl += 'dt=t&'
    baseUrl += 'ie=UTF-8&'
    baseUrl += 'oe=UTF-8&'
    baseUrl += 'clearbtn=1&'
    baseUrl += 'otf=1&'
    baseUrl += 'pc=1&'
    baseUrl += 'srcrom=0&'
    baseUrl += 'ssel=0&'
    baseUrl += 'tsel=0&'
    baseUrl += 'kc=2&'
    baseUrl += 'tk=' + str(tk) + '&'
    baseUrl += 'q=' + content
    return baseUrl




def translate(data, tk, tl):
    # content是要翻译的内容

    content = urllib.parse.quote(data[0])

    url = buildUrl(content, tk, tl)

    result = open_url(url)
    res_json = json.loads(result)

    translate = res_json[0][0][0]
    print(translate)
    result = translate +'\n'

    # 保存翻译后的内容到文件中
    with open('D:/python/456.txt', 'a', encoding='utf-8') as f:
        f.write(result)


def main():
    js = Py4Js()
    # tl是要翻译的目标语种，值参照ISO 639-1标准，如果翻译成中文"zh/zh-CN简体中文"
    tl = "en"
    # 读取需要翻译的文件
    with open('D:/python/ch-en.txt', encoding="utf-8") as file_obj:
         for line in file_obj:
             data = line.split('  ')
             if len(data)==1:
                print (data[0])
                tk = js.getTk(data[0])
                translate(data,tk,tl)
                print ('success'+'\n')
             else:
                 print('lose')
if __name__ == "__main__":
    main()