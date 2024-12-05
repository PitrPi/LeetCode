class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        if len(s1) < len(s2):
            s2, s1 = s1, s2
        # s1 is always longer
        for idx, (a, b) in enumerate(zip(s1, s2)):
            if a != b:
                break
            if idx + 1 >= len(s2):
                return True

        for idx_back, (a, b) in enumerate(zip(reversed(s1), reversed(s2))):
            if a != b:
                break
            if idx_back + 1 >= len(s2):
                return True

        return idx + idx_back >= len(s2)


if __name__ == "__main__":
    sentence1 = "A B C D B B"
    sentence2 = "A B B"
    Solution().areSentencesSimilar(sentence1, sentence2)

    sentence1 = "of"
    sentence2 = "A lot of words"
    Solution().areSentencesSimilar(sentence1, sentence2)
