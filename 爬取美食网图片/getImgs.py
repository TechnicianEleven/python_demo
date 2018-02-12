import requests
import re
content=requests.get('http://home.meishichina.com/recipe.html').text
match_src=re.compile('<img.*?data-src="(.*?)">',re.S)
lists=re.findall(match_src,content)
n=1
for item in lists:
    html = requests.get(item)
    n=int(n)+1
    with open('imgs/picture'+str(n)+'.jpg', 'wb') as file:
      file.write(html.content)
    

