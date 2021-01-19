import requests
import json
import pandas as pd
# 创建格式化的url
url = "http://m.maoyan.com/mmdb/comments/movie/1217513.json?_v_=yes&offset={}&startTime=2018-08-{}%2015%3A10%3A31"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/71.0.3578.80 Safari/537.36'}
cookies={'cookie':'ll="118146"; bid=TmhKuJuduXg;_pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1546327449%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DhHN2Yd4Dv0cgQ7ZjfKYJLxx5pHBfxobT_mbI7xkTpqm%26wd%3D%26eqid%3D9d9da00d000635e6000000035c2b1590%22%5D; _pk_ses.100001.8cb4=*;__utma=30149280.1984545108.1546327452.1546327452.1546327452.1; __utmc=30149280;__utmz=30149280.1546327452.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1;_pk_id.100001.8cb4=d088968fa7a76a7e.1546327449.1.1546327540.1546327449.; __utmb=30149280.4.9.1546327540915'}
date = range(20,23)
def get_json(url,k_name):
    json_str = requests.get(url=url,headers=headers).content
    data = json.loads(json_str)
    data = data[str(k_name)]
    return data
def mao_yan():
    # 先创建列标题
    df = pd.DataFrame(columns=['city','content'])
    print("开始爬取...")
    cnt = 0
    for day in date:
        try:
            for page in range(0,300):
                url1 = url.format(page * 15, str(day))
            # 最新短评
                data_cmts = get_json(url1, 'cmts')
             # 最热短评
                data_hcmts = get_json(url1, 'hcmts')
            for data_cmt in data_cmts:
                item = {}
                if cnt == 0:
                    for data_hcmt in data_hcmts:
                        item['city'] = data_hcmt['cityName']
                        item['content'] = data_hcmt['content']
                        item['date'] = data_hcmt['startTime']
                        # print(data_hcmt['content'])
                        df = df.append(item, ignore_index=True)
                    cnt += 1
                item['city'] = data_cmt['cityName']
                item['content'] = data_cmt['content']
                item['date'] = data_cmt['startTime']
                df = df.append(item, ignore_index=True)
        except Exception as e:
            # print(e)
            df.to_csv('train_.csv', encoding='utf_8_sig')
            continue
if __name__ == "__main__":
    mao_yan()
    print("爬取已结束。。。")