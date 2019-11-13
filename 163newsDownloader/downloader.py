import json
import requests
from bs4 import BeautifulSoup


def get_page_list(pageNum):

    headers = {
    'Referer': 'https://news.163.com/domestic/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    }

    params = (
        ('callback', 'data_callback'),
    )

    url_temp = 'http://temp.163.com/special/00804KVA/cm_guonei_0{}.js'    #02-08国内
    # https://temp.163.com/special/00804KVA/cm_guoji_02.js?callback=data_callback.  #02-08国际
    # https://temp.163.com/special/00804KVA/cm_war_02.js?callback=data_callback    #02-08军事
    # https://temp.163.com/special/00804KVA/cm_hangkong_09.js?callback=data_callback&a=2    #02-08航空

    return_list = []
    for i in range(pageNum):
        url = url_temp.format(i)
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            continue

        res = response.text
        res = res.replace("data_callback(", "");
        res = res.replace(")", "");
        _response = json.loads(res)
        return_list.append(_response)


    with open('/Users/qianqian/Desktop/return_list.txt', 'w', encoding='utf-8') as list_f:
        list_f.write(str(return_list))
    list_f.close()

    with open('/Users/qianqian/Desktop/docurl.txt', 'w', encoding='utf-8') as url_f:
        for i in range(len(return_list)):
            for j in range(len(return_list[0])):
                url_f.write(return_list[i][j]['docurl'] + '\n')
    url_f.close()

    return return_list



def get_content(url, article_count):
    body = ''
    resp = requests.get(url)
    if resp.status_code == 200:
        body = resp.text
        bs4 = BeautifulSoup(body, 'html.parser')
        try:

            body = bs4.find('div', class_='post_text')

            # Remove style and video
            for e in body.find_all('style'):
                e.decompose()
            for e in body.find_all('div', class_='video-wrapper'):
                e.decompose()

            # Remove AD and ep-source
            body.find('div', class_='gg200x300').decompose()
            body.find('div', class_='ep-source').decompose()


            file_name = '/Users/qianqian/Desktop/data/' + str(article_count) + '.txt'
            with open(file_name, 'a', encoding='utf-8') as article_f:
                article_f.write(str(body.get_text()))

            # dirty hack: creat bash file , but it works:), like "python3 -m jieba 1.txt > result1.txt"
            with open('/Users/qianqian/Desktop/cut.sh', 'a', encoding='utf-8') as bash_file:
                bash_file.write("python3 -m jieba " + str(article_count) + ".txt > result" + str(article_count) + ".txt\n")

        except AttributeError as e:
            print(e)
        else:
            pass
        finally:
            pass

    return body


if __name__ == "__main__":

    my_list =  get_page_list(9)
    article_count = 0

    for i in range(len(my_list)):
            for j in range(len(my_list[0])):
                my_url = my_list[i][j]['docurl']
                article_count = article_count + 1
                print("Now we are crawling  " + "page " + str(i+1) + " and this is the " + str(j+1) + " article of this page") #debug
                get_content(my_url, article_count)

    print("Total" + str(article_count) + "found.")
