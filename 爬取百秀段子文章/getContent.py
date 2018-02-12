import urllib.request
import urllib
import re
class QSBK(object):
    def __init__(self):#define variable and constant
        self.pageIndex=1
        self.user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64gent'
        self.headers={'User-Agent':self.user_agent}
        self.stories=[]
        self.enable=False
    def getPage(self):#get webPage
        try:
            url='http://www.qiushibaike.com/8hr/page/'+str(self.pageIndex)
            req=urllib.request.Request(url,headers=self.headers)
            resp=urllib.request.urlopen(req)
            resp_data=resp.read().decode('utf-8')
            return resp_data
        except urllib.error.URLError as e:
            print ('except:',e)

    def getPageStory(self):#match paragraph 
        PageStory=[]
        match_Story=re.compile('title=.*?<h2>(.*?)</h2>.*?class="content">.*?<span>(.*?)</span>.*?number">(.*?)</i>.*?number">(.*?)</i>',re.S)
        items=re.findall(match_Story,self.getPage())
        return items
        
 
        #print ( (str(item[0]),'\n',str(item[1]).replace('<br/>',''),'\n','好笑：',item[2],'评论：',item[3]))            
    def getOneStory(self):# press enter next story
        L=len(self.getPageStory())
        S=self.getPageStory()
        onestory=[]
        n=0
        for N in range(L):
            onestory.append(str(S[N][0])+'\n'+str(S[N][1]).replace('<br/>','')+'\n'+'好笑：'+str(S[N][2])+'\n'+'评论：'+str(S[N][3]))
        while L>0:
            print (onestory[n])
            input()
            n=n+1
            L=L-1
            if L<=0:
                self.pageIndex=self.pageIndex+1
                return self.getOneStory()
        
         
S=QSBK()
S.getOneStory()