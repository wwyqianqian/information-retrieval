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
            body = bs4.find('div', class_='post_text').get_text()
            # dirty hack
            body = body.replace("(function() {", "")
            body = body.replace("(window.slotbydup=window.slotbydup || []).push({", "")
            body = body.replace("id: '6374560',", "")
            body = body.replace("container: 'ssp_6374560',", "")
            body = body.replace("size: '300,250',", "")
            body = body.replace("display: 'inlay-fix',", "")
            body = body.replace("async:true", "")
            body = body.replace("});", "")
            body = body.replace("})();", "")

            body = body.replace("#endText .video-info a{text-decoration:none;color: #000;}", "")
            body = body.replace("#endText .video-info a:hover{color:#d34747;}", "")
            body = body.replace("#endText .video-list li{overflow:hidden;float: left; list-style:none; width: 132px;height: 118px; position: relative;margin:8px 3px 0px 0px;}", "")
            body = body.replace("#entText .video-list a,#endText .video-list a:visited{text-decoration:none;color:#fff;}", "")
            body = body.replace("#endText .video-list .overlay{text-align: left; padding: 0px 6px; background-color: #313131; font-size: 12px; width: 120px; position: absolute; bottom: 0px; left: 0px; height: 26px; line-height: 26px; overflow: hidden;color: #fff; }", "")
            body = body.replace("#endText .video-list .on{border-bottom: 8px solid #c4282b;}", "")
            body = body.replace("#endText .video-list .play{width: 20px; height: 20px; background:url(http://static.ws.126.net/video/img14/zhuzhan/play.png);position: absolute;right: 12px; top: 62px;opacity: 0.7; color:#fff;filter:alpha(opacity=70); _background: none; _filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src=\"http://static.ws.126.net/video/img14/zhuzhan/play.png\"); }", "")
            body = body.replace("#endText .video-list a:hover .play{opacity: 1;filter:alpha(opacity=100);_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src=\"http://static.ws.126.net/video/img14/zhuzhan/play.png\");}", "")

            fuck_str = "window.NTES && function(d){var f=function(c){var b=c.getAttribute(\"flashvars\"),a=c.getAttribute(\"repovideourl\").replace(\".flv\",\"-mobile.mp4\");h=d(c.parentNode.parentNode.parentNode),g='<embed src=\"http://v.163.com/swf/video/NetEaseFlvPlayerV3.swf\" flashvars=\"'+b+'\" allowfullscreen=\"true\" allowscriptaccess=\"always\" quality=\"high\" wmode=\"opaque\" width=\"100%\" height=\"100%\" type=\"application/x-shockwave-flash\" />';if(1/*(iPhone|iPad|iPod|Android|NETEASEBOBO|blackberry|bb\\d+)/ig.test(navigator.userAgent)*/){g='<video controls=\"controls\" preload=\"auto\" width=\"100%\" height=\"100%\"><source type=\"video/mp4\" src=\"'+a+'\">您的浏览器暂时无法播放此视频.</video>';NTES(\".video-inner .video\").attr(\"style\", \"background: #000;\");}h.$(\".video\")[0].innerHTML=g;},e=function(b){var a=d(b.parentNode.parentNode.parentNode);a.$(\"li\").removeCss(\"on\"),b.addCss(\"on\"),a.$(\".video-title\")[0].innerHTML=\"string\"==typeof b.textContent?b.textContent:b.innerText,a.$(\".video-title\")[0].setAttribute(\"href\",b.getAttribute(\"url\")),a.$(\".video-from\")[0].innerHTML=\"（来源：\"+b.getAttribute(\"source\")+\"）\",f(b);};window.continuePlay=function(){var a,b=d(d(\".video-list .on\")[0].nextSibling);3==b.nodeType&&(b=d(b.nextSibling));if(b&&d(\".video-inner input\")[0].checked){e(b);}},function(){var a={init:function(){if(d(\".video-list li\")[0]){d(d(\".video-list li\")[0]).addCss(\"on\"),this.eventBind();}},eventBind:function(){d(\".video-list li\").addEvent(\"click\",function(b){e(d(this)),b.preventDefault();}};a.init();}();}(NTES);"
            body = body.replace(fuck_str, "")

            file_name = '/Users/qianqian/Desktop/data/' + str(article_count) + '.txt'
            with open(file_name, 'a', encoding='utf-8') as article_f:
                article_f.write(body)

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

    print("Total" + str(article_count) + "downloaded.")
