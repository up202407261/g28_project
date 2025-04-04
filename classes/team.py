#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 09:19:38 2025

@author: barbarafilipa2006
"""
#%%

from classes.gclass import Gclass

class Team(Gclass):
    
    obj = dict()
    lst=list()
    pos=0
    sortkey=''
    
    att=['_id','_name','_region','_ranking']
    
    header='Team'
    
    des=['Id','Name','Region','Ranking']

    def __init__(self,id,name,region,ranking):
        super().__init__()
        
        id = Team.get_id(id)
        self._id=id
        self._name=name
        self._region=region
        self._ranking=int(ranking)
        
        Team.obj[id] = self
        Team.lst.append(id)
        
    @property
    def id(self):
        return self._id

    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name=name

    @property
    def region(self):
        return self._region
        
    @region.setter
    def region(self,region):
        self._region=region
        
    @property
    def ranking(self):
        return self._ranking
    
    @ranking.setter
    def ranking(self,ranking):
        self._ranking=ranking