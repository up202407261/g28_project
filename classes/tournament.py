#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 09:18:52 2025

@author: barbarafilipa2006
"""

#%%

from classes.gclass import Gclass

class Tournament(Gclass):
    
    obj = dict()
    lst=list()
    pos=0
    sortkey=''
    
    att=['_id','_prize_pool','_name','_location','_sponsor_id']
    
    header='Tournament'
    
    des=['Id','Prize_Pool','Name','Location','Sponsor_Id']

    def __init__(self,id,prize_pool,name,location,sponsor_id):
        super().__init__()
        
        id =Tournament.get_id(id)
        self._id=id
        self._prize_pool=prize_pool
        self._name=name
        self._location=location
        self._sponsor_id=sponsor_id

        
        Tournament.obj[id] = self
        Tournament.lst.append(id)
        
    @property
    def id(self):
        return self._id
      
    @property
    def prize_pool(self):
        return self._prize_pool
   
    @prize_pool.setter
    def prize_pool(self,prize_pool):
        self._prize_pool=prize_pool
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self,name):
        self._name=name

    @property
    def location(self):
        return self._location
        
    @location.setter
    def location(self,location):
        self._location=location
    
    @property
    def sponsor_id(self):
        return self._sponsor_id
        
