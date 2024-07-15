class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        loser_dict = {}
        winner_dict = {}

        for match in matches:
            winner_dict[match[0]] = winner_dict.get(match[0], 0) + 1
            loser_dict[match[1]] = loser_dict.get(match[1], 0) + 1
        winners = [
            player for player, count in winner_dict.items()
            if count > 0 and player not in loser_dict
        ]
        losers = [
            player for player, count in loser_dict.items() if count == 1
        ]
        return [sorted(winners), sorted(losers)]

# not fast on runtime but great on memory
