import numpy as np
import time
import matplotlib.pyplot as plt

# class Game:
#     def __init__(self, b_acc, b_esc, skill_1_up_acc, skill_1_down_esc, skill_2_down_acc, skill_2_up_esc, num_players):
#         self.b_acc = b_acc
#         self.b_esc = b_esc
#         self.skill_1_up_acc = skill_1_up_acc
#         self.skill_1_down_esc = skill_1_down_esc
#         self.skill_2_up_esc = skill_2_up_esc
#         self.skill_2_down_acc = skill_2_down_acc
#         self.num_players = num_players
#         if self.b_acc + self.skill_1_up_acc > 1:
#             print('Skill 1 accuracy increase too much!')
#             raise Exception('Please reduce skill 1 accuracy increase.')
#         if self.b_esc - self.skill_1_down_esc < 0:
#             print('Skill 1 escape decrease too much!')
#             raise Exception('Please reduce skill 1 escape decrease')
#         if self.b_acc - self.skill_2_down_acc < 0:
#             print('Skill 2 accuracy decrease too much!')
#             raise Exception('Please reduce skill 2 accuracy decrease.')
#         if self.b_esc + self.skill_2_down_acc > 1:
#             print('Skill 2 escape increase too much!')
#             raise Exception('Please reduce skill 2 escape increase.')
#
#     def set_target(self, num_players):
#         res = np.random.randint(0, num_players, num_players)
#         while np.sum(res == np.arange(num_players)) != 0:
#             res = np.random.randint(0, num_players, num_players)
#         return res
#
#     def choose_skill(self, skill):
#         if skill == 0:
#             self.acc = self.b_acc
#             self.esc = self.b_esc
#         elif skill == 1:
#             self.acc = self.b_acc + self.skill_1_up_acc
#             self.esc = self.b_esc - self.skill_1_down_esc
#         elif skill == 2:
#             self.acc = self.b_acc - self.skill_2_down_acc
#             self.esc = self.b_esc + self.skill_2_up_esc
#         else:
#             raise Exception('Please input a valid choice.')
#
#     def hit_a_round(self, num_players):
#         target = self.set_target(num_players)
#         accuracy = np.array([self.acc] + [self.b_acc] * (num_players - 1))
#         escape = np.array([self.esc] + [self.b_esc] * (num_players - 1))
#         hit = np.random.binomial(1, accuracy)
#         hit = target[hit != 0]
#         hit_count = np.zeros(num_players, dtype=int)
#         count = np.unique(hit, return_counts=True)
#         hit_count[count[0]] = count[1]
#         escape_needed = escape ** hit_count
#         random_escape = np.random.rand(num_players)
#         survivors = random_escape < escape_needed
#         if np.sum(survivors) == 0:
#             return True, 0
#         else:
#             return survivors[0], np.sum(survivors)
#
#     def start_a_game(self):
#         num_players = self.num_players
#         while True:
#             main_player, num_players = self.hit_a_round(num_players)
#             if not main_player:
#                 return False
#             if num_players == 0 or num_players == 1:
#                 return True
#
#
# G = Game(b_acc=0.5, b_esc=0.1, skill_1_up_acc=0.3, skill_1_down_esc=0.05,
#          skill_2_up_esc=0.3, skill_2_down_acc=0.05, num_players=100)
# G.choose_skill(2)
# count_ = 0
# tic = time.time()
# for i in range(100000):
#     res = G.start_a_game()
#     if res:
#         count_ += 1
# toc = time.time()
# print(toc - tic)
# print(count_/100000)


class Game2:
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


g = Game2(0.5, 0.3, 0.1, 0.5, 0.05, 100, 0.3, 0.85, 0.05, 0.4, 0.1)
g.choose_skill(2)
count = 0
round = []
tic = time.time()
for j in range(10000):
    a, b = g.start_a_game()
    if a:
        count += 1
    round.append(b)
toc = time.time()
print(toc - tic)
print(count)

plt.hist(round, bins=20, normed=1, edgecolor="black")
plt.show()