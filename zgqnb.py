import requests
'https://ipvv.183read.cc/zxh_api/v1/?act=newspaper.get.pc.data&param=%7B%22resource_id%22:%22%22,%22item_id%22:968451,%22page_id%22:1390960760,%22imei%22:%22e8d5d850761c3ecb4442b4fa3ebf86bd%22,%22platform%22:3,%22use_https%22:%221%22,%22version_num%22:%221.0.0%22,%22token%22:null,%22version%22:1%7D&ts=1742454699&nonce=3fDef7d13a8e36Ed9f4ceDdAE6deC35b&sign=9f1ddc46165e37264b51caf4204fac3e&app_key=337439fef71af08fe85942ebd690e43f'

'https://ipvv.183read.cc/zxh_api/v1/?act=newspaper.get.pc.data&param=%7B%22resource_id%22:%22%22,%22item_id%22:968451,%22page_id%22:1390960759,%22imei%22:%22e8d5d850761c3ecb4442b4fa3ebf86bd%22,%22platform%22:3,%22use_https%22:%221%22,%22version_num%22:%221.0.0%22,%22token%22:null,%22version%22:1%7D&ts=1742454684&nonce=3A45d2eE29cAc972CC4cbb3b57f5a5E3&sign=3fadc3d73ec0473f4894d0f0cae6c194&app_key=337439fef71af08fe85942ebd690e43f'





def get_pageinfo():
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Origin": "https://rmzxb.183read.cc",
        "Referer": "https://rmzxb.183read.cc/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://ipvv.183read.cc/zxh_api/v1/"
    page_id = '137305139'
    params = {
        "act": "newspaper.get.pc.data",
        "param": f"{{\"resource_id\":\"\",\"item_id\":627436,\"page_id\":{page_id},\"imei\":\"e8d5d850761c3ecb4442b4fa3ebf86bd\",\"platform\":3,\"use_https\":\"1\",\"version_num\":\"1.0.0\",\"token\":null,\"version\":1}}",
        "ts": "1742453168",
        "nonce": "B164B402Ac7aea3D5A3A07DcB45cCDA2",
        "sign": "24c131bf4dfdf35b574db21bca53d10a",
        "app_key": "337439fef71af08fe85942ebd690e43f"
    }
    response = requests.get(url, headers=headers, params=params)
    dict = response.json()
    pageId_list = dict['result']['page_list']
    page_article_list = dict['result']['page_info']['article_list']
    pageids = []
    articles = []
    for id in pageId_list:
        pageId = id['page_id']
        pageids.append(pageId)
        # print(pageId)
    # for temp in page_article_list:
    #     article_id = temp['magazine_article_id']
    #     articles.append(article_id)
        # print(article_id)
    # result_list = [(pageid,articleid) for pageid,articleid in zip(pageids,articles)]
    return pageids


def parse_pageinfo(pageId,time_id):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Origin": "https://rmzxb.183read.cc",
        "Referer": "https://rmzxb.183read.cc/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://ipvv.183read.cc/zxh_api/v1/"
    params = {
        "act": "newspaper.get.pc.data",
        "param": f"{{\"resource_id\":\"\",\"item_id\":{time_id},\"page_id\":{pageId},\"imei\":\"e8d5d850761c3ecb4442b4fa3ebf86bd\",\"platform\":3,\"use_https\":\"1\",\"version_num\":\"1.0.0\",\"token\":null,\"version\":1}}",
        "ts": "1742453168",
        "nonce": "B164B402Ac7aea3D5A3A07DcB45cCDA2",
        "sign": "24c131bf4dfdf35b574db21bca53d10a",
        "app_key": "337439fef71af08fe85942ebd690e43f"
    }
    response = requests.get(url, headers=headers, params=params)
    dict = response.json()
    title1 = dict['result']['page_info']['page_number'] + dict['result']['page_info']['page_name']
    return title1

def get_time_id(pageId):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Origin": "https://rmzxb.183read.cc",
        "Referer": "https://rmzxb.183read.cc/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://ipvv.183read.cc/zxh_api/v1/"
    params = {
        "act": "newspaper.get.pc.data",
        "param": f"{{\"resource_id\":\"\",\"item_id\":627436,\"page_id\":{pageId},\"imei\":\"e8d5d850761c3ecb4442b4fa3ebf86bd\",\"platform\":3,\"use_https\":\"1\",\"version_num\":\"1.0.0\",\"token\":null,\"version\":1}}",
        "ts": "1742453168",
        "nonce": "B164B402Ac7aea3D5A3A07DcB45cCDA2",
        "sign": "24c131bf4dfdf35b574db21bca53d10a",
        "app_key": "337439fef71af08fe85942ebd690e43f"
    }
    response = requests.get(url, headers=headers, params=params)
    dict = response.json()
    next_time_id = dict['result']['item_info']['last_next_info']['next_item_id']
    return  next_time_id
    # print(next_time_id)


def get_article_id_list(page_id):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Origin": "https://rmzxb.183read.cc",
        "Referer": "https://rmzxb.183read.cc/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://ipvv.183read.cc/zxh_api/v1/"

    params = {
        "act": "newspaper.get.pc.data",
        "param": f"{{\"resource_id\":\"\",\"item_id\":627436,\"page_id\":{page_id},\"imei\":\"e8d5d850761c3ecb4442b4fa3ebf86bd\",\"platform\":3,\"use_https\":\"1\",\"version_num\":\"1.0.0\",\"token\":null,\"version\":1}}",
        "ts": "1742453168",
        "nonce": "B164B402Ac7aea3D5A3A07DcB45cCDA2",
        "sign": "24c131bf4dfdf35b574db21bca53d10a",
        "app_key": "337439fef71af08fe85942ebd690e43f"
    }
    response = requests.get(url, headers=headers, params=params)
    dict = response.json()
    page_article_list = dict['result']['page_info']['article_list']
    articles = []
    for id in page_article_list:
        articleid = id['magazine_article_id']
        articles.append(articleid)

    return articles
        # print(articleid)


def parse_articleinfo(article_id,name):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Origin": "https://rmzxb.183read.cc",
        "Referer": "https://rmzxb.183read.cc/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://ipvv.183read.cc/zxh_api/v1/"

    params_article = {
        "act": "newspaper.article.info.get",
        "param": f"{{\"article_id\":{article_id},\"platform\":3,\"use_https\":\"1\",\"version_num\":\"1.0.0\",\"token\":null,\"version\":1}}",
        "ts": "1742457724",
        "nonce": "ECA6C6C727Cdf6ea2ac5d69079443952",
        "sign": "a052244ffd2d41899407e3049760116e",
        "app_key": "337439fef71af08fe85942ebd690e43f"
    }
    response = requests.get(url, headers=headers, params=params_article)

    dict = response.json()
    content = dict['result']['newspaper_article_info']['content'].replace('<p>','').replace('</p>','').strip()
    article = dict['result']['newspaper_article_info']['title']
    author = dict['result']['newspaper_article_info']['author']

    dict = {
        '网站域名': 'rmzxb.183read.cc',
        '中文域名': '人民政协报',
        '文章ID': article_id,
        '一级栏目': name,
        '二级栏目': article,
        '作者': author,
        '文章内容': content
    }
    print(dict)


def main():
    page_list = get_pageinfo()
    for pageid in page_list:
        get_time_id(pageid)
        title = parse_pageinfo(pageid)
        article_id_list = get_article_id_list(pageid)
        for articleid in article_id_list:
            parse_articleinfo(articleid,title)


if __name__ == '__main__':
    main()
