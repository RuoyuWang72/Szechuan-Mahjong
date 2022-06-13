#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:10:57 2022

@author: ruoyuwang
"""


# Convert suits to numbers.
dots = [int(i) for i in input('What dots do you have(e.g.: 1,1,2,3,etc)? ').split(',')]
bamboo = [int(i) + 10 for i in input('What bamboo do you have(e.g.: 1,1,2,3,etc)? ').split(',')]
characters = [int(i) + 20 for i in input('What characters do you have(e.g.: 1,1,2,3,etc)? ').split(',')]


mahjong_ = dots + bamboo + characters
mahjong = [i for i in mahjong_ if i not in [0,10,20]]
mahjong.sort()

class Mahjong:
    def __init__(self,mahjong,mahjong_):
        self.mahjong = mahjong
        self.mahjong_ = mahjong_
        
    def check_if_legal(self):
        if len(self.mahjong) != 13:
            return f'You have {len(self.mahjong)} inputs. Please make sure you have 13 tiles.'
        elif 0 not in self.mahjong_ and 10 not in self.mahjong_ and 20 not in self.mahjong_:
            return 'You have three suits. Please discard at least one.'
        else:
            for x in set(self.mahjong):
                if self.mahjong.count(x) > 4:
                    return f'You have {self.mahjong.count(x)} identical cards. Please make sure you have the correct input.'
            else:
                pass
        return 'Input is legal.'

    def check_if_ready(self,mahjong):
        eyes = [x for x in set(mahjong) if mahjong.count(x) >= 2]
        if len(eyes) == 0:
            return False
        if len(eyes) == 7:
            return True
        for i in eyes:
            mahjong_copy = mahjong.copy()
            mahjong_copy.remove(i)
            mahjong_copy.remove(i)
            for j in mahjong_copy:    
                if j != -1 and mahjong_copy.count(j) >= 3:
                    mahjong_copy[mahjong_copy.index(j)] = -1
                    mahjong_copy[mahjong_copy.index(j)] = -1
                    mahjong_copy[mahjong_copy.index(j)] = -1                
                elif ((j + 1) in mahjong_copy) and ((j + 2) in mahjong_copy):
                    mahjong_copy[mahjong_copy.index(j)] = -1
                    mahjong_copy[mahjong_copy.index(j + 1)] = -1
                    mahjong_copy[mahjong_copy.index(j + 2)] = -1
                else:
                    pass
            mahjong_copy = [i for i in mahjong_copy if i != -1]
            if mahjong_copy == []:
                return True
        return False
    
    def find_winning_tiles(self):
        self.winning_tiles = []
        for i in range(1,30):
            if i not in [0,10,20,30]:
                mahjong_copy = self.mahjong.copy()
                mahjong_copy.append(i)
                if self.check_if_ready(mahjong_copy) == True:
                    self.winning_tiles.append(i)

    def numbers_to_suits(self,mahjong):
        to_suits = []
        for i in mahjong:
            if 0 < i < 10:
                to_suits.append(f'{i} dot')
            elif 10 < i < 20:
                to_suits.append(f'{i-10} bamboo')
            else:
                to_suits.append('f{i-20}character')
        return to_suits
        
display = Mahjong(mahjong, mahjong_)
if display.check_if_legal() == 'Input is legal.':
    display.find_winning_tiles()
    print('Your inputs are: ')
    print(display.numbers_to_suits(mahjong))
    print('='*80)
    if len(display.winning_tiles) > 0:
        print('Your winning tiles are: ')
        print(display.numbers_to_suits(display.winning_tiles))
    else:
        print('You have not yet acquired ready hands! ')
else:
    print('Your inputs are: ')
    print(display.numbers_to_suits(mahjong))    
    print('='*80)
    print(display.check_if_legal())