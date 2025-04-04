#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 09:17:05 2025

@author: barbarafilipa2006
"""
#%%

import datetime as dt

from classes.gclass import Gclass

class Game(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    
    att = ['_id','_team_id','_tournament_id' ,'_participation_date', '_result']
    
    header = 'Game'
    
    des = ['Id','Team_Id','Tournament_Id','Participation Date', 'Result']
    
    def __init__(self, id,team_id, tournament_id, participation_date, result):
        super().__init__()
        
        id = Game.get_id(id)
        self._id = id
        self._team_id = team_id
        self._tournament_id = tournament_id
        self._participation_date = dt.date.fromisoformat(participation_date)
        self._result = result
        

        Game.obj[id] = self
        Game.lst.append(id)
    
    @property
    def id(self):
        return self._id
    
    @property
    def team_id(self):
        return self._id
    
    @property
    def tournament_id(self):
        return self._tournament_id
    
    
    @property
    def participation_date(self):
        return self._participation_date
    
    @participation_date.setter
    def participation_date(self, value):
        self._participation_date = value
    
    @property
    def result(self):
        return self._result
    
    @result.setter
    def result(self, value):
        self._result = value
