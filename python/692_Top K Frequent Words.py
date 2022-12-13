from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        words_counter = Counter(words)
        return [word for word, occurrence in sorted(words_counter.most_common(), key=lambda i: (-i[1], i[0]))[:k]]
