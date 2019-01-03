# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 19:03:13 2019

@author: abhis
"""

import tweepy as tp
import os
import time

class Post():
    def KeyandPost(self,number):
        
        #access token
        consumer_key='###############'
        consumer_secret='###############'
        access_token='###############-###############'
        access_secret='###############'
        
        #login
        auth=tp.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_secret)
        api=tp.API(auth)
        
        #iterates over images in pictures folder
        os.chdir('pictures')
        x=0
        for img in os.listdir('.'):
            if(x==number):
                break
            api.update_with_media(img)
            time.sleep(25)
            x+=1



    
    
