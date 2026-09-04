class Solution:
    def intToRoman(self, num: int) -> str:
        
        s = num//1000 * 'M'
        num %= 1000

        if num>=900:
            s += 'CM'
        elif 900>num>499:
            s += 'D'
            s += ((num-500)//100) * 'C'
        elif num>399:
            s += 'CD'
        else:
            s += (num//100) * 'C'
        num %= 100
        
        if num>=90:
            s += 'XC'
        elif 90>num>49:
            s += 'L'
            s += ((num-50)//10) * 'X'
        elif num>39:
            s += 'XL'
        else:
            s += (num//10) * 'X'
        num %= 10
        
        if num>=9:
            s += 'IX'
        elif 9>num>4:
            s += 'V'
            s += (num-5) * 'I'
        elif num>3:
            s += 'IV'
        else:
            s += num * 'I'
        
        return s