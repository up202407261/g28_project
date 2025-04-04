#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 09:18:11 2025

@author: barbarafilipa2006
"""
#%%

from classes.gclass import Gclass

class Sponsor(Gclass):
   
    obj = dict()
    lst=list()
    pos=0
    sortkey=''
   
    att=['_id','_name','_contribution']
   
    header='Team'
   
    des=['Id','Name','Contribution']
 
    def __init__(self,id,name,contribution):
        super().__init__()
        
        id = Sponsor.get_id(id)
        self._id=int(id)
        self._name=name
        self._contribution=int(contribution)
       
        Sponsor.obj[id] = self
        Sponsor.lst.append(id)
       
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
    def contribution(self):
        return self._contribution
       
    @contribution.setter
    def contribution(self,contribution):
        self._contribution=contribution
        
 