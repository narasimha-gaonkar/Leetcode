class Solution:
    def fractionAddition(self, expression: str) -> str:
        if not expression:
            return "0/1"
        
        num = []
        den = []
        denominator = 1
        i = 0
        
        pos = False
        if expression[0] != '-':
            expression = '+' + expression
        
        while i < len(expression):
            pos = True if expression[i] == '+' else False
            i += 1
            n = 0
            while i < len(expression) and expression[i].isdigit():
                n = n * 10 + int(expression[i])
                i += 1
            num.append(n if pos else -n)
            
            i += 1
            d = 0
            while i < len(expression) and expression[i].isdigit():
                d = d * 10 + int(expression[i])
                i += 1
            denominator *= d
            den.append(d)
        # print(num, den)
        # print('denominator', denominator)
        for j in range(len(num)):
            num[j] = (num[j] * denominator)/ den[j]
        num_sum = sum(num)
        # print(num_sum, denominator)
        gcd = math.gcd(int(num_sum), int(denominator))
        numerator = int(num_sum) // gcd
        denominator = int(denominator) // gcd
        
        return f'{numerator}/{denominator}'
            
            
        
                
                
                
            
        