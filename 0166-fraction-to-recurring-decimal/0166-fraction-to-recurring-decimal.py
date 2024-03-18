class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

    
        sign = "-" if numerator * denominator < 0 else ""

        numerator = abs(numerator)
        denominator = abs(denominator)


        integer_part = numerator // denominator
        remainder = numerator % denominator
        decimal_part = []
        remainder_map = {} 
        if remainder == 0:
            return sign + str(integer_part)
        
        # print('Line 17', remainder)
        while remainder != 0:
            if remainder in remainder_map:
                decimal_part.insert(remainder_map[remainder], "(")
                decimal_part.append(")")
                break
            
            remainder_map[remainder] = len(decimal_part)
            digit = remainder * 10 // denominator
            decimal_part.append(str(digit))
            remainder = remainder * 10 % denominator
            # print(remainder, digit, remainder_map)

        decimal_str = "".join(decimal_part)
        
        return sign + str(integer_part) + "." + decimal_str
                
            
            
            
        
        
        
        
        