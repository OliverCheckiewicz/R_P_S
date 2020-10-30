#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:23:04 2019

@author: Oliver Checkiewicz
"""


import random as r

options = ['Rock', 'Paper', 'Scissors']

playing = "yes"

while playing == "yes":
    
    player = input('choose Rock Paper Scissors !')
    
    random_index = r.randint(0,2)
    
    
    computer = options[random_index]
    
    
    if player == computer:
            print("Tie!")     
            
    elif player == 'Rock' and computer == 'Paper':
            print("Computer wins")
            
    elif player == 'Paper' and computer == 'Rock':
            print("Player wins")   
          
    elif player == 'Scissors' and computer == 'Paper':
            print("Player wins")
              
    elif player == 'Paper' and computer == 'Scissors':
            print("Computer wins")   
    
    elif player == 'Rock' and computer == 'Scissors':
            print("player wins") 
        
    elif player == 'Scissors' and computer == 'Rock':
            print("Computer wins")  
    else:
            print("That's not a valid play. Check your spelling!")
    
    playing = input('Do you want to play again yes/no)')
    
    if playing == 'no':
        print('thank you for playing')
        break 


    




#    
#    
#if computer == "Paper":
#            print("You lose!", computer, "covers", player)
#else:
#    print("You win!", player, "smashes", computer)
#elif player == "Paper":
#if computer == "Scissors":
#            print("You lose!", computer, "cut", player)
#else:
#    print("You win!", player, "covers", computer)
#elif player == "Scissors":
#if computer == "Rock":
#            print("You lose...", computer, "smashes", player)
#else:
#    print("You win!", player, "cut", computer)
#else:
#    print("That's not a valid play. Check your spelling!")