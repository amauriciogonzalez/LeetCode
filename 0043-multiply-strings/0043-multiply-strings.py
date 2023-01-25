class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if "0" == num1 or "0" == num2:
            return "0"

        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) -1, -1, -1):
                result[i + j + 1] += int(num1[i]) * int(num2[j])
                result[i + j] += result[i + j + 1] // 10
                result[i + j + 1] %= 10

        num = ""
        i = 0
        while result[i] == 0:
            i += 1
        while i < len(result):
            num = num + str(result[i])
            i += 1
        return num

