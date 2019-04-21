# 590PR Final Project 


**Title: Monte Carlo Simulation – Who will survive?**

Team Members: Zhe Zhang, Gangfeng Huang 

**Project Description:**
This project is inspired by the video game, PlayUnkown’s Battlegrounds (PUBG), and attempts to simulate a set of conditions and find out the game winner. 

**Basic game conditions:**
1.	There are 100 players in each game, and the last player standing on the ground is the winner. In each game, the shooting hit rate of the players follows a normal distribution. 
2.	At the beginning of each game, each player’s shooting hit rate will be reset. 
3.	Each player has an HP value of 100. When HP is less than or equal to 0, the player will be eliminated. 
4.	The damage to players who get shot depend on which body parts are shot. There is 30% of chance being shot on head and 70% on other body parts. The damage to the head and the damage to other parts of the body follow normal distribution as well. 

**Special game conditions:**
1.	Select high magnification scope: increase X% shooting rate, but will reduce the ability to resist damage Y%
2.	Choose body armor: increase the capability that resists damage by Y%., but will reduce the shooting hit rate X%
3.	Use the initial settings 

As the chance for any player to win a game is quite low, we will simulate 100,000 times to make better estimations. 

**We plan to explore the following areas:** 
1.	The chance for player X to win the game 
2.	For player X, choosing which option can increase his chance to win most? 

**Hypotheses:**
1.	The change of player X to win the game is three times higher than that of other players 
2.	For player X, selecting high magnificent scope can increase his chance to win most

**Simulation variables:**

**Preliminary results:**

**References:**
