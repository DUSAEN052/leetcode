from collections import Counter
from collections import defaultdict

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        output = set()
        visited = Counter(tiles)
        curr = defaultdict(int)
        
        self.find_seq([], tiles, curr, visited, output)
        
        return len(output) - 1
        
    def find_seq(self, seq, tiles, curr, visited, output):
        if len(seq) <= len(tiles):
            output.add(''.join(seq))
        for letter in tiles:
            if curr[letter] + 1 <= visited[letter]:
                seq.append(letter)
                curr[letter] += 1
                self.find_seq(seq, tiles, curr, visited, output)
                seq.pop()
                curr[letter] -= 1
