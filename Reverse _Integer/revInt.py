class Solution:
    def reverse(self, x: int) -> int:
        num=x
        rev=0
        while(num!=0):
            rem=int(num%10 if x>0 else abs(num)%10)
            rev=rev*10 + rem
            num=int(num/10)

            if( rev>pow(2,31) or rev<-(pow(2,31)-1) ):
                return 0
            # if( rev>(2^31) or rev<((2^31)-1) ):
            #     return 0
                
        return rev if x>0 else -rev
        