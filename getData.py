# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 18:44:41 2019

@author: abhis
"""

from bs4 import BeautifulSoup as bs
import os
import requests

class Images():
    def getData(self,url,x):
        
        #get data in html format
        page=requests.get(url)
        soup=bs(page.text,'html.parser')
        
        #parse html for images
        image=soup.find_all('img')
        
        #create directory if not present
        if not os.path.exists('pictures'):
            os.makedirs('pictures')
        
        #move
        os.chdir('pictures')
        
        for i in image:
            try:
                url=i['src']
                source=requests.get(url)
                if(source.status_code==200):
                    with open('pictures-'+str(x)+'.jpg','wb') as f:
                        f.write(requests.get(url).content)
                        f.close()
                        x+=1
            except:
                pass

if __name__=="__main__":
    url='https://www.google.com/search?q=arsenal+images&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjM2NzIo9DfAhWGMd8KHZydAOMQ_AUIDigB&biw=1366&bih=626'     
    imageNumber=0
    Images.getData(Images,url,imageNumber)