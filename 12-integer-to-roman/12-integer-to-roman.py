class Solution:
    def intToRoman(self, num: int) -> str:
        # 1,4,5,9,10,40,50,90,100,400,500,900,1000
        dic = {1000:'M',900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50: "L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV",1:"I"}
        res = ""
        
        for I, R in dic.items():
            n = (num//I)
            res += R*n
            num -= I*n
            
        return res
            