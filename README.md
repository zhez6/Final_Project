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
5. The game ends either when player X is eliminated or player X becomes the final winner. 
6. Each game must have a winner. If there are only two players standing on the ground and they hit each other in which the damages are over HP simultaneously, a winner will be randomly chosen.  

**Special game conditions:**
1.	Select high magnification scope: increase X% shooting rate, but will reduce the ability to resist damage Y%
2.	Choose body armor: increase the capability that resists damage by Y%., but will reduce the shooting hit rate X%
3.	Use the default settings 

As the chance for any player to win a game is quite low, we will simulate 100,000 times to make better estimations. 

**We plan to explore the following areas:** 
1.	The chance for player X to win the game 
2.	For player X, choosing which option can increase his chance to win most? 

**Hypotheses:**
1. The chance of player X to win the game is three times higher than that of other players 
2. For player X, selecting high magnificent scope can increase his chance to win most
3. Player X is likely to survive after 10 rounds in a game

**Simulation variables:**  
1. basic_acc: basic accuracy of the player X  
2. acc_change: the amount of accuracy change of skill 1 and 2  
3. def_change: the amount of defence change of skill 1 and 2  
4. other_acc: the mean accuracy of other players  
5. acc_std: the standard deviation accuracy of other players  
6. num_players: the number of players in the game, including the main character  
7. head_percentage: the percentage one person shoots another person in his head  
8. head_mean_damage: the mean damage when shooting a person in his head  
9. head_std_damage: the standard deviation damage when shooting a person in his head  
10. body_mean_damage: the mean damage when shooting a person in his body  
11. body_std_damage: the standard deviation damage when shooting a person in his body  
        
The above param will be stored in self.param. In addition, two other params will be calculated after  
the main character choosing his ability.  

1. self.acc: the accuracy of the main character after choosing the ability  
2. self.blood: the actual HP of the main character after choosing the ability  

**Preliminary results:**
1) Select skill one: increase 10% shooting rate, but will reduce the ability to resist damage 5%  
   Winning rate of Player X: 1.147%  
   Average winning rate of other characters: 0.999%
   ![Image text](https://github.com/zhez6/Final_Project/blob/master/Choose%20Skill%20One.png)
2) Select skill two: increase the capability that resists damage by 10%., but will reduce the shooting hit rate 5%  
   Winning rate of Player X: 0.810%  
   Average winning rate of other characters: 1.002%  
   ![Image text](https://github.com/zhez6/Final_Project/blob/master/Choose%20Skill%20Two.png)
3) Use the Default settings  
   Winning rate of Player X: 1.018%  
   Average winning rate of other characters: 1.000%  
   ![Image text](https://github.com/zhez6/Final_Project/blob/master/Default%20settings.png)

**Conclusion:**
1. Based on our preliminary results, the winning chance of player X, no matter what option he may choose, is not
significant higher than the average winning chance of other players.Thus, hypothesis 1 seems to be incorrect. 
2. From the simulation results, the selecting skill one (i.e. selecting high magnificent scope) increases Player X's chance of 
winning most. Thus, hypothesis two seems to be reasonable. 
3. From the Frequency vs The number of rounds when a game ends histograms, the probability of player X to survive after 
10 rounds in each game is quite small. Thus, hypothesis three seems to be incorrect. 

**References:**

GAMEPLAY RELATED. Retrieved from https://support.pubg.com/hc/en-us/categories/115000247733-GAMEPLAY-RELATED  

Networks. Retrieved from https://blogs.cornell.edu/info2040/2015/09/22/gunmans-dilemma-strategy-of-the-underdog/  

Tapsell, C. (2019, March 20). PUBG weapon damage stats - Bizon stats, damage chart and the best weapons in PUBG. Retrieved from https://www.eurogamer.net/articles/2019-03-20-pubg-weapon-damage-stats-best-weapons-5414#section-1




