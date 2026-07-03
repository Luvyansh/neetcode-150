class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def rabinKarp(word1: str, word2: str) -> int:
            base1, mod1 = 31, 768258391
            base2, mod2 = 37, 685683731
            n, m = len(word1), len(word2)

            power1, power2 = 1, 1
            for _ in range(m):
                power1 = (power1 * base1) % mod1
                power2 = (power2 * base2) % mod2

            word1_hash1 = word1_hash2 = 0
            word2_hash1 = word2_hash2 = 0

            for i in range(m):
                word1_hash1 = (word1_hash1 * base1 + ord(word2[i])) % mod1
                word1_hash2 = (word1_hash2 * base2 + ord(word2[i])) % mod2
                word2_hash1 = (word2_hash1 * base1 + ord(word1[i])) % mod1
                word2_hash2 = (word2_hash2 * base2 + ord(word1[i])) % mod2

            for i in range(n - m + 1):
                if word2_hash1 == word1_hash1 and word2_hash2 == word1_hash2:
                    return i

                if i + m < n:
                    word2_hash1 = (word2_hash1 * base1 - ord(word1[i]) * power1 + ord(word1[i + m])) % mod1
                    word2_hash2 = (word2_hash2 * base2 - ord(word1[i]) * power2 + ord(word1[i + m])) % mod2

                    word2_hash1 = (word2_hash1 + mod1) % mod1
                    word2_hash2 = (word2_hash2 + mod2) % mod2

            return -1

        res = []
        words.sort(key=len)

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if rabinKarp(words[j], words[i]) != -1:
                    res.append(words[i])
                    break

        return res