# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 22:53:18 2019

@author: abhis
"""

import post
import getData

class Run():
    def run(self):
        g=getData.Images
        url='https://www.google.com/search?q=arsenal+images&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjM2NzIo9DfAhWGMd8KHZydAOMQ_AUIDigB&biw=1366&bih=626'     
        imageNumber=0
        g.getData(g,url,imageNumber)  
        
        p=post.Post
        x=input('How many do you want to post ?')
        x=int(x)
        p.KeyandPost(p,x)
        
        
if __name__=="__main__":    
    r=Run()
    r.run()