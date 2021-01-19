import requests
import time
import random
import json
import pandas as pd


movie = pd.DataFrame(columns=['city','content'])
for i in range(0, 300):
    j = random.randint(1,300)
    print(str(i)+' '+str(j))
    try:
        time.sleep(2)
        url= "http://m.maoyan.com/mmdb/comments/movie/1217513.json?_v_=yes&offset=" + str(j)
        html = requests.get(url=url).content
        data = json.loads(html.decode('utf-8'))['cmts']

        for item in data:
            movie = movie.append({'city':item['cityName'],
                                    'content':item['content'],'date':item['startTime']},ignore_index=True)
            movie.to_excel('风雨骤.xlsx',index=False)
    except:
        continue