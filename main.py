import numpy as np
import time
import matplotlib.pyplot as plt
import collections


class Game:
    def __init__(self, basic_acc, acc_change, def_change, other_acc, acc_std, num_players,
                 head_percentage, head_mean_damage, head_std_damage, body_mean_damage, body_std_damage):
        """
        :param basic_acc: basic accuracy of the main character
        :param acc_change: the amount of accuracy change of skill 1 and 2
        :param def_change: the amount of defence change of skill 1 and 2
        :param other_acc: the mean accuracy of other players
        :param acc_std: the standard deviation accuracy of other players
        :param num_players: the number of players in the game, including the main character
        :param head_percentage: the percentage one person shoots another person in his head
        :param head_mean_damage: the mean damage when shooting a person in his head
        :param head_std_damage: the standard deviation damage when shooting a person in his head
        :param body_mean_damage: the mean damage when shooting a person in his body
        :param body_std_damage: the standard deviation damage when shooting a person in his body
        The above param will be stored in self.param. In addition, two other params will be calculated after
        the main character choosing his ability.
        self.acc: the accuracy of the main character after choosing the ability
        self.blood: the actual blood of the main character after choosing the ability
        """
        self.basic_acc = basic_acc
        self.acc_change = acc_change
        self.def_change = def_change
        self.other_acc = other_acc
        self.acc_std = acc_std
        self.num_players = num_players
        self.head_percentage = head_percentage
        self.head_mean_damage = head_mean_damage
        self.head_std_damage = head_std_damage
        self.body_mean_damage = body_mean_damage
        self.body_std_damage = body_std_damage

    def choose_skill(self, skill):
        """
        According to the skill the main character choose, initialize his accuracy and blood.
        :param skill: The number of skill the character wants to choose.
        If 0, use the default accuracy and defence.
        If 1, improve the accuracy and reduce the defence.
        If 2, imporve the defence and reduce accuracy.
        Otherwise raise an Exception.
        :return: None
        """
        if skill == 0:
            self.acc = self.basic_acc
            self.blood = 100
        elif skill == 1:
            self.acc = self.basic_acc + self.acc_change
            self.blood = 100 / (1 + self.def_change)
        elif skill == 2:
            self.acc = self.basic_acc - self.acc_change
            self.blood = 100 / (1 - self.def_change)
        else:
            raise Exception('Please input a valid choice.')

    def start_a_game(self):
        """
        Start a game and get the result of this game.
        :return: bool and int. The bool value means whether the main character wins the game.
        The integer means the number of rounds a game has.
        """
        blood, accuracy = self.initialize_a_game()
        num_players = self.num_players
        num_round = 0
        while True:
            num_round += 1
            target = self.set_target(num_players)
            damage = self.generate_hit_damage(target, accuracy, num_players)
            blood = blood - damage
            # print(blood)
            if blood[0] > 0 and np.sum(blood > 0) == 1:
                return True, num_round
            if blood[0] <= 0:
                if np.sum(blood > 0) == 0:
                    return True, num_round
                else:
                    return False, num_round
            accuracy = accuracy[blood > 0]
            num_players = np.sum(blood > 0)
            blood = blood[blood > 0]

    def initialize_a_game(self):
        """
        Initialize the accuracy and blood of all players.
        :return: None
        """
        blood = np.array([self.blood] + [100] * (self.num_players-1))
        accuracy = np.r_[self.acc, np.random.randn(self.num_players-1) * self.acc_std + self.other_acc]
        accuracy = np.clip(accuracy, 0, 1)
        return blood, accuracy

    def set_target(self, num_players):
        """
        Initiate all the targets in a round. The target of a person is uniformly random.
        Since no one should shoot himself, we will reset the target until no one's target is himself.
        :param num_players: the remaining number of players in the game.
        :return: None
        """
        res = np.random.randint(0, num_players, num_players)
        while np.sum(res == np.arange(num_players)) != 0:
            res = np.random.randint(0, num_players, num_players)
        return res

    def generate_hit_damage(self, target, accuracy, num_players):
        """

        :param target:
        :param accuracy:
        :param num_players:
        :return:
        """
        hit_or_not = np.random.binomial(1, accuracy)
        head_or_body = np.random.binomial(1, [self.head_percentage]*num_players)
        head_damage = np.random.rand(num_players) * self.head_std_damage + self.head_mean_damage
        head_damage = np.clip(head_damage, 0, None)
        body_damage = np.random.rand(num_players) * self.body_std_damage + self.body_mean_damage
        body_damage = np.clip(body_damage, 0, None)
        actual_damage = head_or_body * head_damage + (1 - head_or_body) * body_damage
        damage = np.zeros(num_players)
        for i in range(num_players):
            if hit_or_not[i]:
                damage[target[i]] += actual_damage[i]
        return damage * 100


num_game = 100000
g = Game(0.5, 0.1, 0.05, 0.5, 0.05, 100, 0.3, 0.9, 0.06, 0.45, 0.03)
g.choose_skill(0)
count = 0
round = []
tic = time.time()
for j in range(num_game):
    a, b = g.start_a_game()
    if a:
        count += 1
    round.append(b)
toc = time.time()
print('Running time:', str(toc - tic)+'s')
print('Winning rate of main character:', str(count/num_game*100)+'%')
print('Winning rate of other characters:', str((100-count/num_game*100)/99)+'%')
count = collections.Counter(round)
plt.hist(round, bins=len(count), density=1, edgecolor="black")
plt.show()
