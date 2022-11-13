#!/usr/bin/env python
# coding: utf-8

# # Rock Paper Scissors Game

# In[11]:




opcion_jugador_1 = input('Escribe aqui tu opcion: ')
opcion_jugador_2 = input('Escribe aqui tu opcion: ')

rock = 'rock'
paper = 'paper'
scissors = 'scissors'

opcion_jugador_1 = opcion_jugador_1.lower()
opcion_jugador_2 = opcion_jugador_2.lower()

if opcion_jugador_1 == rock and opcion_jugador_2 == rock:
    print("its a tie")
elif opcion_jugador_1 == rock and opcion_jugador_2 == scissors:
    print("player 1 wins")
elif opcion_jugador_1 == rock and opcion_jugador_2 == paper:
     print("player 2 wins")
elif opcion_jugador_1 == scissors and opcion_jugador_2 == scissors:
    print("its a tie")
elif opcion_jugador_1 == scissors and opcion_jugador_2 == rock:
    print("player 2 wins")
elif opcion_jugador_1 == scissors and opcion_jugador_2 == paper:
    print("player 1 wins")
elif opcion_jugador_1 == paper and opcion_jugador_2 == paper:
    print("its a tie")
elif opcion_jugador_1 == paper and opcion_jugador_2 == rock:
    print("player 1 wins")
elif opcion_jugador_1 == paper and opcion_jugador_2 == scissors:
    print("player 2 wins")
else:
    print('no one wins')


# # Random Investment Profit

# In[3]:



import random

#investment = (100, 1000, 10000)
profit = (0.5, -2, 1.5)

user_option = input("Elige una cantidad a invertir: ")
profit_random = random.choice(profit)

print("Elegiste invertir: ", user_option)

if profit_random == 0.5:
    print("Tu ganancia fue de: ", profit_random, "%")
elif profit_random == -2:
    print("Tuviste una perdida de: ", profit_random, "%")
else:
    print("Tu ganancia fue de: ", profit_random, "%")
    


# # Rock Paper Scissors with Loops

# In[18]:


rounds = 1
player1_wins = 0
player2_wins = 0


while True: 
    
    print("ROUND ", rounds)
    opcion_jugador_1 = input('Escribe aqui tu opcion: ')
    opcion_jugador_2 = input('Escribe aqui tu opcion: ')

    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'

    opcion_jugador_1 = opcion_jugador_1.lower()
    opcion_jugador_2 = opcion_jugador_2.lower()

    if opcion_jugador_1 == rock and opcion_jugador_2 == rock:
        print("its a tie")
    elif opcion_jugador_1 == rock and opcion_jugador_2 == scissors:
        print("player 1 wins")
        player1_wins += 1
    elif opcion_jugador_1 == rock and opcion_jugador_2 == paper:
        print("player 2 wins")
        player2_wins += 1
    elif opcion_jugador_1 == scissors and opcion_jugador_2 == scissors:
        print("its a tie")
    elif opcion_jugador_1 == scissors and opcion_jugador_2 == rock:
        print("player 2 wins")
        player2_wins += 1
    elif opcion_jugador_1 == scissors and opcion_jugador_2 == paper:
        print("player 1 wins")
        player1_wins += 1
    elif opcion_jugador_1 == paper and opcion_jugador_2 == paper:
        print("its a tie")
    elif opcion_jugador_1 == paper and opcion_jugador_2 == rock:
        print("player 1 wins")
        player1_wins += 1 
    elif opcion_jugador_1 == paper and opcion_jugador_2 == scissors:
        print("player 2 wins")
        player2_wins += 1
    else:
        print('no one wins')

    rounds += 1
    
    if player1_wins == 3:
        print('Player 1 wins the game.')
        break 
        
    if player2_wins == 3:
        print('Player 2 wins the game.')
        break
    
    


# In[ ]:





# In[ ]:




