class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def permutation(string, num, builder, output):
            if num == len(string):
                output.append(builder)
            else: 
                if string[num].isalpha():
                    permutation(string, num + 1, builder + string[num].swapcase(), output)
                permutation(string, num + 1, builder + (string[num]), output)
        
        output = []
        builder = ""
        permutation(S, 0, builder, output)
        return output
        